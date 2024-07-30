import argparse
import json
import os
import re
from typing import List, Optional

from pydantic import BaseModel, Field


def parse_avro_type(avro_type, known_types):
    if isinstance(avro_type, list):
        if "null" in avro_type:
            non_null_type = [t for t in avro_type if t != "null"][0]
            return Optional[parse_avro_type(non_null_type, known_types)]
        else:
            return [parse_avro_type(t, known_types) for t in avro_type]
    elif avro_type == "string":
        return str
    elif avro_type == "long":
        return int
    elif avro_type == "double":
        return float
    elif avro_type == "boolean":
        return bool
    elif isinstance(avro_type, dict):
        if avro_type["type"] == "array":
            return List[parse_avro_type(avro_type["items"], known_types)]
        elif avro_type["type"] == "record":
            full_name = f"{avro_type.get('namespace', '')}.{avro_type['name']}".strip(
                "."
            )
            return known_types.get(full_name, full_name)
    elif isinstance(avro_type, str) and avro_type in known_types:
        return known_types[avro_type]
    return avro_type


def build_dependency_graph(schema, dependencies, known_types):
    if isinstance(schema, dict) and schema.get("type") == "record":
        full_name = f"{schema.get('namespace', '')}.{schema['name']}".strip(".")
        if full_name not in dependencies:
            dependencies[full_name] = set()
        for field in schema["fields"]:
            field_type = field["type"]
            if isinstance(field_type, dict) and field_type.get("type") == "record":
                dep_full_name = (
                    f"{field_type.get('namespace', '')}.{field_type['name']}".strip(".")
                )
                dependencies[full_name].add(dep_full_name)
                build_dependency_graph(field_type, dependencies, known_types)
            elif isinstance(field_type, list):
                for t in field_type:
                    if isinstance(t, dict) and t.get("type") == "record":
                        dep_full_name = f"{t.get('namespace', '')}.{t['name']}".strip(
                            "."
                        )
                        dependencies[full_name].add(dep_full_name)
                        build_dependency_graph(t, dependencies, known_types)
                    elif isinstance(t, dict) and t.get("type") == "array":
                        item_type = t["items"]
                        if (
                            isinstance(item_type, dict)
                            and item_type.get("type") == "record"
                        ):
                            dep_full_name = f"{item_type.get('namespace', '')}.{item_type['name']}".strip(
                                "."
                            )
                            dependencies[full_name].add(dep_full_name)
                            build_dependency_graph(item_type, dependencies, known_types)
            elif isinstance(field_type, dict) and field_type.get("type") == "array":
                item_type = field_type["items"]
                if isinstance(item_type, dict) and item_type.get("type") == "record":
                    dep_full_name = (
                        f"{item_type.get('namespace', '')}.{item_type['name']}".strip(
                            "."
                        )
                    )
                    dependencies[full_name].add(dep_full_name)
                    build_dependency_graph(item_type, dependencies, known_types)


def topological_sort(dependencies):
    sorted_list = []
    while dependencies:
        acyclic = False
        for node, edges in list(dependencies.items()):
            for edge in edges:
                if edge in dependencies:
                    break
            else:
                acyclic = True
                del dependencies[node]
                sorted_list.append(node)
        if not acyclic:
            raise RuntimeError("A cyclic dependency occurred")
    return sorted_list


def avro_to_pydantic(avro_schema):
    models = {}
    known_types = {}

    def parse_record(name, namespace, fields):
        class_attrs = {}
        annotations = {}
        for field in fields:
            field_name = field["name"]
            field_type = parse_avro_type(field["type"], known_types)
            field_default = field.get("default", ...)
            annotations[field_name] = field_type
            class_attrs[field_name] = Field(default=field_default, alias=field_name)
        class_attrs["__annotations__"] = annotations
        model = type(name, (BaseModel,), class_attrs)
        full_name = f"{namespace}.{name}".strip(".")
        models[full_name] = model
        known_types[full_name] = full_name

    def parse_schema(schema):
        if isinstance(schema, dict) and schema.get("type") == "record":
            parse_record(schema["name"], schema.get("namespace", ""), schema["fields"])
            for field in schema["fields"]:
                if (
                    isinstance(field["type"], dict)
                    and field["type"].get("type") == "record"
                ):
                    parse_schema(field["type"])
                elif isinstance(field["type"], list):
                    for t in field["type"]:
                        if isinstance(t, dict) and t.get("type") == "record":
                            parse_schema(t)
                        elif isinstance(t, dict) and t.get("type") == "array":
                            item_type = t["items"]
                            if (
                                isinstance(item_type, dict)
                                and item_type.get("type") == "record"
                            ):
                                parse_schema(item_type)
                elif (
                    isinstance(field["type"], dict)
                    and field["type"].get("type") == "array"
                ):
                    item_type = field["type"]["items"]
                    if (
                        isinstance(item_type, dict)
                        and item_type.get("type") == "record"
                    ):
                        parse_schema(item_type)

    parse_schema(avro_schema)

    return models


def extract_type_name(type_str):
    # 匹配 Optional[List['...']]
    match = re.search(r"Optional\[List\['(.+?)'\]\]", type_str)
    if match:
        return f"List[{match.group(1).split('.')[-1]}]"

    # 匹配 Optional[ForwardRef('...')]
    match = re.search(r"Optional\[ForwardRef\('(.+?)'\)\]", type_str)
    if match:
        return f"Optional[{match.group(1).split('.')[-1]}]"

    # 匹配 List[ForwardRef('...')]
    match = re.search(r"List\[ForwardRef\('(.+?)'\)\]", type_str)
    if match:
        return f"List[{match.group(1).split('.')[-1]}]"

    # 匹配 ForwardRef('...')
    match = re.search(r"ForwardRef\('(.+?)'\)", type_str)
    if match:
        return match.group(1).split(".")[-1]

    # 匹配 List['...']
    match = re.search(r"List\['(.+?)'\]", type_str)
    if match:
        return f"List[{match.group(1).split('.')[-1]}]"

    # 匹配 Optional[List[...]]
    match = re.search(r"Optional\[List\[(.+?)\]\]", type_str)
    if match:
        return f"List[{match.group(1)}]"

    # 匹配 Optional[...]
    match = re.search(r"Optional\[(.+?)\]", type_str)
    if match:
        return f"Optional[{match.group(1)}]"

    # 匹配 List[...]
    match = re.search(r"List\[(.+?)\]", type_str)
    if match:
        return f"List[{match.group(1)}]"

    # 匹配 '...'
    match = re.search(r"'\s*(.+?)\s*'", type_str)
    if match:
        return match.group(1).split(".")[-1]

    # 如果没有匹配，返回原始字符串
    return type_str


def remove_namespace(field_type_str):
    field_type_str = extract_type_name(field_type_str)
    if "Optional[" in field_type_str:
        inner_type = field_type_str[9:-1]
        if "." in inner_type:
            inner_type = inner_type.split(".")[
                -1
            ]  # Keep only the type name without namespace
        field_type_str = f"Optional[{inner_type}]"

    if "List[" in field_type_str:
        inner_type = field_type_str[5:-1]
        if "." in inner_type:
            inner_type = inner_type.split(".")[
                -1
            ]  # Keep only the type name without namespace
        field_type_str = f"List[{inner_type}]"

    if "." in field_type_str:
        field_type_str = field_type_str.split(".")[
            -1
        ]  # Keep only the type name without namespace

    return field_type_str


def main():
    parser = argparse.ArgumentParser(description="Avro to pydantic with references.")
    parser.add_argument("--avsc", type=str, required=True, help="avro schema file.")
    parser.add_argument(
        "--output-file",
        type=str,
        required=True,
        help="Path to the output file where the resolved schema will be written.",
    )

    args = parser.parse_args()

    with open(f"{args.avsc}", "r") as f:
        avro_schema = json.load(f)

    # Step 1: Build dependency graph
    dependencies = {}
    known_types = {}
    build_dependency_graph(avro_schema, dependencies, known_types)

    # Step 2: Topological sort to determine the order of class definitions
    sorted_classes = topological_sort(dependencies)

    # Step 3: Parse schema and generate models
    models = avro_to_pydantic(avro_schema)

    os.makedirs(os.path.dirname(args.output_file), exist_ok=True)
    with open(f"{args.output_file}", "w") as f:
        f.write("from typing import List, Optional\n")
        f.write("from pydantic import BaseModel, Field\n\n")

        # Write class definitions in sorted order
        for class_name in sorted_classes:
            model = models[class_name]
            f.write(f"class {class_name.split('.')[-1]}(BaseModel):\n")
            annotations = model.__annotations__
            for field_name, field_type in annotations.items():
                field_type_str = str(field_type).replace("typing.", "")
                field_type_str = remove_namespace(field_type_str)
                default_value = model.model_fields[field_name].default
                if default_value is ...:
                    f.write(f"    {field_name}: {field_type_str}\n")
                else:
                    f.write(f"    {field_name}: {field_type_str} = {default_value}\n")
            f.write("\n")


if __name__ == "__main__":
    main()

import argparse
import glob
import json
import os


def load_and_combine_schemas(schema_files):
    # Load all schemas
    schemas = {}
    for schema_file in schema_files:
        with open(schema_file, "r") as f:
            schema = json.load(f)
            full_name = f"{schema.get('namespace', '')}.{schema['name']}".strip(".")
            schemas[full_name] = schema

    return schemas


def resolve_references(schema, combined_schemas, resolved_names):
    if isinstance(schema, dict):
        if "type" in schema:
            if isinstance(schema["type"], list):
                # Handle union types
                schema["type"] = [
                    (
                        resolve_references(t, combined_schemas, resolved_names)
                        if isinstance(t, str) and t in combined_schemas
                        else t
                    )
                    for t in schema["type"]
                ]
            elif isinstance(schema["type"], str) and schema["type"] in combined_schemas:
                # Check if the schema has already been resolved
                if schema["type"] in resolved_names:
                    return schema["type"]
                # Resolve the referenced schema and recursively resolve its references
                resolved_schema = resolve_references(
                    combined_schemas[schema["type"]], combined_schemas, resolved_names
                )
                # Ensure we keep the original type name for the resolved schema
                resolved_schema["name"] = schema["type"].split(".")[-1]
                resolved_names.add(schema["type"])
                return resolved_schema
        return {
            k: resolve_references(v, combined_schemas, resolved_names)
            for k, v in schema.items()
        }
    elif isinstance(schema, list):
        return [
            resolve_references(item, combined_schemas, resolved_names)
            for item in schema
        ]
    elif isinstance(schema, str) and schema in combined_schemas:
        # Check if the schema has already been resolved
        if schema in resolved_names:
            return schema
        # Resolve the referenced schema and recursively resolve its references
        resolved_schema = resolve_references(
            combined_schemas[schema], combined_schemas, resolved_names
        )
        # Ensure we keep the original type name for the resolved schema
        resolved_schema["name"] = schema.split(".")[-1]
        resolved_names.add(schema)
        return resolved_schema
    else:
        return schema


def get_files_in_directory(directory, extension="*.avsc"):
    try:
        # 使用 glob 获取指定目录中的所有 .avsc 文件
        files = glob.glob(os.path.join(directory, extension))

        # 过滤出文件
        files = [f for f in files if os.path.isfile(f)]

        return files
    except Exception as e:
        print(f"Error accessing directory {directory}: {e}")
        return []


def main():
    parser = argparse.ArgumentParser(
        description="Combine Avro schemas with references."
    )
    parser.add_argument(
        "--source-directory",
        type=str,
        required=True,
        help="Path to the directory containing schema files.",
    )
    parser.add_argument(
        "--output-file",
        type=str,
        required=True,
        help="Path to the output file where the resolved schema will be written.",
    )
    parser.add_argument(
        "--main-schema",
        type=str,
        required=True,
        help="The full name of the main schema to resolve (including namespace).",
    )

    args = parser.parse_args()

    schema_files = get_files_in_directory(args.source_directory)
    combined_schemas = load_and_combine_schemas(schema_files)

    if args.main_schema not in combined_schemas:
        print(
            f"Error: Main schema '{args.main_schema}' not found in the provided schemas."
        )
        exit(1)

    # Track already resolved schemas
    resolved_names = set()

    # Now resolve references in the main schema
    main_schema = combined_schemas[args.main_schema]
    resolved_main_schema = resolve_references(
        main_schema, combined_schemas, resolved_names
    )

    # Ensure the output directory exists
    output_dir = os.path.dirname(args.output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Write the resolved schema to the output file
    with open(args.output_file, "w") as output_file:
        json.dump(resolved_main_schema, output_file, indent=2)

    print(f"Resolved schema has been written to {args.output_file}")


if __name__ == "__main__":
    main()

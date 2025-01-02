import json
from typing import Type

from pydantic import BaseModel


def read_object(file_path: str, model: Type[BaseModel]) -> BaseModel:
    with open(file_path, "r") as file:
        data = json.load(file)

        # 假设 JSON 数据包含以下字段：topic, partition, offset, key, value
        return model(**data)


def read_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()

import json
from typing import Optional, Type
from pydantic import BaseModel


# 从文件读取 JSON 数据，并反序列化为 AmazonKafkaMessage 对象
def read_object(file_path:str,model:Type[BaseModel]) -> Optional[BaseModel]:
    with open(file_path, 'r') as file:
        
        data = json.load(file)
        
        # 假设 JSON 数据包含以下字段：topic, partition, offset, key, value
        return model(**data)

def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()
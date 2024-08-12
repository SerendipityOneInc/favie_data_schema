import json
from typing import Any, Dict
from favie_data_schema.favie.adapter.common.crawler_kakfa_message import CrawlerKafkaMessage


# 从文件读取 JSON 数据，并反序列化为 AmazonKafkaMessage 对象
def read_amazon_message(file_path: str = '/workspace/jobs/resources/amazon_message.json') -> CrawlerKafkaMessage:
    with open(file_path, 'r') as file:
        
        data = json.load(file)
        
        # 假设 JSON 数据包含以下字段：topic, partition, offset, key, value
        return CrawlerKafkaMessage(**data)

# 示例使用
if __name__ == "__main__":
    file_path = '/workspace/jobs/resources/amazon_message.json'  # 替换为你的 JSON 文件路径
    message = read_amazon_message(file_path)
    print(message)
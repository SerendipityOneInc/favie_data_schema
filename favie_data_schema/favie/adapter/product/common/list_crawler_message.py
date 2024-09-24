from typing import List, Optional, Type
from pydantic import BaseModel, Field
import json

class ListCrawlerMessage(BaseModel):
    host: Optional[str] = None,
    product_id: Optional[str] = None
    parser_name: Optional[str] = None
    title: Optional[str] = None
    category_id: Optional[str] = None
    crawl_result: Optional[BaseModel] = None
    task_id: Optional[int] = None
    page: Optional[int] = None
    create_time: Optional[str] = None
    update_time: Optional[str] = None
    
    @classmethod
    def deserialize(cls, message: str,crawl_result_model:Type[BaseModel]) -> 'ListCrawlerMessage':
        # 如果存在crawl_result并且它是字典类型，将其转换为JSON字符串
        data = json.loads(message)
        if 'crawl_result' in data and isinstance(data['crawl_result'], dict):
            data['crawl_result'] = crawl_result_model(**data['crawl_result'])
        return cls(**data)


from typing import List, Optional
from pydantic import BaseModel, Field
import json

class ListCrawlerMessage(BaseModel):
    product_id: Optional[str] = None
    parser_name: Optional[str] = None
    title: Optional[str] = None
    category_id: Optional[str] = None
    crawl_result: Optional[str] = None
    task_id: Optional[int] = None
    page: Optional[int] = None
    create_time: Optional[str] = None
    update_time: Optional[str] = None
    
    @classmethod
    def from_dict(cls, data: dict):
        # 如果存在crawl_result并且它是字典类型，将其转换为JSON字符串
        if 'crawl_result' in data and isinstance(data['crawl_result'], dict):
            data['crawl_result'] = json.dumps(data['crawl_result'], indent=4)
        return cls(**data)


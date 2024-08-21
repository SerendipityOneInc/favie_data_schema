from typing import Optional
from pydantic import BaseModel
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_detail import RainforestProductDetail

class CrawlerKafkaMessage(BaseModel):
    url : Optional[str] = None,
    host: Optional[str] = None,
    product_id: Optional[str] = None,
    product_title: Optional[str] = None,
    source: Optional[int] = None,
    parser_name : Optional[str] = None,
    crawl_result: Optional[RainforestProductDetail] = None
    raw_result: Optional[str] = None
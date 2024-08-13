import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from favie_data_schema.favie.data.crawl_data.crawler.common import Source
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_review import (
    RainforestProductReview,
)


class FavieSpiderProductReviewData(BaseModel):
    id: str = uuid.uuid1().hex  # UUID1
    url: str  # URL
    host: str  # 商品所在网站的域名，比如：www.amazon.com
    product_id: Optional[str] = None  # 商品ID，比如：Amazon为ASIN: B0CBLKS51N
    product_title: Optional[str] = None  # 商品Title
    parser_name: Optional[str] = None  # used for spider
    source: Optional[Source] = 0  # 数据来源
    raw_result: Optional[str] = (
        None  # 原始抓取结果，如果为Rainforest则为API则为Response的json结果，如果为自研爬虫则为原始html
    )
    crawl_result: Optional[RainforestProductReview] = (
        None  # 商品review解析结果，存储为JSON格式，遵循RainForest的数据模型
    )
    create_time: Optional[datetime] = Field(default_factory=datetime.now)  # 爬虫写入时间
    update_time: Optional[datetime] = Field(default_factory=datetime.now)  # 数据更新时间
    task_id: Optional[int] = None  # 爬虫任务ID

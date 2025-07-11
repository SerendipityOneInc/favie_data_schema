import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field

from favie_data_schema.favie.data.crawl_data.crawler.common import Source, SpiderCrawlStatus
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_detail import (
    RainforestProductDetail,
)


class FavieSpiderProductData(BaseModel):
    id: str = uuid.uuid1().hex  # UUID1
    url: str  # URL
    host: str  # 商品所在网站的域名，比如：www.amazon.com
    product_id: Optional[str] = None  # 商品ID，比如：Amazon为ASIN: B0CBLKS51N
    product_title: Optional[str] = None  # 商品Title
    parser_name: Optional[str] = None  # used for spider
    source: Optional[Source] = 0  # 数据来源
    raw_result: Optional[
        str
    ] = None  # 原始抓取结果，如果为Rainforest则为API则为Response的json结果，如果为自研爬虫则为原始html
    crawl_result: Optional[
        RainforestProductDetail
    ] = None  # 商品解析结果，存储为JSON格式，遵循RainForest的数据模型
    crawl_status: Optional[str] = None # 爬取状态 比如SpiderCrawlStatus.SUCCESS.msg
    mission: Optional[str] = None  # 业务上的任务概念
    task_id: Optional[int] = None  # 爬虫任务ID
    create_time: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))  # 爬虫写入时间，使用UTC
    update_time: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))  # 数据更新时间，使用UTC

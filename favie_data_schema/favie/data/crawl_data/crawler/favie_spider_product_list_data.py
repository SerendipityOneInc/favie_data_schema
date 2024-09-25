import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field

from favie_data_schema.favie.data.crawl_data.crawler.common import Source
from favie_data_schema.favie.data.crawl_data.crawler.stark_product_list import (
    StarkProductList,
)


class FavieSpiderProductListData(BaseModel):
    id: str = uuid.uuid1().hex  # UUID1
    host: Optional[str] = None  # 域名
    parser_name: Optional[str] = None  # used for spider
    category_id: Optional[str] = None  # 类目id
    page: Optional[int] = None  # 页码
    source: Optional[Source] = 0  # 数据来源
    mission: Optional[str] = None  # 业务上的任务概念
    task_id: Optional[int] = None  # 爬虫任务ID
    raw_result: Optional[
        str
    ] = None  # 原始抓取结果，如果为Rainforest则为API则为Response的json结果，如果为自研爬虫则为原始html
    crawl_result: Optional[
        StarkProductList
    ] = None  # 类目解析结果，存储为JSON格式，遵循RainForest的数据模型
    create_time: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))  # 爬虫写入时间，使用UTC
    update_time: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))  # 数据更新时间，使用UTC

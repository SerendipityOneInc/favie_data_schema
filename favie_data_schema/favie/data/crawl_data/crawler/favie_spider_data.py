'''
Author: ace-srp ace@srp.one
Date: 2024-11-12 18:20:08
LastEditors: ace-srp ace@srp.one
LastEditTime: 2024-11-12 18:21:49
FilePath: /favie_data_schema/favie_data_schema/favie/data/crawl_data/crawler/favie_spider_data.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from favie_data_schema.favie.data.crawl_data.crawler.common import Source
from favie_data_schema.favie.data.crawl_data.crawler.crawler_result import CrawlerResult


class ContentType(str, Enum):
    OTHER = "other"
    WEBPAGE = "webpage"
    SUBTITLE = "subtitle"
    AUDIO = "audio"
    VIDEO = "video"
    IMAGE = "image"


class FavieSpiderData(BaseModel):
    id: str = uuid.uuid1().hex
    url: str
    content_type: Optional[ContentType] = ContentType.OTHER
    source: Optional[Source] = 0
    spider: Optional[str] = None
    parser_name: Optional[str] = None  # 新增字段
    mission: Optional[str] = None      # 新增字段
    crawl_result: Optional[CrawlerResult] = None
    raw_result: Optional[str] = None   # 新增字段
    task_id: Optional[int] = None
    create_time: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
    update_time: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
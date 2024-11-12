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
    source: Optional[Source] = 0  # 数据来源
    spider: Optional[str] = None  # 爬虫名称, 由不同的content_type交给不同的爬虫处理解析
    parser_name: Optional[str] = None  # 爬虫解析器名称
    mission: Optional[str] = None      # 爬虫任务名称
    crawl_result: Optional[CrawlerResult] = None  # 爬虫结果
    raw_result: Optional[str] = None   # 源码存储
    task_id: Optional[int] = None  # 爬虫任务ID
    create_time: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))  # 爬虫写入时间，使用UTC
    update_time: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))  # 数据更新时间，使用UTC
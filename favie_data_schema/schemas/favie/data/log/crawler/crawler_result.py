from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional, Union
from uuid import UUID

from pydantic import BaseModel, Field


class CrawlerRequestInfo(BaseModel):
    use_api: bool = True
    api_base: str = "https://api.crawlbase.com/"
    api_params: Optional[str] = None


class ParsedWebPageContent(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    hostname: Optional[str] = None
    date: Optional[str] = None
    fingerprint: Optional[str] = None
    id: Optional[str] = None
    license: Optional[str] = None
    comments: Optional[str] = None
    raw_text: Optional[str] = None
    text: Optional[str] = None
    language: Optional[str] = None
    image: Optional[str] = None
    pagetype: Optional[str] = None
    filedate: Optional[str] = None
    source: Optional[str] = None
    source_hostname: Optional[str] = None
    excerpt: Optional[str] = None
    categories: Optional[str] = None
    tags: Optional[str] = None


class WebPageContent(BaseModel):
    raw_html: Optional[str] = None
    parsed_webpage_content: Optional[ParsedWebPageContent] = None


class SubTitleTrunk(BaseModel):
    trunck_content_str: Optional[str] = None
    trunck_content_position: Optional[int] = None


class SubtitleContent(BaseModel):
    concatenated_string: Optional[str] = None
    subtitle_trunks: Optional[List[SubTitleTrunk]] = None


class CrawlerResult(BaseModel):
    crawler_request_info: CrawlerRequestInfo
    original_status: int = Field(200, ge=-(2**31), le=(2**31 - 1))
    pc_status: int = Field(200, ge=-(2**31), le=(2**31 - 1))
    original_url: str
    url: str
    webpage: Optional[WebPageContent] = None
    subtitle: Optional[SubtitleContent] = None
    doc_filter_result: Optional[List[str]] = None

from typing import List, Optional

from pydantic import BaseModel

from favie_data_schema.favie.data.interface.common.favie_model import MetaInfo


class RequestImageItem(BaseModel):
    category: Optional[str] = None
    site: Optional[str] = None
    link: Optional[str] = None
    text: Optional[str] = None


class FavieImageItem(BaseModel):
    link: Optional[str] = None
    f_link: Optional[str] = None
    format: Optional[str] = None
    category: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    size: Optional[int] = None
    status: Optional[int] = None


class FavieImageCrawlResponse(BaseModel):
    source_type: Optional[int] = None
    source_id: Optional[str] = None
    images: Optional[List[FavieImageItem]] = None


class FavieImageCrawlRequest(BaseModel):
    source_type: Optional[int] = None
    source_type: Optional[int] = None
    source_id: Optional[str] = None
    images: Optional[List[RequestImageItem]] = None
    force: Optional[bool] = None
    meta_info: Optional[MetaInfo] = None

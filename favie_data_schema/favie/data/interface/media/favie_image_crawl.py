from typing import List, Optional

from pydantic import BaseModel

from favie_data_schema.favie.data.interface.common.favie_model import FavieImageItem, MetaInfo


class RequestImageItem(BaseModel):
    category: Optional[str] = None
    site: Optional[str] = None
    link: Optional[str] = None
    text: Optional[str] = None


class FavieImageCrawlResponse(BaseModel):
    source_type: Optional[int] = None
    source_id: Optional[str] = None
    images: Optional[List[FavieImageItem]] = None


class FavieImageCrawlRequest(BaseModel):
    source_type: Optional[int] = None
    source_id: Optional[str] = None
    images: Optional[List[RequestImageItem]] = None
    force: Optional[bool] = None
    meta_info: Optional[MetaInfo] = None

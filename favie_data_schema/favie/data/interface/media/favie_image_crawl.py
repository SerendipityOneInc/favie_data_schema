from typing import List, Optional

from pydantic import BaseModel


class ImageItem(BaseModel):
    category: Optional[str] = None
    site: Optional[str] = None
    url: Optional[str] = None
    text: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None


class MetaInfo(BaseModel):
    source_type: Optional[str] = None
    parser_name: Optional[str] = None
    parses_at: Optional[str] = None
    data_type: Optional[str] = None
    f_categories_update_at: Optional[str] = None
    f_images_crawl_send_at: Optional[str] = None
    f_categories_map_type: Optional[int] = None
    f_categories_map_version: Optional[int] = None
    f_categories_predict_score: Optional[float] = None
    source_1_updates_at: Optional[str] = None
    source_2_updates_at: Optional[str] = None
    source_3_updates_at: Optional[str] = None
    source_4_updates_at: Optional[str] = None
    source_5_updates_at: Optional[str] = None


class FavieImageCrawlResponse(BaseModel):
    source_type: Optional[int] = None
    source_id: Optional[str] = None
    images: Optional[List[ImageItem]] = None


class FavieImageCrawlRequest(BaseModel):
    source_type: Optional[int] = None
    source_id: Optional[str] = None
    images: Optional[List[ImageItem]] = None
    force: Optional[bool] = None
    meta_info: Optional[MetaInfo] = None

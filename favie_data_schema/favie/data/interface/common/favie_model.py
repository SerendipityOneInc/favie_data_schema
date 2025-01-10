from typing import List, Optional

from pydantic import BaseModel


class FavieTag(BaseModel):
    biz_name: Optional[str] = None
    tag_name: Optional[str] = None


class FavieImageItem(BaseModel):
    link: Optional[str] = None
    f_link: Optional[str] = None
    md5: Optional[str] = None
    desc: Optional[str] = None
    format: Optional[str] = None
    category: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    size: Optional[int] = None
    size_type: Optional[str] = None
    status: Optional[int] = None
    position: Optional[int] = None


class MetaInfo(BaseModel):
    source_type: Optional[str] = None
    parser_name: Optional[str] = None
    first_parser_name: Optional[str] = None
    parses_at: Optional[str] = None
    data_type: Optional[str] = None
    app_key: Optional[str] = None
    version: Optional[str] = None
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
    err_code: Optional[int] = None
    err_messages: Optional[List[str]] = None

from typing import List, Optional

from pydantic import BaseModel


class FavieTag(BaseModel):
    biz_name: Optional[str] = None
    tag_name: Optional[str] = None


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
    err_code: Optional[int] = None
    err_messages: Optional[List[str]] = None

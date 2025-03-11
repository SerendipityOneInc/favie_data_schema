from typing import Any, List, Optional

from favie_data_common.common.pydantic_utils import PydanticUtils
from pydantic import BaseModel, validator


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


class FavieDataAction(BaseModel):
    action_name: Optional[str] = None
    action_params: Optional[Any] = None


class MetaInfo(BaseModel):
    source_type: Optional[str] = None
    parser_name: Optional[str] = None
    first_parser_name: Optional[str] = None
    parses_at: Optional[str] = None
    data_type: Optional[str] = None
    app_key: Optional[str] = None
    version: Optional[str] = None

    actions: Optional[List[FavieDataAction]] = None

    @validator("actions", pre=True)
    def actions_validator(cls, value):
        return PydanticUtils.deserialize_data(List[FavieDataAction], value)

    mark_archive: Optional[bool] = None

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

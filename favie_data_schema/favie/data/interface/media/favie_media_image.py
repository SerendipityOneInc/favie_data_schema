from typing import Dict, Optional

from favie_data_common.common.pydantic_utils import PydanticUtils
from pydantic import BaseModel, field_validator


class FavieMediaImage(BaseModel):
    f_url: Optional[str] = None

    @field_validator("f_url", mode="before")
    def validate_f_url(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    site: Optional[str] = None

    @field_validator("site", mode="before")
    def validate_site(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    url: Optional[str] = None

    @field_validator("url", mode="before")
    def validate_url(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    format: Optional[str] = None

    @field_validator("format", mode="before")
    def validate_format(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    text: Optional[str] = None

    @field_validator("text", mode="before")
    def validate_text(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    color_mode: Optional[str] = None

    @field_validator("color_mode", mode="before")
    def validate_color_mode(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    exif: Optional[Dict] = None

    @field_validator("exif", mode="before")
    def validate_exif(cls, value):
        return PydanticUtils.deserialize_data(Dict, value)

    frames: Optional[int] = None

    @field_validator("frames", mode="before")
    def validate_frames(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    width: Optional[int] = None

    @field_validator("width", mode="before")
    def validate_width(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    height: Optional[int] = None

    @field_validator("height", mode="before")
    def validate_height(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    size: Optional[int] = None

    @field_validator("size", mode="before")
    def validate_size(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    size_type: Optional[str] = None

    @field_validator("size_type", mode="before")
    def validate_size_type(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    category: Optional[str] = None

    @field_validator("category", mode="before")
    def validate_category(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    source_type: Optional[int] = None

    @field_validator("source_type", mode="before")
    def validate_source_type(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    source_id: Optional[str] = None

    @field_validator("source_id", mode="before")
    def validate_source_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    error: Optional[str] = None

    @field_validator("error", mode="before")
    def validate_error(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    error_code: Optional[str] = None

    @field_validator("error_code", mode="before")
    def validate_error_code(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_updates_at: Optional[str] = None

    @field_validator("f_updates_at", mode="before")
    def validate_f_updates_at(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_creates_at: Optional[str] = None

    @field_validator("f_creates_at", mode="before")
    def validate_f_creates_at(cls, value):
        return PydanticUtils.deserialize_data(str, value)

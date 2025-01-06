from typing import Any, Dict, Optional

from favie_data_common.common.pydantic_utils import PydanticUtils
from pydantic import BaseModel, field_validator

from favie_data_schema.favie.data.interface.common.favie_model import MetaInfo
from favie_data_schema.favie.data.interface.product.favie_product import (
    AttrInfo,
    BaseInfo,
    DescInfo,
    MediaInfo,
    PriceInfo,
    SaleInfo,
)


class FavieProductDetailBase(BaseModel):
    base_info: Optional[BaseInfo] = None

    @field_validator("base_info", mode="before")
    def validate_base_info(cls, value):
        return PydanticUtils.deserialize_data(BaseInfo, value)

    price_info: Optional[PriceInfo] = None

    @field_validator("price_info", mode="before")
    def validate_price_info(cls, value):
        return PydanticUtils.deserialize_data(PriceInfo, value)

    desc_info: Optional[DescInfo] = None

    @field_validator("desc_info", mode="before")
    def validate_desc_info(cls, value):
        return PydanticUtils.deserialize_data(DescInfo, value)

    attr_info: Optional[AttrInfo] = None

    @field_validator("attr_info", mode="before")
    def validate_attr_info(cls, value):
        return PydanticUtils.deserialize_data(AttrInfo, value)

    media_info: Optional[MediaInfo] = None

    @field_validator("media_info", mode="before")
    def validate_media_info(cls, value):
        return PydanticUtils.deserialize_data(MediaInfo, value)

    sale_info: Optional[SaleInfo] = None

    @field_validator("sale_info", mode="before")
    def validate_sale_info(cls, value):
        return PydanticUtils.deserialize_data(SaleInfo, value)

    variants_str: Optional[str] = None

    @field_validator("variants_str", mode="before")
    def validate_variants_str(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    raw_data: Optional[str] = None

    @field_validator("raw_data", mode="before")
    def validate_raw_data(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_images_tags: Optional[Dict[str, Dict[str, Any]]] = None

    @field_validator("f_images_tags", mode="before")
    def validate_f_images_tags(cls, value):
        return PydanticUtils.deserialize_data(Dict[str, Dict[str, Any]], value)

    f_images_bg_remove: Optional[Dict[str, Dict[str, Any]]] = None

    @field_validator("f_images_bg_remove", mode="before")
    def validate_f_images_bg_remove(cls, value):
        return PydanticUtils.deserialize_data(Dict[str, Dict[str, Any]], value)

    f_cate_tags: Optional[str] = None

    @field_validator("f_cate_tags", mode="before")
    def validate_f_cate_tags(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_meta: Optional[MetaInfo] = None

    @field_validator("f_meta", mode="before")
    def validate_f_meta(cls, value):
        return PydanticUtils.deserialize_data(MetaInfo, value)

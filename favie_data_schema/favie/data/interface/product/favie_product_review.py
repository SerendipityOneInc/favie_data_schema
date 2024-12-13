from typing import List, Optional

from favie_data_common.common.pydantic_utils import PydanticUtils
from pydantic import BaseModel, field_validator

from favie_data_schema.favie.data.interface.common.favie_model import FavieImageItem, FavieTag, MetaInfo
from favie_data_schema.favie.data.interface.product.favie_product import AttributeItem


class FavieProductReview(BaseModel):
    f_review_id: Optional[str] = None

    @field_validator("f_review_id", mode="before")
    def validate_f_review_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_spu_id: Optional[str] = None

    @field_validator("f_spu_id", mode="before")
    def validate_f_spu_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    site: Optional[str] = None

    @field_validator("site", mode="before")
    def validate_site(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    spu_id: Optional[str] = None

    @field_validator("spu_id", mode="before")
    def validate_spu_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    sku_id: Optional[str] = None

    @field_validator("sku_id", mode="before")
    def validate_sku_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    review_id: Optional[str] = None

    @field_validator("review_id", mode="before")
    def validate_review_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    title: Optional[str] = None

    @field_validator("title", mode="before")
    def validate_title(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    body: Optional[str] = None

    @field_validator("body", mode="before")
    def validate_body(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    body_html: Optional[str] = None

    @field_validator("body_html", mode="before")
    def validate_body_html(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    link: Optional[str] = None

    @field_validator("link", mode="before")
    def validate_link(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    images: Optional[List[str]] = None

    @field_validator("images", mode="before")
    def validate_images(cls, value):
        return PydanticUtils.deserialize_data(List[str], value)

    f_images: Optional[List[str]] = None

    @field_validator("f_images", mode="before")
    def validate_f_images(cls, value):
        return PydanticUtils.deserialize_data(List[str], value)

    f_image_list: Optional[List[FavieImageItem]] = None

    @field_validator("f_image_list", mode="before")
    def validate_f_image_list(cls, value):
        return PydanticUtils.deserialize_data(List[FavieImageItem], value)

    f_system_tags: Optional[List[FavieTag]] = None

    @field_validator("f_system_tags", mode="before")
    def validate_f_system_tags(cls, value):
        return PydanticUtils.deserialize_data(List[FavieTag], value)

    videos: Optional[List[str]] = None

    @field_validator("videos", mode="before")
    def validate_videos(cls, value):
        return PydanticUtils.deserialize_data(List[str], value)

    f_videos: Optional[List[str]] = None

    @field_validator("f_videos", mode="before")
    def validate_f_videos(cls, value):
        return PydanticUtils.deserialize_data(List[str], value)

    rating: Optional[float] = None

    @field_validator("rating", mode="before")
    def validate_rating(cls, value):
        return PydanticUtils.deserialize_data(float, value)

    date_raw: Optional[str] = None

    @field_validator("date_raw", mode="before")
    def validate_date_raw(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    date_utc: Optional[str] = None

    @field_validator("date_utc", mode="before")
    def validate_date_utc(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    author_name: Optional[str] = None

    @field_validator("author_name", mode="before")
    def validate_author_name(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    author_id: Optional[str] = None

    @field_validator("author_id", mode="before")
    def validate_author_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    author_url: Optional[str] = None

    @field_validator("author_url", mode="before")
    def validate_author_url(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    vine_program: Optional[bool] = None

    @field_validator("vine_program", mode="before")
    def validate_vine_program(cls, value):
        return PydanticUtils.deserialize_data(bool, value)

    verified_purchase: Optional[bool] = None

    @field_validator("verified_purchase", mode="before")
    def validate_verified_purchase(cls, value):
        return PydanticUtils.deserialize_data(bool, value)

    review_country: Optional[str] = None

    @field_validator("review_country", mode="before")
    def validate_review_country(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    is_global_review: Optional[bool] = None

    @field_validator("is_global_review", mode="before")
    def validate_is_global_review(cls, value):
        return PydanticUtils.deserialize_data(bool, value)

    position: Optional[int] = None

    @field_validator("position", mode="before")
    def validate_position(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    attributes: Optional[List[AttributeItem]] = None

    @field_validator("attributes", mode="before")
    def validate_attributes(cls, value):
        return PydanticUtils.deserialize_data(List[AttributeItem], value)

    helpful_votes: Optional[int] = None

    @field_validator("helpful_votes", mode="before")
    def validate_helpful_votes(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    unhelpful_votes: Optional[int] = None

    @field_validator("unhelpful_votes", mode="before")
    def validate_unhelpful_votes(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    stark_tag: Optional[int] = None

    @field_validator("stark_tag", mode="before")
    def validate_stark_tag(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    stark_tags: Optional[List[int]] = None

    @field_validator("stark_tags", mode="before")
    def validate_stark_tags(cls, value):
        return PydanticUtils.deserialize_data(List[int], value)

    f_status: Optional[str] = None

    @field_validator("f_status", mode="before")
    def validate_f_status(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_meta: Optional[MetaInfo] = None

    @field_validator("f_meta", mode="before")
    def validate_f_meta(cls, value):
        return PydanticUtils.deserialize_data(MetaInfo, value)

    f_updates_at: Optional[str] = None

    @field_validator("f_updates_at", mode="before")
    def validate_f_updates_at(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_creates_at: Optional[str] = None

    @field_validator("f_creates_at", mode="before")
    def validate_f_creates_at(cls, value):
        return PydanticUtils.deserialize_data(str, value)

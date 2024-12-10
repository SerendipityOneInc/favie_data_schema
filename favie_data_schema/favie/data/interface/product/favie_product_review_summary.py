from typing import List, Optional

from favie_data_common.common.pydantic_utils import PydanticUtils
from pydantic import BaseModel, field_validator

from favie_data_schema.favie.data.interface.common.favie_model import MetaInfo


class FavieProductReviewSummary(BaseModel):
    f_spu_id: Optional[str] = None

    @field_validator("f_spu_id", mode="before")
    def validate_f_spu_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    link: Optional[str] = None

    @field_validator("link", mode="before")
    def validate_link(cls, value):
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

    rating: Optional[float] = None

    @field_validator("rating", mode="before")
    def validate_rating(cls, value):
        return PydanticUtils.deserialize_data(float, value)

    ratings_total: Optional[int] = None

    @field_validator("ratings_total", mode="before")
    def validate_ratings_total(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    ratings_total_filtered: Optional[int] = None

    @field_validator("ratings_total_filtered", mode="before")
    def validate_ratings_total_filtered(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    five_star: Optional[int] = None

    @field_validator("five_star", mode="before")
    def validate_five_star(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    four_star: Optional[int] = None

    @field_validator("four_star", mode="before")
    def validate_four_star(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    three_star: Optional[int] = None

    @field_validator("three_star", mode="before")
    def validate_three_star(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    two_star: Optional[int] = None

    @field_validator("two_star", mode="before")
    def validate_two_star(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    one_star: Optional[int] = None

    @field_validator("one_star", mode="before")
    def validate_one_star(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    recommended_percentage: Optional[float] = None

    @field_validator("recommended_percentage", mode="before")
    def validate_recommended_percentage(cls, value):
        return PydanticUtils.deserialize_data(float, value)

    reviews_total: Optional[int] = None

    @field_validator("reviews_total", mode="before")
    def validate_reviews_total(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    reviews_total_filtered: Optional[int] = None

    @field_validator("reviews_total_filtered", mode="before")
    def validate_reviews_total_filtered(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    top_reviews: Optional[List[str]] = None

    @field_validator("top_reviews", mode="before")
    def validate_top_reviews(cls, value):
        return PydanticUtils.deserialize_data(List[str], value)

    top_favourable: Optional[str] = None

    @field_validator("top_favourable", mode="before")
    def validate_top_favourable(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    top_critical: Optional[str] = None

    @field_validator("top_critical", mode="before")
    def validate_top_critical(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_status: Optional[str] = None

    @field_validator("f_status", mode="before")
    def validate_f_status(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_updates_at: Optional[str] = None

    @field_validator("f_updates_at", mode="before")
    def validate_f_updates_at(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_meta: Optional[MetaInfo] = None

    @field_validator("f_meta", mode="before")
    def validate_f_meta(cls, value):
        return PydanticUtils.deserialize_data(MetaInfo, value)

    f_creates_at: Optional[str] = None

    @field_validator("f_creates_at", mode="before")
    def validate_f_creates_at(cls, value):
        return PydanticUtils.deserialize_data(str, value)

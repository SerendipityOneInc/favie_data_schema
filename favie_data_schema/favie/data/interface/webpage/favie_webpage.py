from typing import List, Optional

from favie_data_common.common.pydantic_utils import PydanticUtils
from pydantic import BaseModel, field_validator

from favie_data_schema.favie.data.interface.common.favie_model import FavieImageItem, FavieTag, MetaInfo


class ImageData(BaseModel):
    url: Optional[str] = None
    desc: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None


class VideoData(BaseModel):
    url: Optional[str] = None
    desc: Optional[str] = None
    duration: Optional[int] = None


class ReferenceData(BaseModel):
    url: Optional[str] = None
    desc: Optional[str] = None


class ProductData(BaseModel):
    url: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None
    images: Optional[List[ImageData]] = None
    videos: Optional[List[VideoData]] = None


class WebpageAuthor(BaseModel):
    user_name: Optional[str] = None
    display_name: Optional[str] = None
    description: Optional[str] = None
    link: Optional[str] = None
    type: Optional[str] = None
    image_url: Optional[str] = None
    posts_count: Optional[int] = None
    followers_count: Optional[int] = None
    following_count: Optional[int] = None


class WebpageReviewSummary(BaseModel):
    upvotes_count: Optional[int] = None
    downvotes_count: Optional[int] = None
    views_count: Optional[int] = None
    comments_total: Optional[int] = None


class FavieWebpage(BaseModel):
    md5_id: Optional[str] = None

    @field_validator("md5_id", mode="before")
    def validate_md5_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    url: Optional[str] = None

    @field_validator("url", mode="before")
    def validate_url(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    host: Optional[str] = None

    @field_validator("host", mode="before")
    def validate_host(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    domain: Optional[str] = None

    @field_validator("domain", mode="before")
    def validate_domain(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_fingerprint: Optional[int] = None

    @field_validator("f_fingerprint", mode="before")
    def validate_f_fingerprint(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    favicon: Optional[str] = None

    @field_validator("favicon", mode="before")
    def validate_favicon(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    language: Optional[str] = None

    @field_validator("language", mode="before")
    def validate_language(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    title: Optional[str] = None

    @field_validator("title", mode="before")
    def validate_title(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    description: Optional[str] = None

    @field_validator("description", mode="before")
    def validate_description(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    author: Optional[str] = None

    @field_validator("author", mode="before")
    def validate_author(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    author_v1: Optional[WebpageAuthor] = None

    @field_validator("author_v1", mode="before")
    def validate_author_v1(cls, value):
        return PydanticUtils.deserialize_data(WebpageAuthor, value)

    keywords: Optional[List[str]] = None

    @field_validator("keywords", mode="before")
    def validate_keywords(cls, value):
        return PydanticUtils.deserialize_data(List[str], value)

    robots: Optional[List[str]] = None

    @field_validator("robots", mode="before")
    def validate_robots(cls, value):
        return PydanticUtils.deserialize_data(List[str], value)

    content: Optional[str] = None

    @field_validator("content", mode="before")
    def validate_content(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    content_type: Optional[str] = None

    @field_validator("content_type", mode="before")
    def validate_content_type(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    excerpt: Optional[str] = None

    @field_validator("excerpt", mode="before")
    def validate_excerpt(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    comments: Optional[List[str]] = None

    @field_validator("comments", mode="before")
    def validate_comments(cls, value):
        return PydanticUtils.deserialize_data(List[str], value)

    subtitles: Optional[List[str]] = None

    @field_validator("subtitles", mode="before")
    def validate_subtitles(cls, value):
        return PydanticUtils.deserialize_data(List[str], value)

    review_summary: Optional[WebpageReviewSummary] = None

    @field_validator("review_summary", mode="before")
    def validate_review_summary(cls, value):
        return PydanticUtils.deserialize_data(WebpageReviewSummary, value)

    images: Optional[List[ImageData]] = None

    @field_validator("images", mode="before")
    def validate_images(cls, value):
        return PydanticUtils.deserialize_data(List[ImageData], value)

    f_images: Optional[List[ImageData]] = None

    @field_validator("f_images", mode="before")
    def validate_f_images(cls, value):
        return PydanticUtils.deserialize_data(List[ImageData], value)

    f_image_list: Optional[List[FavieImageItem]] = None

    @field_validator("f_image_list", mode="before")
    def validate_f_image_list(cls, value):
        return PydanticUtils.deserialize_data(List[FavieImageItem], value)

    videos: Optional[List[VideoData]] = None

    @field_validator("videos", mode="before")
    def validate_videos(cls, value):
        return PydanticUtils.deserialize_data(List[VideoData], value)

    f_videos: Optional[List[VideoData]] = None

    @field_validator("f_videos", mode="before")
    def validate_f_videos(cls, value):
        return PydanticUtils.deserialize_data(List[VideoData], value)

    f_system_tags: Optional[List[FavieTag]] = None

    @field_validator("f_system_tags", mode="before")
    def validate_f_system_tags(cls, value):
        return PydanticUtils.deserialize_data(List[FavieTag], value)

    references: Optional[List[ReferenceData]] = None

    @field_validator("references", mode="before")
    def validate_references(cls, value):
        return PydanticUtils.deserialize_data(List[ReferenceData], value)

    products: Optional[List[ProductData]] = None

    @field_validator("products", mode="before")
    def validate_products(cls, value):
        return PydanticUtils.deserialize_data(List[ProductData], value)

    json_lds: Optional[List[str]] = None

    @field_validator("json_lds", mode="before")
    def validate_json_lds(cls, value):
        return PydanticUtils.deserialize_data(List[str], value)

    open_graphs: Optional[List[str]] = None

    @field_validator("open_graphs", mode="before")
    def validate_open_graphs(cls, value):
        return PydanticUtils.deserialize_data(List[str], value)

    twitter_cards: Optional[List[str]] = None

    @field_validator("twitter_cards", mode="before")
    def validate_twitter_cards(cls, value):
        return PydanticUtils.deserialize_data(List[str], value)

    page_type: Optional[str] = None

    @field_validator("page_type", mode="before")
    def validate_page_type(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_status: Optional[str] = None

    @field_validator("f_status", mode="before")
    def validate_f_status(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    ext_data: Optional[str] = None

    @field_validator("ext_data", mode="before")
    def validate_ext_data(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_meta: Optional[MetaInfo] = None

    @field_validator("f_meta", mode="before")
    def validate_f_meta(cls, value):
        return PydanticUtils.deserialize_data(MetaInfo, value)

    webpage_create_time: Optional[str] = None

    @field_validator("webpage_create_time", mode="before")
    def validate_webpage_create_time(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    create_time: Optional[str] = None

    @field_validator("create_time", mode="before")
    def validate_create_time(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    update_time: Optional[str] = None

    @field_validator("update_time", mode="before")
    def validate_update_time(cls, value):
        return PydanticUtils.deserialize_data(str, value)

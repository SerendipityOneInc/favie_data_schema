from typing import List, Optional

from pydantic import BaseModel

from favie_data_schema.favie.data.interface.common.favie_model import FavieTag, MetaInfo
from favie_data_schema.favie.data.interface.media.favie_image_crawl import FavieImageItem


class ImageData(BaseModel):
    url: Optional[str] = None
    desc: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None


class VideoData(BaseModel):
    url: Optional[str] = None
    desc: Optional[str] = None


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


class FavieWebpage(BaseModel):
    md5_id: Optional[str] = None
    url: Optional[str] = None
    host: Optional[str] = None
    domain: Optional[str] = None
    f_fingerprint: Optional[int] = None
    favicon: Optional[str] = None
    language: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    author: Optional[str] = None
    keywords: Optional[List[str]] = None
    robots: Optional[List[str]] = None
    content: Optional[str] = None
    content_type: Optional[str] = None
    excerpt: Optional[str] = None
    comments: Optional[List[str]] = None
    subtitles: Optional[List[str]] = None
    images: Optional[List[ImageData]] = None
    f_images: Optional[List[ImageData]] = None
    f_image_list: Optional[List[FavieImageItem]] = None
    videos: Optional[List[VideoData]] = None
    f_videos: Optional[List[VideoData]] = None
    f_system_tags: Optional[List[FavieTag]] = None
    references: Optional[List[ReferenceData]] = None
    products: Optional[List[ProductData]] = None
    json_lds: Optional[List[str]] = None
    open_graphs: Optional[List[str]] = None
    twitter_cards: Optional[List[str]] = None
    page_type: Optional[str] = None
    f_status: Optional[str] = None
    ext_data: Optional[str] = None
    f_meta: Optional[MetaInfo] = None
    create_time: Optional[str] = None
    update_time: Optional[str] = None

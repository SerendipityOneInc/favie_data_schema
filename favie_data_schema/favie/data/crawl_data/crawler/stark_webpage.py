from typing import List, Optional
from pydantic import BaseModel

class WebpageImage(BaseModel):
    url: Optional[str] = None
    desc: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None

class WebpageVideo(BaseModel):
    url: Optional[str] = None
    desc: Optional[str] = None
    duration: Optional[int] = None

class WebpageProduct(BaseModel):
    url: Optional[str] = None
    title: Optional[str] = None
    subhead: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None
    images: Optional[List[WebpageImage]] = None
    videos: Optional[List[WebpageVideo]] = None

class WebpageReference(BaseModel):
    url: Optional[str] = None
    desc: Optional[str] = None

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

class WebpageSubtitleChunk(BaseModel):
    start_time: Optional[float] = None # in seconds
    end_time: Optional[float] = None # in seconds
    text: Optional[str] = None

class WebpageComment(BaseModel):
    text: Optional[str] = None
    images: Optional[list[WebpageImage]] = None
    videos: Optional[list[WebpageVideo]] = None
    author: Optional[WebpageAuthor] = None
    created_at: Optional[str] = None # in ISO format
    upvotes_count: Optional[int] = None
    downvotes_count: Optional[int] = None
    comments: Optional[List["WebpageComment"]] = None

class WebpageItem(BaseModel):
    url: Optional[str] = None
    host: Optional[str] = None
    domain: Optional[str] = None
    favicon: Optional[str] = None
    language: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    author: Optional[str] = None  # [need to be deleted]
    author_v1: Optional[WebpageAuthor] = None
    keywords: Optional[List[str]] = None
    robots: Optional[List[str]] = None
    content: Optional[str] = None # text content of the webpage
    content_type: Optional[str] = None
    excerpt: Optional[str] = None
    comments: Optional[List[str]] = None
    subtitles: Optional[List[str]] = None  # [need to be deleted]
    subtitles_v1: Optional[List[WebpageSubtitleChunk]] = None
    upvotes_count: Optional[int] = None
    downvotes_count: Optional[int] = None
    views_count: Optional[int] = None
    comments_total: Optional[int] = None
    images: Optional[List[WebpageImage]] = None
    videos: Optional[List[WebpageVideo]] = None
    references: Optional[List[WebpageReference]] = None
    products: Optional[List[WebpageProduct]] = None
    json_lds: Optional[List[str]] = None
    open_graphs: Optional[List[str]] = None
    twitter_cards: Optional[List[str]] = None
    page_type: Optional[str] = None
    ext_data: Optional[str] = None  #extra data for the webpage, such as chapters, markdown, etc.
    create_time: Optional[str] = None
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

class WebpageItem(BaseModel):
    url: Optional[str] = None
    host: Optional[str] = None
    domain: Optional[str] = None
    favicon: Optional[str] = None
    language: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    author: Optional[str] = None
    keywords: Optional[List[str]] = None
    robots: Optional[List[str]] = None
    content: Optional[str] = None # text content of the webpage
    content_type: Optional[str] = None
    excerpt: Optional[str] = None
    comments: Optional[List[str]] = None
    subtitles: Optional[List[str]] = None
    images: Optional[List[WebpageImage]] = None
    videos: Optional[List[WebpageVideo]] = None
    references: Optional[List[WebpageReference]] = None
    products: Optional[List[WebpageProduct]] = None
    json_lds: Optional[List[str]] = None
    open_graphs: Optional[List[str]] = None
    twitter_cards: Optional[List[str]] = None
    page_type: Optional[str] = None
    ext_data: Optional[str] = None
    create_time: Optional[str] = None
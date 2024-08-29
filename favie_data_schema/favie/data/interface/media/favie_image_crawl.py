from typing import List, Optional
from pydantic import BaseModel, Field

class ImageItem(BaseModel):
    category: Optional[str] = None
    site: Optional[str] = None
    url: Optional[str] = None
    text: Optional[str] = None

class FavieImageCrawlResponse(BaseModel):
    source_type: Optional[int] = None
    source_id: Optional[str] = None
    images: Optional[List[ImageItem]] = None

class FavieImageCrawlRequest(BaseModel):
    source_type: Optional[int] = None
    source_id: Optional[str] = None
    images: Optional[List[ImageItem]] = None
    force: Optional[bool] = None


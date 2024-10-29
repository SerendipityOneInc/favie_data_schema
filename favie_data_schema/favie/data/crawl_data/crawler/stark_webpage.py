
from typing import List, Optional
from pydantic import BaseModel

class WebpageImage(BaseModel):
    url: Optional[str] = None
    desc: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None

class WebpageItem(BaseModel):
    url: Optional[str] = None
    host: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    author: Optional[str] = None
    tags: Optional[List[str]] = None
    page_type: Optional[str] = None
    images: Optional[List[WebpageImage]] = None
    create_time: Optional[str] = None
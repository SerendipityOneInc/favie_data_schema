from typing import List, Optional
from pydantic import BaseModel, Field

class FavieMediaImage(BaseModel):
    f_url: Optional[str] = None
    site: Optional[str] = None
    url: Optional[str] = None
    format: Optional[str] = None
    text: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    size: Optional[int] = None
    category: Optional[str] = None
    source_type: Optional[int] = None
    source_id: Optional[str] = None
    f_updates_at: Optional[str] = None
    f_creates_at: Optional[str] = None


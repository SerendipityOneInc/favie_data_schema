from typing import List, Optional
from pydantic import BaseModel, Field

class FavieReview(BaseModel):
    f_review_id: Optional[str] = None
    f_spu_id: Optional[str] = None
    site: Optional[str] = None
    spu_id: Optional[str] = None
    review_id: Optional[str] = None
    title: Optional[str] = None
    body: Optional[str] = None
    link: Optional[str] = None
    images: Optional[List[str]] = None
    rating: Optional[float] = None
    date: Optional[str] = None
    author_name: Optional[str] = None
    author_id: Optional[str] = None
    author_url: Optional[str] = None
    vine_program: Optional[bool] = None
    verified_purchase: Optional[bool] = None
    review_country: Optional[str] = None
    is_global_review: Optional[bool] = None
    position: Optional[int] = None
    helpful_votes: Optional[int] = None
    unhelpful_votes: Optional[int] = None
    f_updates_at: Optional[str] = None
    f_creates_at: Optional[str] = None


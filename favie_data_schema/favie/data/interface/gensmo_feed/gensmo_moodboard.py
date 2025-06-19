from typing import List, Optional

from pydantic import BaseModel

from favie_data_schema.api.data.product import FavieProductDetail


class Candidate(BaseModel):
    Primary: Optional[str] = None
    Secondary: Optional[str] = None
    Score: Optional[float] = None


class MoodBoardTag(BaseModel):
    Category: Optional[str] = None
    Candidates: Optional[List[Candidate]] = None


class GemMoodboard(BaseModel):
    moodboard_id: Optional[str] = None
    moodboard_image_url: Optional[str] = None
    moodboard_type: Optional[str] = None
    product_ids: Optional[List[str]] = None
    products: Optional[List[FavieProductDetail]] = None
    moodboard_op: Optional[str] = None
    moodboard_tags: Optional[List[MoodBoardTag]] = None

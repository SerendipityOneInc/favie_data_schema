
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict, Union
from uuid import UUID

from pydantic import BaseModel, Field


class RequestInfo(BaseModel):
    success: Optional[bool] = None
    credits_used: Optional[int] = None
    credits_used_this_request: Optional[int] = None
    credits_remaining: Optional[int] = None
    credits_reset_at: Optional[str] = None


class RequestParameters(BaseModel):
    amazon_domain: Optional[str] = None
    asin: Optional[str] = None
    type: Optional[str] = None


class RequestMetadata(BaseModel):
    created_at: Optional[str] = None
    processed_at: Optional[str] = None
    total_time_taken: Optional[float] = None
    amazon_url: Optional[str] = None


class SubTitle(BaseModel):
    text: Optional[str] = None
    link: Optional[str] = None


class Product(BaseModel):
    title: Optional[str] = None
    link: Optional[str] = None
    sub_title: Optional[SubTitle] = None
    image: Optional[str] = None
    asin: Optional[str] = None


class FiveStar(BaseModel):
    percentage: Optional[int] = None
    count: Optional[int] = None


class FourStar(BaseModel):
    percentage: Optional[int] = None
    count: Optional[int] = None


class ThreeStar(BaseModel):
    percentage: Optional[int] = None
    count: Optional[int] = None


class TwoStar(BaseModel):
    percentage: Optional[int] = None
    count: Optional[int] = None


class OneStar(BaseModel):
    percentage: Optional[int] = None
    count: Optional[int] = None


class RatingBreakdown(BaseModel):
    five_star: Optional[FiveStar] = None
    four_star: Optional[FourStar] = None
    three_star: Optional[ThreeStar] = None
    two_star: Optional[TwoStar] = None
    one_star: Optional[OneStar] = None


class Summary(BaseModel):
    rating: Optional[float] = None
    ratings_total: Optional[int] = None
    ratings_total_filtered: Optional[int] = None
    reviews_total_filtered: Optional[int] = None
    reviews_total: Optional[int] = None
    rating_breakdown: Optional[RatingBreakdown] = None


class Date(BaseModel):
    raw: Optional[str] = None
    utc: Optional[str] = None


class Profile(BaseModel):
    name: Optional[str] = None
    link: Optional[str] = None
    id: Optional[str] = None
    image: Optional[str] = None


class Reviews(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    body: Optional[str] = None
    asin: Optional[str] = None
    body_html: Optional[str] = None
    link: Optional[str] = None
    images: Optional[List[str]] = None
    rating: Optional[int] = None
    date: Optional[Date] = None
    profile: Optional[Profile] = None
    vine_program: Optional[bool] = None
    verified_purchase: Optional[bool] = None
    review_country: Optional[str] = None
    is_global_review: Optional[bool] = None
    position: Optional[int] = None
    helpful_votes: Optional[int] = None


class Pagination(BaseModel):
    ratings_total_filtered: Optional[int] = None
    reviews_total_filtered: Optional[int] = None
    reviews_total: Optional[int] = None
    total_results: Optional[int] = None
    total_pages: Optional[int] = None
    message: Optional[str] = None
    current_page: Optional[int] = None
    start: Optional[int] = None
    end: Optional[int] = None


class RainforestProductReview(BaseModel):
    request_info: Optional[RequestInfo] = None
    request_parameters: Optional[RequestParameters] = None
    request_metadata: Optional[RequestMetadata] = None
    product: Optional[Product] = None
    summary: Optional[Summary] = None
    reviews: Optional[List[Reviews]] = None
    pagination: Optional[Pagination] = None

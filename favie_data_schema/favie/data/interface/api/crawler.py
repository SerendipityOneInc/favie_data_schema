from decimal import Decimal
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from favie_data_schema.favie.data.crawl_data.crawler.favie_spider_data import (
    ContentType,
)

from favie_data_schema.favie.data.interface.product.favie_product import FavieProductDetail, FavieProductReview, ReviewSummary
from favie_data_schema.favie.data.interface.webpage.favie_webpage import FavieWebpage

class CrawlerStatus(Enum):
    """每个资源的状态"""

    NOTEXIST = "notexist"
    PROCESSING = "processing"
    SUCCESS = "success"
    FAILED = "failed"


class CrawlerDataRequest(BaseModel):
    """Crawler data request model."""

    url: str
    content_type: Optional[ContentType] = None


class CrawlerDataResponse(BaseModel):
    """Crawler data response model."""

    status: CrawlerStatus
    data: Optional[FavieWebpage] = None


class CrawlerProductDataRequest(BaseModel):
    """Crawler product data request model."""

    product_id: Optional[str] = None


class CrawlerProductDataResponse(BaseModel):
    """Crawler product data response model."""

    status: CrawlerStatus
    data: Optional[FavieProductDetail] = None


class CrawlerProductReviewDataResponse(BaseModel):
    """Crawler product review data response model."""

    status: CrawlerStatus
    data: Optional[list[FavieProductReview]] = None


class CrawlerProductReviewData(BaseModel):
    """Crawler product review data model."""
    review_summary: Optional[ReviewSummary] = None
    reviews: Optional[list[FavieProductReview]] = None
    
class MainImage(BaseModel):
    """
    Main image schema.
    """

    link: Optional[str] = None


class ProductCard(BaseModel):
    """
    Product card schema.
    """

    product_id: str = Field(alias="asin")
    title: str
    main_image: Optional[MainImage] = None
    images: Optional[List[MainImage]] = None
    link: Optional[str] = None
    origin_price: Optional[Decimal] = None
    current_price: Optional[Decimal] = None
    currency_symbol: Optional[str] = None
    discount: Optional[Decimal] = None
    rating: Optional[Decimal] = None
    ratings_total: Optional[int] = None
    sell_amount_last_month: Optional[int] = None
    brand: Optional[str] = None
    categories: Optional[List] = None
    source: Optional[str] = None
    source_icon: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)

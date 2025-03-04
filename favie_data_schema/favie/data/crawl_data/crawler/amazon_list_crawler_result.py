from typing import List, Optional, Dict
from pydantic import BaseModel, Field

class Category(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None

class Bestseller(BaseModel):
    link: Optional[str] = None
    category: Optional[str] = None

class Deal(BaseModel):
    link: Optional[str] = None
    badge_text: Optional[str] = None

class Price(BaseModel):
    symbol: Optional[str] = None
    value: Optional[float] = None
    currency: Optional[str] = None
    raw: Optional[str] = None
    name: Optional[str] = None
    is_primary: Optional[bool] = None
    is_rrp: Optional[bool] = None

class AmazonListCrawlResult(BaseModel):
    position: Optional[int] = None
    title: Optional[str] = None
    asin: Optional[str] = None
    link: Optional[str] = None
    recent_sales: Optional[str] = None
    categories: Optional[List[Category]] = None
    image: Optional[str] = None
    bestseller: Optional[Bestseller] = None
    deal: Optional[Deal] = None
    is_prime: Optional[bool] = None
    rating: Optional[float] = None
    ratings_total: Optional[int] = None
    prices: Optional[List[Price]] = None
    price: Optional[Price] = None


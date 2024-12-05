from typing import List, Optional

from pydantic import BaseModel


class Category(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None


class Bestseller(BaseModel):
    link: Optional[str] = None
    category: Optional[str] = None


class Images(BaseModel):
    link: Optional[str] = None


class Price(BaseModel):
    symbol: Optional[str] = None
    value: Optional[float] = None
    currency: Optional[str] = None
    raw: Optional[str] = None
    name: Optional[str] = None
    is_primary: Optional[bool] = None
    is_rrp: Optional[bool] = None
    asin: Optional[str] = None


class DealListItem(BaseModel):
    position: Optional[int] = None
    link: Optional[str] = None
    asin: Optional[str] = None
    title: Optional[str] = None
    starts_at: Optional[str] = None
    ends_at: Optional[str] = None
    deal_id: Optional[str] = None
    deal_link: Optional[str] = None
    image: Optional[str] = None
    deal_price: Optional[Price] = None
    current_price: Optional[Price] = None
    list_price: Optional[Price] = None
    percent_off: Optional[int] = None
    deal_type: Optional[str] = None
    is_lightning_deal: Optional[bool] = None


class ProductListItem(BaseModel):
    position: Optional[int] = None
    title: Optional[str] = None
    asin: Optional[str] = None
    link: Optional[str] = None
    categories: Optional[List[Category]] = None
    image: Optional[str] = None
    images: Optional[List[Images]] = None
    rating: Optional[float] = None
    ratings_total: Optional[int] = None
    prices: Optional[List[Price]] = None  # only support rf api
    price: Optional[Price] = None
    rrp: Optional[Price] = None


class StarkProductList(BaseModel):
    product_list: Optional[List[ProductListItem]] = None
    deal_list: Optional[List[DealListItem]] = None

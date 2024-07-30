from typing import List, Optional
from pydantic import BaseModel, Field

class Price(BaseModel):
    lower_value: Optional[int] = None
    upper_value: Optional[int] = None
    value: Optional[int] = None
    currency: Optional[str] = None
    updates_at: Optional[str] = None

class Images(BaseModel):
    main_image: Optional[str] = None
    images: List[nal[List[str]] = None

class Brand(BaseModel):
    name: Optional[str] = None
    link: Optional[str] = None

class StandardAttributes(BaseModel):
    is_used: Optional[bool] = None
    is_bundle: Optional[bool] = None
    is_auction: Optional[bool] = None
    has_coupon: Optional[bool] = None
    is_preorder: Optional[bool] = None
    is_best_seller: Optional[bool] = None
    is_best_offer: Optional[bool] = None
    is_marketplace_item: Optional[bool] = None
    is_private_brand: Optional[bool] = None
    recent_sales: Optional[int] = None
    bestsellers_rank: Optional[int] = None
    product_model_number: Optional[str] = None
    is_platform_choice: Optional[bool] = None

class Inventory(BaseModel):
    status: Optional[str] = None
    quantity_available: Optional[int] = None
    quantity_sold: Optional[int] = None

class SearchAliasItem(BaseModel):
    title: Optional[str] = None
    value: Optional[str] = None

class Deal(BaseModel):
    deal_id: Optional[str] = None
    title: Optional[str] = None
    image: Optional[str] = None
    link: Optional[str] = None
    deal_type: Optional[str] = None
    starts_at: Optional[str] = None
    ends_at: Optional[str] = None
    deal_price: Optional[Price] = None
    was_price: Optional[Price] = None
    list_price: Optional[Price] = None
    is_lightning_deal: Optional[bool] = None
    is_member_exclusive: Optional[bool] = None
    is_member: Optional[bool] = None
    free_shipping: Optional[bool] = None
    is_map: Optional[bool] = None
    description: Optional[str] = None

class Shipping(BaseModel):
    price: Optional[DeliveryPrice] = None
    service: Optional[str] = None
    ships_to: Optional[str] = None
    location: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    zipcode: Optional[str] = None
    store_id: Optional[str] = None
    delivery_estimate: Optional[str] = None

class Fulfillment(BaseModel):
    pickup: Optional[bool] = None
    delivery_from_store: Optional[bool] = None
    shipping: Optional[bool] = None

class ReturnPolicy(BaseModel):
    returns_accepted: Optional[bool] = None
    free_returns: Optional[bool] = None
    returns_raw: Optional[str] = None

class Promotion(BaseModel):
    why_buy: List[nal[List[str]] = None

class FavieProduct(BaseModel):
    f_parser_name: Optional[str] = None
    f_sku_id: Optional[str] = None
    f_spu_id: Optional[str] = None
    site: Optional[str] = None
    sku_id: Optional[str] = None
    spu_id: Optional[str] = None
    title: Optional[str] = None
    link: Optional[str] = None
    sub_title: Optional[str] = None
    sub_title_link: Optional[str] = None
    description: Optional[str] = None
    description_external_link: Optional[str] = None
    rich_product_description: Optional[str] = None
    price: Optional[Price] = None
    f_status: Optional[str] = None
    images: Optional[Images] = None
    f_images: Optional[Images] = None
    f_categories: List[CategoryItem] = None
    categories: List[CategoryItem] = None
    videos: List[Video] = None
    f_brand: Optional[Brand] = None
    brand: Optional[Brand] = None
    feature_bullets: List[nal[List[str]] = None
    attributes: List[AttributeItem] = None
    specifications: List[AttributeItem] = None
    standard_attributes: Optional[StandardAttributes] = None
    offers: List[Offer] = None
    seller: Optional[Seller] = None
    inventory: Optional[Inventory] = None
    keywords: Optional[str] = None
    search_alias: Optional[SearchAliasItem] = None
    deal: Optional[Deal] = None
    shipping: Optional[Shipping] = None
    fulfillment: Optional[Fulfillment] = None
    returns_policy: Optional[ReturnPolicy] = None
    variants: List[SimpleProduct] = None
    promotion: Optional[Promotion] = None
    f_updates_at: Optional[str] = None


from typing import List, Optional

from pydantic import BaseModel

from favie_data_schema.favie.data.interface.common.favie_model import FavieImageItem, FavieTag


class FavieCategoriesPredictResponse(BaseModel):
    ids: Optional[List[List[str]]] = None
    categories: Optional[List[List[str]]] = None
    scores: Optional[List[List[float]]] = None


class Price(BaseModel):
    lower_value: Optional[int] = None
    upper_value: Optional[int] = None
    value: Optional[int] = None
    currency: Optional[str] = None
    updates_at: Optional[str] = None
    source_type: Optional[str] = None
    parser_name: Optional[str] = None
    app_key: Optional[str] = None


class Images(BaseModel):
    main_image: Optional[str] = None
    images: Optional[List[str]] = None


class CategoryItem(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None


class Video(BaseModel):
    duration_seconds: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    link: Optional[str] = None
    thumbnail: Optional[str] = None
    is_hero_video: Optional[bool] = None
    title: Optional[str] = None


class Brand(BaseModel):
    name: Optional[str] = None
    link: Optional[str] = None


class AttributeItem(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None


class PlatformChoice(BaseModel):
    keywords: Optional[str] = None
    link: Optional[str] = None


class SellerRank(BaseModel):
    category: Optional[str] = None
    rank: Optional[int] = None
    link: Optional[str] = None


class Seller(BaseModel):
    name: Optional[str] = None
    link: Optional[str] = None
    id: Optional[str] = None
    rating: Optional[float] = None
    ratings_total: Optional[int] = None
    postive_feedback_percent: Optional[float] = None


class Inventory(BaseModel):
    status: Optional[str] = None
    quantity_available: Optional[int] = None
    quantity_sold: Optional[int] = None
    out_of_stock_at: Optional[str] = None
    updates_at: Optional[str] = None


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


class ReturnPolicy(BaseModel):
    returns_accepted: Optional[bool] = None
    free_returns: Optional[bool] = None
    returns_raw: Optional[str] = None


class RatingBreakdown(BaseModel):
    five_star: Optional[int] = None
    five_percentage: Optional[int] = None
    four_star: Optional[int] = None
    four_percentage: Optional[int] = None
    three_star: Optional[int] = None
    three_percentage: Optional[int] = None
    two_star: Optional[int] = None
    two_percentage: Optional[int] = None
    one_star: Optional[int] = None
    one_percentage: Optional[int] = None


class SimpleProduct(BaseModel):
    f_sku_id: Optional[str] = None
    source: Optional[str] = None
    sku_id: Optional[str] = None
    title: Optional[str] = None
    link: Optional[str] = None
    price: Optional[Price] = None
    images: Optional[Images] = None
    dimensions: Optional[List[AttributeItem]] = None


class Promotion(BaseModel):
    why_buy: Optional[List[str]] = None


class ExtendedInfo(BaseModel):
    is_used: Optional[bool] = None
    is_bundle: Optional[bool] = None
    is_auction: Optional[bool] = None
    has_coupon: Optional[bool] = None
    coupon_text: Optional[str] = None
    is_preorder: Optional[bool] = None
    is_best_seller: Optional[bool] = None
    is_best_offer: Optional[bool] = None
    is_marketplace_item: Optional[bool] = None
    is_private_brand: Optional[bool] = None
    recent_sales: Optional[int] = None
    product_model_number: Optional[str] = None
    platform_choice: Optional[PlatformChoice] = None
    last_month_sell_amount: Optional[int] = None


class ReviewSummary(BaseModel):
    link: Optional[str] = None
    rating: Optional[float] = None
    ratings_total: Optional[int] = None
    ratings_total_filtered: Optional[int] = None
    rating_breakdown: Optional[RatingBreakdown] = None
    recommended_percentage: Optional[float] = None
    reviews_total: Optional[int] = None
    reviews_total_filtered: Optional[int] = None
    top_reviews: Optional[List[str]] = None
    top_favourable: Optional[str] = None
    top_critical: Optional[str] = None
    f_updates_at: Optional[str] = None


class BaseInfo(BaseModel):
    request_sku_id: Optional[str] = None
    f_sku_id: Optional[str] = None
    f_spu_id: Optional[str] = None
    sku_id: Optional[str] = None
    spu_id: Optional[str] = None
    site: Optional[str] = None
    title: Optional[str] = None
    sub_title: Optional[str] = None
    sub_title_link: Optional[str] = None
    link: Optional[str] = None
    sku_link: Optional[str] = None
    brand: Optional[Brand] = None
    f_brand: Optional[Brand] = None
    keywords: Optional[str] = None
    categories: Optional[List[CategoryItem]] = None
    f_categories: Optional[List[CategoryItem]] = None
    # f_cate_tags: Optional[str] = None
    shop_id: Optional[str] = None
    shop_name: Optional[str] = None
    shop_site: Optional[str] = None
    link_in_shop: Optional[str] = None
    f_tags: Optional[List[str]] = None
    f_system_tags: Optional[List[FavieTag]] = None
    f_status: Optional[str] = None
    f_updates_at: Optional[str] = None
    f_creates_at: Optional[str] = None


class AttrInfo(BaseModel):
    extended_info: Optional[ExtendedInfo] = None
    specifications: Optional[List[AttributeItem]] = None
    attributes: Optional[List[AttributeItem]] = None


class DescInfo(BaseModel):
    description: Optional[str] = None
    description_external_link: Optional[str] = None
    rich_product_description: Optional[str] = None
    feature_bullets: Optional[List[str]] = None


class MediaInfo(BaseModel):
    f_videos: Optional[List[Video]] = None
    f_image_list: Optional[List[FavieImageItem]] = None
    f_images: Optional[Images] = None
    videos: Optional[List[Video]] = None
    images: Optional[Images] = None


class PriceInfo(BaseModel):
    price: Optional[Price] = None
    rrp: Optional[Price] = None


class SaleInfo(BaseModel):
    seller: Optional[Seller] = None
    returns_policy: Optional[ReturnPolicy] = None
    inventory: Optional[Inventory] = None
    deal: Optional[Deal] = None
    best_seller_rank: Optional[List[SellerRank]] = None
    promotion: Optional[Promotion] = None
    review_summary: Optional[ReviewSummary] = None
    f_historical_prices: Optional[List[Price]] = None

from typing import List, Optional
from pydantic import BaseModel, Field

class MetaInfo(BaseModel):
    source_type: Optional[str] = None
    parser_name: Optional[str] = None
    parses_at: Optional[str] = None
    f_categories_update_at: Optional[str] = None
    f_images_crawl_send_at: Optional[str] = None
    f_categories_map_success: Optional[bool] = None
    source_1_updates_at: Optional[str] = None
    source_2_updates_at: Optional[str] = None
    source_3_updates_at: Optional[str] = None
    source_4_updates_at: Optional[str] = None
    source_5_updates_at: Optional[str] = None

class RatingBreakdown(BaseModel):
    five_star: Optional[int] = None
    four_star: Optional[int] = None
    three_star: Optional[int] = None
    two_star: Optional[int] = None
    one_star: Optional[int] = None

class Price(BaseModel):
    lower_value: Optional[int] = None
    upper_value: Optional[int] = None
    value: Optional[int] = None
    currency: Optional[str] = None
    updates_at: Optional[str] = None

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

class DeliveryPrice(BaseModel):
    raw: Optional[str] = None
    currency: Optional[str] = None
    value: Optional[int] = None
    is_free: Optional[bool] = None

class Seller(BaseModel):
    name: Optional[str] = None
    link: Optional[str] = None
    id: Optional[str] = None
    rating: Optional[float] = None
    ratings_total: Optional[int] = None
    postive_feedback_percent: Optional[float] = None

class SellerRank(BaseModel):
    category: Optional[str] = None
    rank: Optional[int] = None
    link: Optional[str] = None

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

class SimpleProduct(BaseModel):
    f_sku_id: Optional[str] = None
    source: Optional[str] = None
    sku_id: Optional[str] = None
    title: Optional[str] = None
    link: Optional[str] = None
    price: Optional[Price] = None
    images: Optional[Images] = None
    attributes: Optional[List[AttributeItem]] = None

class Promotion(BaseModel):
    why_buy: Optional[List[str]] = None

class FavieProductReview(BaseModel):
    f_review_id: Optional[str] = None
    f_spu_id: Optional[str] = None
    site: Optional[str] = None
    spu_id: Optional[str] = None
    sku_id: Optional[str] = None
    review_id: Optional[str] = None
    title: Optional[str] = None
    body: Optional[str] = None
    body_html: Optional[str] = None
    link: Optional[str] = None
    images: Optional[List[str]] = None
    videos: Optional[List[str]] = None
    rating: Optional[float] = None
    date_raw: Optional[str] = None
    date_utc: Optional[str] = None
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
    f_meta: Optional[MetaInfo] = None
    f_updates_at: Optional[str] = None
    f_creates_at: Optional[str] = None

class ReviewSummary(BaseModel):
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

class StandardAttributes(BaseModel):
    is_used: Optional[bool] = None
    is_bundle: Optional[bool] = None
    is_auction: Optional[bool] = None
    is_member: Optional[bool] = None
    is_member_exclusive_deal: Optional[bool] = None
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

class Delivery(BaseModel):
    fulfilled_by_platform: Optional[bool] = None
    countdown: Optional[str] = None
    comments: Optional[str] = None
    price: Optional[DeliveryPrice] = None

class FavieProductReviewSummary(BaseModel):
    f_spu_id: Optional[str] = None
    site: Optional[str] = None
    spu_id: Optional[str] = None
    sku_id: Optional[str] = None
    summary: Optional[ReviewSummary] = None
    f_meta: Optional[MetaInfo] = None
    f_updates_at: Optional[str] = None
    f_creates_at: Optional[str] = None

class Offer(BaseModel):
    price: Optional[Price] = None
    minimum_order_quantity: Optional[int] = None
    maximum_order_quantity: Optional[int] = None
    standard_attributes: Optional[StandardAttributes] = None
    delivery: Optional[Delivery] = None
    seller: Optional[Seller] = None
    offer_id: Optional[str] = None
    is_member: Optional[bool] = None
    position: Optional[int] = None
    buybox_winner: Optional[bool] = None
    offer_sku_id: Optional[str] = None

class FavieProductDetail(BaseModel):
    f_sku_id: Optional[str] = None
    f_spu_id: Optional[str] = None
    site: Optional[str] = None
    sku_id: Optional[str] = None
    spu_id: Optional[str] = None
    title: Optional[str] = None
    link: Optional[str] = None
    spu_title: Optional[str] = None
    sub_title: Optional[str] = None
    sub_title_link: Optional[str] = None
    description: Optional[str] = None
    description_external_link: Optional[str] = None
    rich_product_description: Optional[str] = None
    price: Optional[Price] = None
    rrp: Optional[Price] = None
    f_status: Optional[str] = None
    images: Optional[Images] = None
    f_images: Optional[Images] = None
    f_categories: Optional[List[CategoryItem]] = None
    categories: Optional[List[CategoryItem]] = None
    videos: Optional[List[Video]] = None
    f_brand: Optional[Brand] = None
    brand: Optional[Brand] = None
    feature_bullets: Optional[List[str]] = None
    attributes: Optional[List[AttributeItem]] = None
    specifications: Optional[List[AttributeItem]] = None
    standard_attributes: Optional[StandardAttributes] = None
    offers: Optional[List[Offer]] = None
    best_seller_rank: Optional[List[SellerRank]] = None
    seller: Optional[Seller] = None
    inventory: Optional[Inventory] = None
    keywords: Optional[str] = None
    search_alias: Optional[SearchAliasItem] = None
    deal: Optional[Deal] = None
    shipping: Optional[Shipping] = None
    fulfillment: Optional[Fulfillment] = None
    returns_policy: Optional[ReturnPolicy] = None
    review_summary: Optional[ReviewSummary] = None
    variants: Optional[List[SimpleProduct]] = None
    promotion: Optional[Promotion] = None
    f_updates_at: Optional[str] = None
    f_creates_at: Optional[str] = None
    f_meta: Optional[MetaInfo] = None


from typing import Any, Dict, List, Optional

from favie_data_common.common.pydantic_utils import PydanticUtils
from pydantic import BaseModel, field_validator

from favie_data_schema.favie.data.interface.common.favie_model import FavieImageItem, FavieTag, MetaInfo
from favie_data_schema.favie.data.interface.common.favie_utils import deserialize_data


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


class FavieProductReviewSummary(BaseModel):
    f_spu_id: Optional[str] = None
    link: Optional[str] = None
    site: Optional[str] = None
    spu_id: Optional[str] = None
    sku_id: Optional[str] = None
    rating: Optional[float] = None
    ratings_total: Optional[int] = None
    ratings_total_filtered: Optional[int] = None
    five_star: Optional[int] = None
    four_star: Optional[int] = None
    three_star: Optional[int] = None
    two_star: Optional[int] = None
    one_star: Optional[int] = None
    recommended_percentage: Optional[float] = None
    reviews_total: Optional[int] = None
    reviews_total_filtered: Optional[int] = None
    top_reviews: Optional[List[str]] = None
    top_favourable: Optional[str] = None
    top_critical: Optional[str] = None
    f_status: Optional[str] = None
    f_updates_at: Optional[str] = None
    f_meta: Optional[MetaInfo] = None
    f_creates_at: Optional[str] = None


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
    f_images: Optional[List[str]] = None
    f_image_list: Optional[List[FavieImageItem]] = None
    f_system_tags: Optional[List[FavieTag]] = None
    videos: Optional[List[str]] = None
    f_videos: Optional[List[str]] = None
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
    stark_tag: Optional[int] = None
    stark_tags: Optional[List[int]] = None
    f_status: Optional[str] = None
    f_meta: Optional[MetaInfo] = None
    f_updates_at: Optional[str] = None
    f_creates_at: Optional[str] = None


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


class FavieProductDetail(BaseModel):
    f_sku_id: Optional[str] = None

    @field_validator("f_sku_id", mode="before")
    def validate_f_sku_id(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "f_sku_id")
        return deserialize_data(expected_type, value)

    f_spu_id: Optional[str] = None

    @field_validator("f_spu_id", mode="before")
    def validate_f_spu_id(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "f_spu_id")
        return deserialize_data(expected_type, value)

    site: Optional[str] = None

    @field_validator("site", mode="before")
    def validate_site(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "site")
        return deserialize_data(expected_type, value)

    sku_id: Optional[str] = None

    @field_validator("sku_id", mode="before")
    def validate_sku_id(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "sku_id")
        return deserialize_data(expected_type, value)

    spu_id: Optional[str] = None

    @field_validator("spu_id", mode="before")
    def validate_spu_id(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "spu_id")
        return deserialize_data(expected_type, value)

    request_sku_id: Optional[str] = None

    @field_validator("request_sku_id", mode="before")
    def validate_request_sku_id(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "request_sku_id")
        return deserialize_data(expected_type, value)

    title: Optional[str] = None

    @field_validator("title", mode="before")
    def validate_title(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "title")
        return deserialize_data(expected_type, value)

    link: Optional[str] = None

    @field_validator("link", mode="before")
    def validate_link(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "link")
        return deserialize_data(expected_type, value)

    sub_title: Optional[str] = None

    @field_validator("sub_title", mode="before")
    def validate_sub_title(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "sub_title")
        return deserialize_data(expected_type, value)

    sub_title_link: Optional[str] = None

    @field_validator("sub_title_link", mode="before")
    def validate_sub_title_link(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "sub_title_link")
        return deserialize_data(expected_type, value)

    shop_id: Optional[str] = None

    @field_validator("shop_id", mode="before")
    def validate_shop_id(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "shop_id")
        return deserialize_data(expected_type, value)

    shop_name: Optional[str] = None

    @field_validator("shop_name", mode="before")
    def validate_shop_name(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "shop_name")
        return deserialize_data(expected_type, value)

    shop_site: Optional[str] = None

    @field_validator("shop_site", mode="before")
    def validate_shop_site(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "shop_site")
        return deserialize_data(expected_type, value)

    link_in_shop: Optional[str] = None

    @field_validator("link_in_shop", mode="before")
    def validate_link_in_shop(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "link_in_shop")
        return deserialize_data(expected_type, value)

    description: Optional[str] = None

    @field_validator("description", mode="before")
    def validate_description(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "description")
        return deserialize_data(expected_type, value)

    description_external_link: Optional[str] = None

    @field_validator("description_external_link", mode="before")
    def validate_description_external_link(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "description_external_link")
        return deserialize_data(expected_type, value)

    rich_product_description: Optional[str] = None

    @field_validator("rich_product_description", mode="before")
    def validate_rich_product_description(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "rich_product_description")
        return deserialize_data(expected_type, value)

    price: Optional[Price] = None

    @field_validator("price", mode="before")
    def validate_price(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "price")
        return deserialize_data(expected_type, value)

    rrp: Optional[Price] = None

    @field_validator("rrp", mode="before")
    def validate_rrp(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "rrp")
        return deserialize_data(expected_type, value)

    f_historical_prices: Optional[List[Price]] = None

    @field_validator("f_historical_prices", mode="before")
    def validate_f_historical_prices(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "f_historical_prices")
        return deserialize_data(expected_type, value)

    historical_prices: Optional[List[Price]] = None

    @field_validator("historical_prices", mode="before")
    def validate_historical_prices(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "historical_prices")
        return deserialize_data(expected_type, value)

    f_images_tags: Optional[Dict[str, Dict[str, Any]]] = None

    @field_validator("f_images_tags", mode="before")
    def validate_f_images_tags(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "f_images_tags")
        return deserialize_data(expected_type, value)

    f_images_bg_remove: Optional[Dict[str, Dict[str, Any]]] = None

    @field_validator("f_images_bg_remove", mode="before")
    def validate_f_images_bg_remove(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "f_images_bg_remove")
        return deserialize_data(expected_type, value)

    f_tags: Optional[List[str]] = None

    @field_validator("f_tags", mode="before")
    def validate_f_tags(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "f_tags")
        return deserialize_data(expected_type, value)

    f_system_tags: Optional[List[FavieTag]] = None

    @field_validator("f_system_tags", mode="before")
    def validate_f_system_tags(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "f_system_tags")
        return deserialize_data(expected_type, value)

    f_cate_tags: Optional[str] = None

    @field_validator("f_cate_tags", mode="before")
    def validate_f_cate_tags(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "f_cate_tags")
        return deserialize_data(expected_type, value)

    f_status: Optional[str] = None

    @field_validator("f_status", mode="before")
    def validate_f_status(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "f_status")
        return deserialize_data(expected_type, value)

    images: Optional[Images] = None

    @field_validator("images", mode="before")
    def validate_images(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "images")
        return deserialize_data(expected_type, value)

    f_images: Optional[Images] = None

    @field_validator("f_images", mode="before")
    def validate_f_images(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "f_images")
        return deserialize_data(expected_type, value)

    f_image_list: Optional[List[FavieImageItem]] = None

    @field_validator("f_image_list", mode="before")
    def validate_f_image_list(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "f_image_list")
        return deserialize_data(expected_type, value)

    f_categories: Optional[List[CategoryItem]] = None

    @field_validator("f_categories", mode="before")
    def validate_f_categories(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "f_categories")
        return deserialize_data(expected_type, value)

    categories: Optional[List[CategoryItem]] = None

    @field_validator("categories", mode="before")
    def validate_categories(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "categories")
        return deserialize_data(expected_type, value)

    videos: Optional[List[Video]] = None

    @field_validator("videos", mode="before")
    def validate_videos(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "videos")
        return deserialize_data(expected_type, value)

    f_videos: Optional[List[Video]] = None

    @field_validator("f_videos", mode="before")
    def validate_f_videos(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "f_videos")
        return deserialize_data(expected_type, value)

    f_brand: Optional[Brand] = None

    @field_validator("f_brand", mode="before")
    def validate_f_brand(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "f_brand")
        return deserialize_data(expected_type, value)

    brand: Optional[Brand] = None

    @field_validator("brand", mode="before")
    def validate_brand(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "brand")
        return deserialize_data(expected_type, value)

    feature_bullets: Optional[List[str]] = None

    @field_validator("feature_bullets", mode="before")
    def validate_feature_bullets(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "feature_bullets")
        return deserialize_data(expected_type, value)

    attributes: Optional[List[AttributeItem]] = None

    @field_validator("attributes", mode="before")
    def validate_attributes(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "attributes")
        return deserialize_data(expected_type, value)

    specifications: Optional[List[AttributeItem]] = None

    @field_validator("specifications", mode="before")
    def validate_specifications(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "specifications")
        return deserialize_data(expected_type, value)

    extended_info: Optional[ExtendedInfo] = None

    @field_validator("extended_info", mode="before")
    def validate_extended_info(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "extended_info")
        return deserialize_data(expected_type, value)

    standard_attributes: Optional[ExtendedInfo] = None

    @field_validator("standard_attributes", mode="before")
    def validate_standard_attributes(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "standard_attributes")
        return deserialize_data(expected_type, value)

    best_seller_rank: Optional[List[SellerRank]] = None

    @field_validator("best_seller_rank", mode="before")
    def validate_best_seller_rank(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "best_seller_rank")
        return deserialize_data(expected_type, value)

    seller: Optional[Seller] = None

    @field_validator("seller", mode="before")
    def validate_seller(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "seller")
        return deserialize_data(expected_type, value)

    inventory: Optional[Inventory] = None

    @field_validator("inventory", mode="before")
    def validate_inventory(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "inventory")
        return deserialize_data(expected_type, value)

    keywords: Optional[str] = None

    @field_validator("keywords", mode="before")
    def validate_keywords(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "keywords")
        return deserialize_data(expected_type, value)

    deal: Optional[Deal] = None

    @field_validator("deal", mode="before")
    def validate_deal(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "deal")
        return deserialize_data(expected_type, value)

    returns_policy: Optional[ReturnPolicy] = None

    @field_validator("returns_policy", mode="before")
    def validate_returns_policy(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "returns_policy")
        return deserialize_data(expected_type, value)

    review_summary: Optional[ReviewSummary] = None

    @field_validator("review_summary", mode="before")
    def validate_review_summary(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "review_summary")
        return deserialize_data(expected_type, value)

    variants: Optional[List[SimpleProduct]] = None

    @field_validator("variants", mode="before")
    def validate_variants(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "variants")
        return deserialize_data(expected_type, value)

    promotion: Optional[Promotion] = None

    @field_validator("promotion", mode="before")
    def validate_promotion(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "promotion")
        return deserialize_data(expected_type, value)

    f_updates_at: Optional[str] = None

    @field_validator("f_updates_at", mode="before")
    def validate_f_updates_at(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "f_updates_at")
        return deserialize_data(expected_type, value)

    f_creates_at: Optional[str] = None

    @field_validator("f_creates_at", mode="before")
    def validate_f_creates_at(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "f_creates_at")
        return deserialize_data(expected_type, value)

    f_meta: Optional[MetaInfo] = None

    @field_validator("f_meta", mode="before")
    def validate_f_meta(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "f_meta")
        return deserialize_data(expected_type, value)

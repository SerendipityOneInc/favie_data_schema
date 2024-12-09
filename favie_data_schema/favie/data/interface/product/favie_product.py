import logging
from typing import Any, Dict, List, Optional

from favie_data_common.common.pydantic_utils import PydanticUtils
from pydantic import BaseModel, field_validator

from favie_data_schema.favie.data.interface.common.favie_model import FavieImageItem, FavieTag, MetaInfo


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


class HistoricalPricesDeserializer:
    @staticmethod
    def deserialize(value: str):
        try:
            if not value:
                return None
            return PydanticUtils.deserialize_data(List[Price], value)

        except Exception:
            try:
                prices = PydanticUtils.deserialize_data(dict[str, List[Price]], value)
                return HistoricalPricesDeserializer.group_to_list(prices)
            except Exception as e:
                logging.exception("Deserialize HistoricalPrices failed: %s", e)
                return None

    @staticmethod
    def group_to_list(prices: Dict[str, List[Price]]):
        if not prices:  # 如果 prices 是空的，返回 None
            return None

        result = []  # 创建一个空列表用于存放所有的 Price 对象
        for price_list in prices.values():  # 遍历字典中的每个 value（每个 value 是一个 Price 列表）
            for price in price_list:  # 遍历当前 Price 列表中的每个 Price 对象
                result.append(price)  # 将它追加到结果列表中
        return result


class FavieProductDetail(BaseModel):
    f_sku_id: Optional[str] = None

    @field_validator("f_sku_id", mode="before")
    def validate_f_sku_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_spu_id: Optional[str] = None

    @field_validator("f_spu_id", mode="before")
    def validate_f_spu_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    site: Optional[str] = None

    @field_validator("site", mode="before")
    def validate_site(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    sku_id: Optional[str] = None

    @field_validator("sku_id", mode="before")
    def validate_sku_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    spu_id: Optional[str] = None

    @field_validator("spu_id", mode="before")
    def validate_spu_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    request_sku_id: Optional[str] = None

    @field_validator("request_sku_id", mode="before")
    def validate_request_sku_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    title: Optional[str] = None

    @field_validator("title", mode="before")
    def validate_title(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    link: Optional[str] = None

    @field_validator("link", mode="before")
    def validate_link(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    sub_title: Optional[str] = None

    @field_validator("sub_title", mode="before")
    def validate_sub_title(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    sub_title_link: Optional[str] = None

    @field_validator("sub_title_link", mode="before")
    def validate_sub_title_link(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    shop_id: Optional[str] = None

    @field_validator("shop_id", mode="before")
    def validate_shop_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    shop_name: Optional[str] = None

    @field_validator("shop_name", mode="before")
    def validate_shop_name(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    shop_site: Optional[str] = None

    @field_validator("shop_site", mode="before")
    def validate_shop_site(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    link_in_shop: Optional[str] = None

    @field_validator("link_in_shop", mode="before")
    def validate_link_in_shop(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    description: Optional[str] = None

    @field_validator("description", mode="before")
    def validate_description(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    description_external_link: Optional[str] = None

    @field_validator("description_external_link", mode="before")
    def validate_description_external_link(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    rich_product_description: Optional[str] = None

    @field_validator("rich_product_description", mode="before")
    def validate_rich_product_description(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    price: Optional[Price] = None

    @field_validator("price", mode="before")
    def validate_price(cls, value):
        return PydanticUtils.deserialize_data(Price, value)

    rrp: Optional[Price] = None

    @field_validator("rrp", mode="before")
    def validate_rrp(cls, value):
        return PydanticUtils.deserialize_data(Price, value)

    f_historical_prices: Optional[List[Price]] = None

    @field_validator("f_historical_prices", mode="before")
    def validate_f_historical_prices(cls, value):
        return HistoricalPricesDeserializer.deserialize(value)

    historical_prices: Optional[List[Price]] = None

    @field_validator("historical_prices", mode="before")
    def validate_historical_prices(cls, value):
        return HistoricalPricesDeserializer.deserialize(value)

    f_images_tags: Optional[Dict[str, Dict[str, Any]]] = None

    @field_validator("f_images_tags", mode="before")
    def validate_f_images_tags(cls, value):
        return PydanticUtils.deserialize_data(Dict[str, Dict[str, Any]], value)

    f_images_bg_remove: Optional[Dict[str, Dict[str, Any]]] = None

    @field_validator("f_images_bg_remove", mode="before")
    def validate_f_images_bg_remove(cls, value):
        return PydanticUtils.deserialize_data(Dict[str, Dict[str, Any]], value)

    f_tags: Optional[List[str]] = None

    @field_validator("f_tags", mode="before")
    def validate_f_tags(cls, value):
        return PydanticUtils.deserialize_data(List[str], value)

    f_system_tags: Optional[List[FavieTag]] = None

    @field_validator("f_system_tags", mode="before")
    def validate_f_system_tags(cls, value):
        return PydanticUtils.deserialize_data(List[FavieTag], value)

    f_cate_tags: Optional[str] = None

    @field_validator("f_cate_tags", mode="before")
    def validate_f_cate_tags(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_status: Optional[str] = None

    @field_validator("f_status", mode="before")
    def validate_f_status(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    images: Optional[Images] = None

    @field_validator("images", mode="before")
    def validate_images(cls, value):
        return PydanticUtils.deserialize_data(Images, value)

    f_images: Optional[Images] = None

    @field_validator("f_images", mode="before")
    def validate_f_images(cls, value):
        return PydanticUtils.deserialize_data(Images, value)

    f_image_list: Optional[List[FavieImageItem]] = None

    @field_validator("f_image_list", mode="before")
    def validate_f_image_list(cls, value):
        return PydanticUtils.deserialize_data(List[FavieImageItem], value)

    f_categories: Optional[List[CategoryItem]] = None

    @field_validator("f_categories", mode="before")
    def validate_f_categories(cls, value):
        return PydanticUtils.deserialize_data(List[CategoryItem], value)

    categories: Optional[List[CategoryItem]] = None

    @field_validator("categories", mode="before")
    def validate_categories(cls, value):
        return PydanticUtils.deserialize_data(List[CategoryItem], value)

    videos: Optional[List[Video]] = None

    @field_validator("videos", mode="before")
    def validate_videos(cls, value):
        return PydanticUtils.deserialize_data(List[Video], value)

    f_videos: Optional[List[Video]] = None

    @field_validator("f_videos", mode="before")
    def validate_f_videos(cls, value):
        return PydanticUtils.deserialize_data(List[Video], value)

    f_brand: Optional[Brand] = None

    @field_validator("f_brand", mode="before")
    def validate_f_brand(cls, value):
        return PydanticUtils.deserialize_data(Brand, value)

    brand: Optional[Brand] = None

    @field_validator("brand", mode="before")
    def validate_brand(cls, value):
        return PydanticUtils.deserialize_data(Brand, value)

    feature_bullets: Optional[List[str]] = None

    @field_validator("feature_bullets", mode="before")
    def validate_feature_bullets(cls, value):
        return PydanticUtils.deserialize_data(List[str], value)

    attributes: Optional[List[AttributeItem]] = None

    @field_validator("attributes", mode="before")
    def validate_attributes(cls, value):
        return PydanticUtils.deserialize_data(List[AttributeItem], value)

    specifications: Optional[List[AttributeItem]] = None

    @field_validator("specifications", mode="before")
    def validate_specifications(cls, value):
        return PydanticUtils.deserialize_data(List[AttributeItem], value)

    extended_info: Optional[ExtendedInfo] = None

    @field_validator("extended_info", mode="before")
    def validate_extended_info(cls, value):
        return PydanticUtils.deserialize_data(ExtendedInfo, value)

    standard_attributes: Optional[ExtendedInfo] = None

    @field_validator("standard_attributes", mode="before")
    def validate_standard_attributes(cls, value):
        return PydanticUtils.deserialize_data(ExtendedInfo, value)

    best_seller_rank: Optional[List[SellerRank]] = None

    @field_validator("best_seller_rank", mode="before")
    def validate_best_seller_rank(cls, value):
        return PydanticUtils.deserialize_data(List[SellerRank], value)

    seller: Optional[Seller] = None

    @field_validator("seller", mode="before")
    def validate_seller(cls, value):
        return PydanticUtils.deserialize_data(Seller, value)

    inventory: Optional[Inventory] = None

    @field_validator("inventory", mode="before")
    def validate_inventory(cls, value):
        return PydanticUtils.deserialize_data(Inventory, value)

    keywords: Optional[str] = None

    @field_validator("keywords", mode="before")
    def validate_keywords(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    deal: Optional[Deal] = None

    @field_validator("deal", mode="before")
    def validate_deal(cls, value):
        return PydanticUtils.deserialize_data(Deal, value)

    returns_policy: Optional[ReturnPolicy] = None

    @field_validator("returns_policy", mode="before")
    def validate_returns_policy(cls, value):
        return PydanticUtils.deserialize_data(ReturnPolicy, value)

    review_summary: Optional[ReviewSummary] = None

    @field_validator("review_summary", mode="before")
    def validate_review_summary(cls, value):
        return PydanticUtils.deserialize_data(ReviewSummary, value)

    variants: Optional[List[SimpleProduct]] = None

    @field_validator("variants", mode="before")
    def validate_variants(cls, value):
        return PydanticUtils.deserialize_data(List[SimpleProduct], value)

    promotion: Optional[Promotion] = None

    @field_validator("promotion", mode="before")
    def validate_promotion(cls, value):
        return PydanticUtils.deserialize_data(Promotion, value)

    f_updates_at: Optional[str] = None

    @field_validator("f_updates_at", mode="before")
    def validate_f_updates_at(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_creates_at: Optional[str] = None

    @field_validator("f_creates_at", mode="before")
    def validate_f_creates_at(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_meta: Optional[MetaInfo] = None

    @field_validator("f_meta", mode="before")
    def validate_f_meta(cls, value):
        return PydanticUtils.deserialize_data(MetaInfo, value)

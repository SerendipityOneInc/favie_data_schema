from typing import List, Optional, Union

from pydantic import BaseModel


class RequestInfo(BaseModel):
    success: Optional[bool] = None
    credits_used: Optional[int] = None
    credits_remaining: Optional[int] = None


class RequestMetadata(BaseModel):
    id: Optional[str] = None
    created_at: Optional[str] = None
    processed_at: Optional[str] = None
    total_time_taken: Optional[float] = None
    amazon_url: Optional[str] = None


class RequestParameters(BaseModel):
    type: Optional[str] = None
    url: Optional[str] = None


class StarkShop(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    host: Optional[str] = None


class Specifications(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None


class Price(BaseModel):
    symbol: Optional[str] = None
    currency: Optional[str] = None
    value: Optional[float] = None
    raw: Optional[str] = None


class Variants(BaseModel):
    asin: Optional[str] = None
    text: Optional[str] = None
    dimensions: Optional[List[Specifications]] = None
    link: Optional[str] = None
    price: Optional[Price] = None


class Categories(BaseModel):
    name: Optional[str] = None
    link: Optional[str] = None
    category_id: Optional[str] = None


class BestsellersRank(BaseModel):
    category: Optional[str] = None
    rank: Optional[int] = None
    link: Optional[str] = None


class SummarizationAttributes(BaseModel):
    name: Optional[str] = None
    value: Optional[float] = None
    id: Optional[str] = None


class AmazonsChoice(BaseModel):
    keywords: Optional[str] = None
    link: Optional[str] = None


class ClimatePledgeFriendly(BaseModel):
    text: Optional[str] = None
    image: Optional[str] = None
    link: Optional[str] = None


class Promotions(BaseModel):
    name: Optional[str] = None


class FirstAvailable(BaseModel):
    raw: Optional[str] = None
    utc: Optional[str] = None


class SubTitle(BaseModel):
    text: Optional[str] = None
    link: Optional[str] = None


class StarRating(BaseModel):
    percentage: Optional[int] = None
    count: Optional[int] = None


class RatingBreakdown(BaseModel):
    five_star: Optional[StarRating] = None
    four_star: Optional[StarRating] = None
    three_star: Optional[StarRating] = None
    two_star: Optional[StarRating] = None
    one_star: Optional[StarRating] = None


class Date(BaseModel):
    raw: Optional[str] = None
    utc: Optional[str] = None


class Profile(BaseModel):
    name: Optional[str] = None
    link: Optional[str] = None
    id: Optional[str] = None


class Attributes(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None


class TopReviews(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    body: Optional[str] = None
    body_html: Optional[str] = None
    link: Optional[str] = None
    stark_images: Optional[List[str]] = None
    stark_attributes: Optional[List[Attributes]] = None
    rating: Optional[int] = None
    date: Optional[Date] = None
    profile: Optional[Profile] = None
    vine_program: Optional[bool] = None
    verified_purchase: Optional[bool] = None
    helpful_votes: Optional[int] = None
    review_country: Optional[str] = None
    is_global_review: Optional[bool] = None


class MainImage(BaseModel):
    link: Optional[str] = None


class Images(BaseModel):
    link: Optional[str] = None


class Videos(BaseModel):
    duration_seconds: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    url: Optional[str] = None
    thumbnail: Optional[str] = None
    is_hero_video: Optional[bool] = None
    variant: Optional[str] = None
    title: Optional[str] = None
    group_id: Optional[str] = None
    group_type: Optional[str] = None


class Sections(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None


class ImportantInformation(BaseModel):
    sections: Optional[List[Sections]] = None


class MinimumOrderQuantity(BaseModel):
    value: Optional[int] = None
    message: Optional[str] = None


class Availability(BaseModel):
    type: Optional[str] = None
    raw: Optional[str] = None
    dispatch_days: Optional[int] = None


class ThirdPartySeller(BaseModel):
    name: Optional[str] = None
    link: Optional[str] = None


class Fulfillment(BaseModel):
    type: Optional[str] = None
    is_sold_by_amazon: Optional[bool] = None
    is_fulfilled_by_amazon: Optional[bool] = None
    is_fulfilled_by_third_party: Optional[bool] = None
    is_sold_by_third_party: Optional[bool] = None
    third_party_seller: Optional[ThirdPartySeller] = None


class Claimed(BaseModel):
    percentage: Optional[int] = None
    raw: Optional[str] = None


class Timing(BaseModel):
    raw: Optional[str] = None
    ends_at: Optional[str] = None
    remaining_hours: Optional[int] = None
    remaining_minutes: Optional[int] = None
    remaining_seconds: Optional[int] = None


class Deal(BaseModel):
    claimed: Optional[Claimed] = None
    timing: Optional[Timing] = None


class NewOffersFrom(BaseModel):
    symbol: Optional[str] = None
    value: Optional[float] = None
    currency: Optional[str] = None
    raw: Optional[str] = None


class UsedOffersFrom(BaseModel):
    symbol: Optional[str] = None
    value: Optional[float] = None
    currency: Optional[str] = None
    raw: Optional[str] = None


class MixedOffersFrom(BaseModel):
    symbol: Optional[str] = None
    value: Optional[float] = None
    currency: Optional[str] = None
    raw: Optional[str] = None


class BuyboxWinner(BaseModel):
    minimum_order_quantity: Optional[MinimumOrderQuantity] = None
    offer_id: Optional[str] = None
    is_prime: Optional[bool] = None
    is_prime_exclusive_deal: Optional[bool] = None
    availability: Optional[Availability] = None
    fulfillment: Optional[Fulfillment] = None
    deal: Optional[Deal] = None
    price: Optional[Price] = None
    rrp: Optional[Price] = None
    new_offers_count: Optional[int] = None
    new_offers_from: Optional[NewOffersFrom] = None
    used_offers_count: Optional[int] = None
    used_offers_from: Optional[UsedOffersFrom] = None
    mixed_offers_count: Optional[int] = None
    mixed_offers_from: Optional[MixedOffersFrom] = None


class MoreBuyingChoices(BaseModel):
    price: Optional[Price] = None
    seller_name: Optional[str] = None
    seller_link: Optional[str] = None
    free_shipping: Optional[bool] = None
    position: Optional[int] = None


class Services(BaseModel):
    title: Optional[str] = None
    price: Optional[Price] = None
    whats_included: Optional[List[str]] = None


class Product(BaseModel):
    title: Optional[str] = None
    title_excluding_variant_name: Optional[str] = None
    stark_shop: Optional[StarkShop] = None
    stark_link_in_shop: Optional[str] = None
    variants: Optional[List[Variants]] = None
    keywords: Optional[str] = None
    keywords_list: Optional[List[str]] = None
    link: Optional[str] = None
    asin: Optional[str] = None
    parent_asin: Optional[str] = None
    description: Optional[str] = None
    categories: Optional[List[Categories]] = None
    bestsellers_rank: Optional[List[BestsellersRank]] = None
    summarization_attributes: Optional[List[SummarizationAttributes]] = None
    amazons_choice: Optional[AmazonsChoice] = None
    recent_sales: Optional[str] = None
    climate_pledge_friendly: Optional[ClimatePledgeFriendly] = None
    kindle_unlimited: Optional[bool] = None
    has_coupon: Optional[bool] = None
    coupon_text: Optional[str] = None
    promotions: Optional[List[Promotions]] = None
    brand: Optional[str] = None
    weight: Optional[str] = None
    shipping_weight: Optional[str] = None
    first_available: Optional[Union[str, FirstAvailable]] = None
    delivery_message: Optional[str] = None
    dimensions: Optional[Union[str, List[Specifications]]] = None
    sub_title: Optional[SubTitle] = None
    rating: Optional[float] = None
    rating_breakdown: Optional[RatingBreakdown] = None
    ratings_total: Optional[int] = None
    reviews_total: Optional[int] = None
    top_reviews: Optional[List[TopReviews]] = None
    main_image: Optional[MainImage] = None
    images: Optional[List[Images]] = None
    videos: Optional[List[Videos]] = None
    is_bundle: Optional[bool] = None
    feature_bullets: Optional[List[str]] = None
    important_information: Optional[ImportantInformation] = None
    buybox_winner: Optional[BuyboxWinner] = None
    more_buying_choices: Optional[List[MoreBuyingChoices]] = None
    specifications: Optional[List[Specifications]] = None
    services: Optional[List[Services]] = None
    attributes: Optional[List[Attributes]] = None


class TotalPrice(BaseModel):
    symbol: Optional[str] = None
    value: Optional[float] = None
    currency: Optional[str] = None
    raw: Optional[str] = None


class Products(BaseModel):
    asin: Optional[str] = None
    title: Optional[str] = None
    link: Optional[str] = None
    price: Optional[Price] = None


class FrequentlyBoughtTogether(BaseModel):
    total_price: Optional[TotalPrice] = None
    products: Optional[List[Products]] = None


class AlsoViewed(BaseModel):
    title: Optional[str] = None
    link: Optional[str] = None
    image: Optional[str] = None
    rating: Optional[float] = None
    ratings_total: Optional[int] = None
    is_prime: Optional[bool] = None
    price: Optional[Price] = None


class Bundles(BaseModel):
    asin: Optional[str] = None
    title: Optional[str] = None
    link: Optional[str] = None
    image: Optional[str] = None
    rating: Optional[float] = None
    ratings_total: Optional[int] = None
    item_count: Optional[int] = None
    price: Optional[Price] = None
    rrp: Optional[Price] = None


class BundleContents(BaseModel):
    asin: Optional[str] = None
    title: Optional[str] = None
    link: Optional[str] = None
    image: Optional[str] = None
    rating: Optional[float] = None
    ratings_total: Optional[int] = None
    item_count: Optional[int] = None
    price: Optional[Price] = None


class SponsoredProducts(BaseModel):
    title: Optional[str] = None
    link: Optional[str] = None
    image: Optional[str] = None
    rating: Optional[float] = None
    ratings_total: Optional[int] = None
    is_prime: Optional[bool] = None
    price: Optional[Price] = None


class Items(BaseModel):
    asin: Optional[str] = None
    link: Optional[str] = None
    title: Optional[str] = None
    image: Optional[str] = None
    is_prime: Optional[bool] = None
    price: Optional[Price] = None
    ratings_total: Optional[int] = None


class ShopByLook(BaseModel):
    title: Optional[str] = None
    items: Optional[List[Items]] = None


class RainforestProductDetail(BaseModel):
    request_info: Optional[RequestInfo] = None
    request_metadata: Optional[RequestMetadata] = None
    request_parameters: Optional[RequestParameters] = None
    product: Optional[Product] = None
    frequently_bought_together: Optional[FrequentlyBoughtTogether] = None
    also_viewed: Optional[List[AlsoViewed]] = None
    bundles: Optional[List[Bundles]] = None
    bundle_contents: Optional[List[BundleContents]] = None
    sponsored_products: Optional[List[SponsoredProducts]] = None
    shop_by_look: Optional[ShopByLook] = None

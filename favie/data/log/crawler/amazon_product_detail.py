
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict, Union
from uuid import UUID

from pydantic import BaseModel, Field


class request_info(BaseModel):
    success: bool
    credits_used: int
    credits_used_this_request: int
    credits_remaining: int
    credits_create_time: str


class request_parameters(BaseModel):
    amazon_domain: str
    asin: str
    type: str


class request_metadata(BaseModel):
    created_at: str
    processed_at: str
    total_time_taken: int
    amazon_url: str


class sub_title(BaseModel):
    link: str
    text: str


class main_image(BaseModel):
    link: str


class images(BaseModel):
    link: str
    variant: str


class categories(BaseModel):
    name: str
    link: str
    category_id: str


class search_alias(BaseModel):
    title: str
    value: str


class price(BaseModel):
    symbol: str
    value: float
    currency: str
    raw: str


class protection_plans(BaseModel):
    asin: str
    title: str
    price: price


class maximum_order_quantity(BaseModel):
    value: int
    hard_maximum: bool


class availability(BaseModel):
    type: str
    raw: str
    dispatch_days: int


class secondary_buybox(BaseModel):
    offer_id: str
    caption: str
    availability: availability


class mixed_offers_from(BaseModel):
    pass


class condition(BaseModel):
    is_new: bool


class standard_delivery(BaseModel):
    date: List[str]
    text: str
    name: str


class fastest_delivery(BaseModel):
    pass


class third_party_seller(BaseModel):
    name: str
    link: str
    id: str


class fulfillment(BaseModel):
    type: str
    standard_delivery: standard_delivery
    fastest_delivery: fastest_delivery
    is_sold_by_amazon: bool
    is_fulfilled_by_amazon: bool
    is_fulfilled_by_third_party: bool
    is_sold_by_third_party: bool
    third_party_seller: third_party_seller


class buybox_winner(BaseModel):
    maximum_order_quantity: maximum_order_quantity
    secondary_buybox: secondary_buybox
    offer_id: str
    mixed_offers_count: int
    mixed_offers_from: mixed_offers_from
    is_prime: bool
    is_prime_exclusive_deal: bool
    is_amazon_fresh: bool
    condition: condition
    availability: availability
    fulfillment: fulfillment
    price: price
    shipping: str


class brand_store(BaseModel):
    id: str
    link: str


class newer_model(BaseModel):
    pass


class similar_to_consider(BaseModel):
    pass


class list(BaseModel):
    link: str
    asin: str
    title: str


class save_on_quality(BaseModel):
    title: str
    list: List[list]


class five_star(BaseModel):
    percentage: int
    count: int


class four_star(BaseModel):
    percentage: int
    count: int


class three_star(BaseModel):
    percentage: int
    count: int


class two_star(BaseModel):
    percentage: int
    count: int


class one_star(BaseModel):
    percentage: int
    count: int


class rating_breakdown(BaseModel):
    five_star: five_star
    four_star: four_star
    three_star: three_star
    two_star: two_star
    one_star: one_star


class energy_efficiency(BaseModel):
    pass


class amazons_choice(BaseModel):
    keywords: str


class flag(BaseModel):
    stock: int
    add_to_cart: int
    amazonfit: int
    coupon: int
    coupon_text: int
    aplus: int
    video: int


class spec(BaseModel):
    color_name: str


class AmazonProductDetail(BaseModel):
    request_info: request_info
    request_parameters: request_parameters
    request_metadata: request_metadata
    _id: str
    asin: str
    link: str
    type: str
    countryCode: str
    var_reviews: int
    var_ratings: int
    date: str
    title: str
    price: float
    brand: str
    sub_title: sub_title
    main_image: main_image
    images: List[images]
    images_count: int
    images_flat: str
    categories: List[categories]
    categories_flat: str
    search_alias: search_alias
    protection_plans: List[protection_plans]
    buybox_winner: buybox_winner
    marketplace_id: str
    videos: List[str]
    videos_count: int
    videos_flat: str
    feature_bullets: List[str]
    feature_bullets_count: int
    feature_bullets_flat: str
    attributes: List[str]
    specifications: List[str]
    specifications_flat: str
    top_reviews: List[str]
    brand_store: brand_store
    newer_model: newer_model
    similar_to_consider: similar_to_consider
    compare: List[str]
    frequently_bought_together: List[str]
    save_on_quality: save_on_quality
    similar_list: List[str]
    rating: int
    rating_breakdown: rating_breakdown
    ratings_total: int
    energy_efficiency: energy_efficiency
    keywords: str
    keywords_list: List[str]
    is_bundle: bool
    more_buying_choices: List[str]
    Q_A_num: int
    list_price: int
    save_price: int
    prime_price: int
    request_asin: str
    extra_saving: str
    ranks: List[str]
    deal: int
    first_list_date: int
    productDescription: str
    aplus_content: str
    aplus_table: List[str]
    also_viewed_asins: List[str]
    also_bought_asins: List[str]
    delivery: str
    title_tip_layer: str
    amazons_choice: amazons_choice
    flag: flag
    quantity: int
    parentAsin: str
    varient_num: int
    spec: spec

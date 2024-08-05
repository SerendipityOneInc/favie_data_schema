from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from favie_data_schema.favie.data.crawl_data.crawler.common import Source


class RequestInfo(BaseModel):
    success: Optional[bool] = None
    credits_used: Optional[int] = None
    credits_used_this_request: Optional[int] = None
    credits_remaining: Optional[int] = None
    credits_reset_at: Optional[str] = None


class RequestParameters(BaseModel):
    amazon_domain: Optional[str] = None
    asin: Optional[str] = None
    type: Optional[str] = None


class RequestMetadata(BaseModel):
    created_at: Optional[str] = None
    processed_at: Optional[str] = None
    total_time_taken: Optional[float] = None
    amazon_url: Optional[str] = None


class SubTitle(BaseModel):
    text: Optional[str] = None
    link: Optional[str] = None


class Product(BaseModel):
    title: Optional[str] = None
    link: Optional[str] = None
    sub_title: Optional[SubTitle] = None
    image: Optional[str] = None
    asin: Optional[str] = None


class FiveStar(BaseModel):
    percentage: Optional[int] = None
    count: Optional[int] = None


class FourStar(BaseModel):
    percentage: Optional[int] = None
    count: Optional[int] = None


class ThreeStar(BaseModel):
    percentage: Optional[int] = None
    count: Optional[int] = None


class TwoStar(BaseModel):
    percentage: Optional[int] = None
    count: Optional[int] = None


class OneStar(BaseModel):
    percentage: Optional[int] = None
    count: Optional[int] = None


class RatingBreakdown(BaseModel):
    five_star: Optional[FiveStar] = None
    four_star: Optional[FourStar] = None
    three_star: Optional[ThreeStar] = None
    two_star: Optional[TwoStar] = None
    one_star: Optional[OneStar] = None


class Summary(BaseModel):
    rating: Optional[float] = None
    ratings_total: Optional[int] = None
    ratings_total_filtered: Optional[int] = None
    reviews_total_filtered: Optional[int] = None
    reviews_total: Optional[int] = None
    rating_breakdown: Optional[RatingBreakdown] = None


class Date(BaseModel):
    raw: Optional[str] = None
    utc: Optional[str] = None


class Profile(BaseModel):
    name: Optional[str] = None
    link: Optional[str] = None
    id: Optional[str] = None
    image: Optional[str] = None


class Reviews(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    body: Optional[str] = None
    asin: Optional[str] = None
    body_html: Optional[str] = None
    link: Optional[str] = None
    rating: Optional[int] = None
    date: Optional[Date] = None
    profile: Optional[Profile] = None
    vine_program: Optional[bool] = None
    verified_purchase: Optional[bool] = None
    review_country: Optional[str] = None
    is_global_review: Optional[bool] = None
    position: Optional[int] = None
    helpful_votes: Optional[int] = None


class Pagination(BaseModel):
    ratings_total_filtered: Optional[int] = None
    reviews_total_filtered: Optional[int] = None
    reviews_total: Optional[int] = None
    total_results: Optional[int] = None
    total_pages: Optional[int] = None
    message: Optional[str] = None
    current_page: Optional[int] = None
    start: Optional[int] = None
    end: Optional[int] = None


class RainforestProductReview(BaseModel):
    request_info: Optional[RequestInfo] = None
    request_parameters: Optional[RequestParameters] = None
    request_metadata: Optional[RequestMetadata] = None
    product: Optional[Product] = None
    summary: Optional[Summary] = None
    reviews: Optional[List[Reviews]] = None
    pagination: Optional[Pagination] = None


class FavieSpiderProductReviewData(BaseModel):
    id: str = uuid.uuid1().hex  # UUID1
    url: str  # URL
    host: str  # 商品所在网站的域名，比如：www.amazon.com
    product_id: Optional[str] = None  # 商品ID，比如：Amazon为ASIN: B0CBLKS51N
    product_title: Optional[str] = None  # 商品Title
    parser_name: Optional[str] = None  # used for spider
    source: Optional[Source] = 0  # 数据来源
    raw_result: Optional[
        str
    ] = None  # 原始抓取结果，如果为Rainforest则为API则为Response的json结果，如果为自研爬虫则为原始html
    crawl_result: Optional[
        RainforestProductReview
    ] = None  # 商品review解析结果，存储为JSON格式，遵循RainForest的数据模型
    create_time: Optional[datetime] = datetime.now()  # 爬虫写入时间
    update_time: Optional[datetime] = datetime.now()  # 数据更新时间
    task_id: Optional[int] = None  # 爬虫任务ID

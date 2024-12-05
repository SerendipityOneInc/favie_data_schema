from typing import Optional

from pydantic import BaseModel

from favie_data_schema.favie.data.crawl_data.crawler.crawler_result import CrawlerResult
from favie_data_schema.favie.data.crawl_data.crawler.favie_spider_data import ContentType
from favie_data_schema.favie.data.crawl_data.crawler.stark_product_list import StarkProductList
from favie_data_schema.favie.data.crawl_data.crawler.stark_webpage import WebpageItem
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_detail import RainforestProductDetail
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_review import RainforestProductReview


class StarkMessage(BaseModel):
    url: Optional[str] = None
    host: Optional[str] = None
    product_id: Optional[str] = None
    product_title: Optional[str] = None
    content_type: Optional[ContentType] = ContentType.OTHER  # used for webpage spider，网页专用
    source: Optional[int] = None
    parser_name: Optional[str] = None
    spider: Optional[str] = None  # 爬虫名称, 由不同的content_type交给不同的爬虫处理解析,网页专用
    raw_result: Optional[str] = None
    create_time: Optional[str] = None
    update_time: Optional[str] = None
    mission: Optional[str] = None
    version: Optional[str] = None
    app_key: Optional[str] = None


class StarkProductDetailMessage(StarkMessage):
    crawl_result: Optional[RainforestProductDetail] = None


class StarkProductReviewMessage(StarkMessage):
    crawl_result: Optional[RainforestProductReview] = None


class StarkProductListMessage(StarkMessage):
    crawl_result: Optional[StarkProductList] = None


class StarkWebpageMessage(StarkMessage):
    crawl_result: Optional[CrawlerResult] = None


class StarkNewWebpageMessage(StarkMessage):
    crawl_result: Optional[WebpageItem] = None

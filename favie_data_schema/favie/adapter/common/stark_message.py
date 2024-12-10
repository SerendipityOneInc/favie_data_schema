from typing import Optional

from pydantic import BaseModel

from favie_data_schema.favie.data.crawl_data.crawler.crawler_result import CrawlerResult
from favie_data_schema.favie.data.crawl_data.crawler.favie_spider_data import ContentType
from favie_data_schema.favie.data.crawl_data.crawler.stark_product_list import StarkProductList
from favie_data_schema.favie.data.crawl_data.crawler.stark_webpage import WebpageItem
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_detail import RainforestProductDetail
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_review import RainforestProductReview


class StarkMessage(BaseModel):
    url: Optional[str] = None  # url 和 host 至少要有一个
    host: Optional[str] = None  # url 和 host 至少要有一个
    product_id: Optional[str] = None  # 商品库请求爬取的商品ID，非必填
    product_title: Optional[str] = None  # 商品标题，非必填
    content_type: Optional[ContentType] = ContentType.OTHER  # used for webpage spider，网页专用,非必填
    source: Optional[int] = None  # 数据来源，必填
    parser_name: Optional[str] = None  # parser名称，必填
    spider: Optional[str] = None  # 爬虫名称, 由不同的content_type交给不同的爬虫处理解析,网页专用，非必填
    raw_result: Optional[str] = None  # 原始数据，非必填
    create_time: Optional[str] = None  # 爬取时间，必填
    update_time: Optional[str] = None  # 更新时间，非必填
    mission: Optional[str] = None  # 爬虫任务名称，非必填
    version: Optional[str] = None  # 版本号，非必填，建议填写
    app_key: Optional[str] = None  # 外部数据网关分配的app_key，非必填


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

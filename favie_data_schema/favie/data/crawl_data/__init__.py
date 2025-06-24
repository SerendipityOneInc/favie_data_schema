from .crawler.crawler_result import (
    CrawlerRequestInfo,
    CrawlerResult,
    ParsedWebPageContent,
    SubtitleContent,
    WebPageContent,
)
from .crawler.favie_spider_data import ContentType, FavieSpiderData
from .rainforest.rainforest_product_detail import RainforestProductDetail

# 定义模块的公开接口
__all__ = [
    # crawler.crawler_result 模块的类
    "CrawlerRequestInfo",
    "CrawlerResult",
    "ParsedWebPageContent",
    "SubtitleContent",
    "WebPageContent",
    # crawler.favie_spider_data 模块的类
    "ContentType",
    "FavieSpiderData",
    # rainforest.rainforest_product_detail 模块的类
    "RainforestProductDetail",
]

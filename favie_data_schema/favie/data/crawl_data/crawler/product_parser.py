
from enum import Enum

from pydantic import BaseModel

from favie_data_schema.favie.data.crawl_data.crawler.common import Source


class ContentType(str, Enum):
    """
    Content type
    """

    PRODUCT_DETAIL = "product_detail"
    PRODUCT_LIST = "product_list"
    PRODUCT_REVIEW = "product_review"

    
class ParserType(str, Enum):
    JSON = "json"
    HTML = "html"


class CrawledOutput(BaseModel):
    raw_data: str
    parser_type: ParserType
    content_type: ContentType
    parser_name: str
    source: Source
    original_url: str
    asin: str
    create_time: str
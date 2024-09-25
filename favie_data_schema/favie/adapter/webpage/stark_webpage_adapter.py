from datetime import datetime
import logging
from favie_data_common.common.common_utils import CommonUtils
from favie_data_schema.favie.adapter.common.spark_message import StarkWebpageMessage
from favie_data_schema.favie.adapter.webpage.common.favie_webpage_adapter import FavieWebpageAdapter
from favie_data_schema.favie.data.crawl_data.crawler.crawler_result import ParsedWebPageContent
from favie_data_schema.favie.data.interface.webpage.favie_webpage import FavieWebpage,MetaInfo,ImageData
from favie_data_schema.favie.adapter.tools.data_mock_read import read_object
from urllib.parse import urlparse


class FavieWebpageAdapter(FavieWebpageAdapter):
    @staticmethod
    def stark_webpage_to_favie_webpage(webpage_message: StarkWebpageMessage) -> FavieWebpage:
        if not FavieWebpageAdapter._message_check(webpage_message):
            return None
        
        webpage = FavieWebpage()
        webpage.md5_id = CommonUtils.md5_hash(webpage_message.crawl_result.original_url)
        webpage.url = webpage_message.crawl_result.original_url
        webpage.favicon = None
        webpage.language = webpage_message.crawl_result.webpage.parsed_webpage_content.language
        webpage.title = webpage_message.crawl_result.webpage.parsed_webpage_content.title
        webpage.description = None
        webpage.author = webpage_message.crawl_result.webpage.parsed_webpage_content.author
        webpage.keywords = None
        webpage.robots = None
        webpage.content = webpage_message.crawl_result.webpage.parsed_webpage_content.text
        webpage.content_type = webpage_message.content_type
        webpage.excerpt = webpage_message.crawl_result.webpage.parsed_webpage_content.excerpt
        webpage.comments = None
        webpage.subtitles = None
        webpage.images = FavieWebpageAdapter.__get_images(webpage_message.crawl_result.webpage.parsed_webpage_content)
        webpage.videos = None
        webpage.references = None
        webpage.json_lds = None
        webpage.open_graphs = None
        webpage.twitter_cards = None
        webpage.page_type = webpage_message.crawl_result.webpage.parsed_webpage_content.pagetype
        webpage.f_meta = MetaInfo(
            source_type = str(webpage_message.source),
            parser_name = webpage_message.spider,
            parses_at = FavieWebpageAdapter.get_parse_time(webpage_message),
        )
        return webpage
    
    @staticmethod
    def __get_images(webpage_content: ParsedWebPageContent) -> FavieWebpage:
        return [ImageData(url = image) for image in [webpage_content.image]] if webpage_content.image else None

    @staticmethod
    def get_parse_time(message: StarkWebpageMessage):    
        try:
            return str(int(CommonUtils.datetime_string_to_timestamp(message.update_time)))
        except Exception as e:
            logging.exception("get_parse_time error: %s", message.model_dump_json(exclude_none=True))
            return str(int(datetime.now().timestamp())) 
        
if __name__ == "__main__":
    webpage_message = read_object("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/stark_webpage_message.json", StarkWebpageMessage)
    webpage = FavieWebpageAdapter.stark_webpage_to_favie_webpage(webpage_message)
    if webpage:
        print(webpage.model_dump_json(exclude_none=True))
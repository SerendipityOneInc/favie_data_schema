from typing import List

from favie_data_common.common.common_utils import CommonUtils

from favie_data_schema.favie.adapter.common.deserialize_utils import DeserializeUtils
from favie_data_schema.favie.adapter.common.stark_message import StarkNewWebpageMessage, StarkWebpageMessage
from favie_data_schema.favie.adapter.common.stark_message_utils import StarkMessageUtils
from favie_data_schema.favie.adapter.tools.data_mock_read import read_file
from favie_data_schema.favie.adapter.webpage.common.favie_webpage_adapter import FavieWebpageAdapter
from favie_data_schema.favie.data.crawl_data.crawler.crawler_result import ParsedWebPageContent
from favie_data_schema.favie.data.crawl_data.crawler.stark_webpage import WebpageImage
from favie_data_schema.favie.data.interface.common.favie_enum import MessageDataType
from favie_data_schema.favie.data.interface.webpage.favie_webpage import FavieWebpage, ImageData, MetaInfo


class StarkWebpageAdapter(FavieWebpageAdapter):
    @staticmethod
    def stark_webpage_to_favie_webpage(webpage_message: StarkWebpageMessage | StarkNewWebpageMessage) -> FavieWebpage:
        if webpage_message.parser_name == "InstagramPostListParser":
            return StarkWebpageAdapter.convert_webpage_new(webpage_message)
        else:
            return StarkWebpageAdapter.convert_webpage(webpage_message)

    @staticmethod
    def convert_webpage(webpage_message: StarkWebpageMessage) -> FavieWebpage:
        if not StarkWebpageAdapter._message_check(webpage_message):
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
        webpage.images = StarkWebpageAdapter.__get_images(webpage_message.crawl_result.webpage.parsed_webpage_content)
        webpage.videos = None
        webpage.references = None
        webpage.json_lds = None
        webpage.open_graphs = None
        webpage.twitter_cards = None
        webpage.page_type = webpage_message.crawl_result.webpage.parsed_webpage_content.pagetype
        webpage.f_meta = MetaInfo(
            source_type=str(webpage_message.source),
            parser_name=webpage_message.spider,
            parses_at=StarkMessageUtils.get_parse_time(webpage_message),
            data_type=str(MessageDataType.WEBPAGE_CONTENT_CRAWLER.value),
        )
        return webpage

    @staticmethod
    def convert_webpage_new(webpage_message: StarkNewWebpageMessage) -> FavieWebpage:
        if not StarkWebpageAdapter._message_check_new(webpage_message):
            return None
        webpage = FavieWebpage()
        webpage.md5_id = CommonUtils.md5_hash(webpage_message.crawl_result.url)
        webpage.url = webpage_message.crawl_result.url
        webpage.favicon = None
        webpage.language = None
        webpage.title = webpage_message.crawl_result.title
        webpage.description = webpage_message.crawl_result.description
        webpage.author = webpage_message.crawl_result.author
        webpage.keywords = webpage_message.crawl_result.tags
        webpage.robots = None
        webpage.content = None
        webpage.content_type = webpage_message.content_type
        webpage.excerpt = None
        webpage.comments = None
        webpage.subtitles = None
        webpage.images = StarkWebpageAdapter.__get_images_new(webpage_message.crawl_result.images)
        webpage.videos = None
        webpage.references = None
        webpage.json_lds = None
        webpage.open_graphs = None
        webpage.twitter_cards = None
        webpage.page_type = webpage_message.crawl_result.page_type
        webpage.f_meta = MetaInfo(
            source_type=str(webpage_message.source),
            parser_name=webpage_message.spider,
            parses_at=StarkMessageUtils.get_parse_time(webpage_message),
            data_type=str(MessageDataType.WEBPAGE_CONTENT_CRAWLER.value),
        )
        return webpage

    @staticmethod
    def __get_images(webpage_content: ParsedWebPageContent) -> list[ImageData] | None:
        return [ImageData(url=image) for image in [webpage_content.image]] if webpage_content.image else None

    @staticmethod
    def __get_images_new(images: List[WebpageImage]):
        return (
            [
                ImageData(url=image.url, desc=image.desc, width=image.width, height=image.height)
                for image in images
                if image
            ]
            if images
            else None
        )


if __name__ == "__main__":
    webpage_message_str = read_file(
        "/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/stark_webpage_message_new.json"
    )
    webpage_message = DeserializeUtils.deserialize_webpage_message(webpage_message_str)
    webpage = StarkWebpageAdapter.stark_webpage_to_favie_webpage(webpage_message)
    if webpage:
        print(webpage.model_dump_json(exclude_none=True))

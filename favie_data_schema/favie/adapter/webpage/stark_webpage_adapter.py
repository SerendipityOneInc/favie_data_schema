from typing import List

from favie_data_common.common.common_utils import CommonUtils
from simhash import Simhash

from favie_data_schema.favie.adapter.common.deserialize_utils import DeserializeUtils
from favie_data_schema.favie.adapter.common.stark_message import StarkNewWebpageMessage, StarkWebpageMessage
from favie_data_schema.favie.adapter.common.stark_message_utils import StarkMessageUtils
from favie_data_schema.favie.adapter.tools.data_mock_read import read_file
from favie_data_schema.favie.adapter.webpage.common.favie_webpage_adapter import FavieWebpageAdapter
from favie_data_schema.favie.data.crawl_data.crawler.crawler_result import ParsedWebPageContent
from favie_data_schema.favie.data.crawl_data.crawler.stark_webpage import (
    WebpageImage,
    WebpageProduct,
    WebpageReference,
    WebpageVideo,
)
from favie_data_schema.favie.data.interface.common.favie_enum import FavieDataStatus, MessageDataType
from favie_data_schema.favie.data.interface.webpage.favie_webpage import (
    FavieWebpage,
    ImageData,
    MetaInfo,
    ProductData,
    ReferenceData,
    VideoData,
    WebpageAuthor,
    WebpageComment,
    WebpageReviewSummary,
    WebpageSubtitleChunk,
)


class StarkWebpageAdapter(FavieWebpageAdapter):
    @staticmethod
    def stark_webpage_to_favie_webpage(webpage_message) -> FavieWebpage:
        if isinstance(webpage_message, StarkNewWebpageMessage):
            return StarkWebpageAdapter.convert_webpage_new(webpage_message)
        elif isinstance(webpage_message, StarkWebpageMessage):
            return StarkWebpageAdapter.convert_webpage(webpage_message)
        else:
            return None

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
        content = webpage_message.crawl_result.webpage.parsed_webpage_content.text
        webpage.content = content
        webpage.f_fingerprint = Simhash(content).value if content else None
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
            app_key=webpage_message.app_key,
        )
        webpage.f_status = str(FavieDataStatus.NORMAL.value)
        return webpage

    @staticmethod
    def convert_webpage_new(webpage_message: StarkNewWebpageMessage) -> FavieWebpage:
        if not StarkWebpageAdapter._message_check_new(webpage_message):
            return None
        webpage = FavieWebpage()
        webpage.md5_id = CommonUtils.md5_hash(webpage_message.crawl_result.url)
        webpage.url = webpage_message.crawl_result.url
        webpage.favicon = webpage_message.crawl_result.favicon
        webpage.language = webpage_message.crawl_result.language
        webpage.title = webpage_message.crawl_result.title
        webpage.description = webpage_message.crawl_result.description
        webpage.author = webpage_message.crawl_result.author
        webpage.author_v1 = StarkWebpageAdapter.__get_author(webpage_message)
        webpage.keywords = webpage_message.crawl_result.keywords
        webpage.robots = webpage_message.crawl_result.robots
        content = webpage_message.crawl_result.content
        webpage.content = content
        webpage.f_fingerprint = Simhash(content).value if content else None
        webpage.content_type = webpage_message.content_type
        webpage.excerpt = webpage_message.crawl_result.excerpt
        webpage.comments = webpage_message.crawl_result.comments
        webpage.subtitles = webpage_message.crawl_result.subtitles
        webpage.review_summary = StarkWebpageAdapter.__get_review_summary(webpage_message)
        webpage.images = StarkWebpageAdapter.__get_images_new(webpage_message.crawl_result.images)
        webpage.videos = StarkWebpageAdapter.__get_videos_new(webpage_message.crawl_result.videos)
        webpage.references = StarkWebpageAdapter.__get_references_new(webpage_message.crawl_result.references)
        webpage.json_lds = webpage_message.crawl_result.json_lds
        webpage.open_graphs = webpage_message.crawl_result.open_graphs
        webpage.twitter_cards = webpage_message.crawl_result.twitter_cards
        webpage.products = StarkWebpageAdapter.__get_products_new(webpage_message.crawl_result.products)
        webpage.ext_data = webpage_message.crawl_result.ext_data
        webpage.page_type = webpage_message.crawl_result.page_type
        webpage.comments_v1 = StarkWebpageAdapter.__get_comments(webpage_message)
        webpage.subtitles_v1 = StarkWebpageAdapter.__get_subtitles(webpage_message)
        webpage.f_meta = MetaInfo(
            source_type=str(webpage_message.source),
            parser_name=webpage_message.spider,
            parses_at=StarkMessageUtils.get_parse_time(webpage_message),
            data_type=str(MessageDataType.WEBPAGE_CONTENT_CRAWLER.value),
            app_key=webpage_message.app_key,
        )
        webpage.f_status = str(FavieDataStatus.NORMAL.value)
        webpage.webpage_create_time = webpage_message.crawl_result.create_time
        return webpage

    @staticmethod
    def __get_comments(webpage_message: StarkNewWebpageMessage) -> list[str] | None:
        return (
            [
                WebpageComment(**(comment.model_dump()))
                for comment in webpage_message.crawl_result.comments_v1
                if comment
            ]
            if webpage_message.crawl_result.comments_v1
            else None
        )

    @staticmethod
    def __get_subtitles(webpage_message: StarkNewWebpageMessage) -> list[str] | None:
        return (
            [
                WebpageSubtitleChunk(**(subtitle.model_dump()))
                for subtitle in webpage_message.crawl_result.subtitles_v1
                if subtitle
            ]
            if webpage_message.crawl_result.subtitles_v1
            else None
        )

    @staticmethod
    def __get_review_summary(webpage_message: StarkNewWebpageMessage) -> WebpageReviewSummary:
        return (
            WebpageReviewSummary(
                upvotes_count=webpage_message.crawl_result.upvotes_count,
                downvotes_count=webpage_message.crawl_result.downvotes_count,
                views_count=webpage_message.crawl_result.views_count,
                comments_total=webpage_message.crawl_result.comments_total,
            )
            if CommonUtils.any_not_none(
                webpage_message.crawl_result.upvotes_count,
                webpage_message.crawl_result.downvotes_count,
                webpage_message.crawl_result.views_count,
                webpage_message.crawl_result.comments_total,
            )
            else None
        )

    @staticmethod
    def __get_author(webpage_message: StarkNewWebpageMessage) -> WebpageAuthor:
        auther_v1 = webpage_message.crawl_result.author_v1
        return WebpageAuthor(**auther_v1.model_dump()) if auther_v1 else None

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

    @staticmethod
    def __get_videos_new(videos: List[WebpageVideo]):
        return [VideoData(url=video.url, desc=video.desc) for video in videos if video] if videos else None

    @staticmethod
    def __get_products_new(products: List[WebpageProduct]):
        return (
            [
                ProductData(
                    url=product.url,
                    title=product.title,
                    description=product.description,
                    price=product.price,
                    images=StarkWebpageAdapter.__get_images_new(product.images),
                    videos=StarkWebpageAdapter.__get_videos_new(product.videos),
                )
                for product in products
                if product
            ]
            if products
            else None
        )

    @staticmethod
    def __get_references_new(references: List[WebpageReference]):
        return (
            [ReferenceData(url=reference.url, desc=reference.desc) for reference in references if reference]
            if references
            else None
        )


if __name__ == "__main__":
    webpage_message_str = read_file("./favie_data_schema/favie/resources/stark_webpage_message_new.json")
    webpage_message = DeserializeUtils.deserialize_webpage_message(webpage_message_str)
    webpage = StarkWebpageAdapter.stark_webpage_to_favie_webpage(webpage_message)
    if webpage:
        print(webpage.model_dump_json(exclude_none=True))

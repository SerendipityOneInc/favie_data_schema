from favie_data_schema.favie.adapter.webpage.common.favie_webpage_adapter import FavieWebpageAdapter
from favie_data_schema.favie.data.crawl_data.crawler.crawler_result import ParsedWebPageContent
from favie_data_schema.favie.data.crawl_data.crawler.favie_spider_data import FavieSpiderData
from favie_data_schema.favie.data.interface.webpage.favie_webpage import FavieWebpage,MetaInfo,ImageData,VideoData,ReferenceData
from favie_data_schema.favie.adapter.tools.data_mock_read import read_mock_data
from urllib.parse import urlparse
class CrawlbaseFavieWebpageAdapter(FavieWebpageAdapter):
    @staticmethod
    def convert_to_favie_webpage(webpage_message: FavieSpiderData) -> FavieWebpage:
        if not CrawlbaseFavieWebpageAdapter._message_check(webpage_message):
            return None
        
        webpage = FavieWebpage()
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
        webpage.images = CrawlbaseFavieWebpageAdapter.__get_images(webpage_message.crawl_result.webpage.parsed_webpage_content)
        webpage.videos = None
        webpage.references = None
        webpage.json_lds = None
        webpage.open_graphs = None
        webpage.twitter_cards = None
        webpage.page_type = webpage_message.crawl_result.webpage.parsed_webpage_content.pagetype
        webpage.f_meta = MetaInfo(
            source_type=webpage_message.source,
            parser_name=webpage_message.spider
        )
        return webpage
    
    @staticmethod
    def __get_images(webpage_content: ParsedWebPageContent) -> FavieWebpage:
        return [ImageData(url = image) for image in [webpage_content.image]] if webpage_content.image else None


if __name__ == "__main__":
    webpage_message = read_mock_data("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/webpage_message.json", FavieSpiderData)
    webpage = CrawlbaseFavieWebpageAdapter.convert_to_favie_webpage(webpage_message)
    if webpage:
        print(webpage.model_dump_json(exclude_none=True))
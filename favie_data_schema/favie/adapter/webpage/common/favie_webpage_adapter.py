from favie_data_schema.favie.data.crawl_data.crawler.favie_spider_data import FavieSpiderData
from favie_data_schema.favie.data.interface.webpage.favie_webpage import FavieWebpage
from favie_data_schema.favie.adapter.common.common_utils import CommonUtils

class FavieWebpageAdapter():
    @staticmethod
    def convert_to_favie_webpage(webpage_message: FavieSpiderData) -> FavieWebpage:
        # TODO: implement
        pass
    
    @staticmethod
    def _message_check(webpage_message: FavieSpiderData) -> bool:
        if webpage_message is None:
            return False
        
        if webpage_message.crawl_result is None:
            return False
        
        if webpage_message.crawl_result.original_status != 200 and webpage_message.crawl_result.pc_status != 200:
            return False
        
        if webpage_message.crawl_result.original_url is None:
            return False
        
        if webpage_message.crawl_result.webpage is None:
            return False
        
        if webpage_message.crawl_result.webpage.parsed_webpage_content is None:
            return False
                
        return True

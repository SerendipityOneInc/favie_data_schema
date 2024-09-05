from favie_data_schema.favie.adapter.product.common.favie_product_adapter import FavieProductDetailAdapter
from favie_data_schema.favie.adapter.product.list_adapter.amazon_list_result_adapter import AmazoneListResultAdapter
from favie_data_schema.favie.data.interface.product.favie_product_detail import *
from favie_data_schema.favie.data.crawl_data.crawler.list_crawler_message import ListCrawlerMessage
from favie_data_schema.favie.adapter.tools.data_mock_read import read_file
from favie_data_schema.favie.data.crawl_data.crawler.common import Source
from favie_data_schema.favie.data.crawl_data.crawler.amazon_list_crawler_result import AmazonListCrawlResult
from datetime import datetime
import logging,json

from favie_data_schema.favie.data.interface.product.favie_product_detail import FavieProductDetail

adapter_config = {
    "RainforestStandardV2ProductListParser":AmazoneListResultAdapter,
    "RainforestDealsProductListParser":AmazoneListResultAdapter
}

class ListCrawlerAdapter(FavieProductDetailAdapter):
    @staticmethod
    def convert_to_favie_product(message: ListCrawlerMessage) -> FavieProductDetail:
        if message is None or message.crawl_result is None:
            return None  
        adapter = adapter_config.get(message.parser_name)
        if adapter is None:
            logging.error(f"ListCrawlerAdapter can not find adapter for {message.parser_name}")
            return None
              
        favie_product = adapter.convert_to_favie_product(message.crawl_result)
        if favie_product is None:
            return None
        
        favie_product.f_meta = ListCrawlerAdapter.get_meta_info(message)
        return favie_product
    
    @staticmethod
    def get_meta_info(message: ListCrawlerMessage):
        return MetaInfo(
            source_type = Source.SPIDER,
            parser_name = message.parser_name,
            parses_at = message.create_time 
        )
            
def main():
    messate = read_file("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/amazon_list_message.json")
    list_message = ListCrawlerMessage.deseriallize(messate,AmazonListCrawlResult)
    favie_product: FavieProductDetail = ListCrawlerAdapter.convert_to_favie_product(list_message)
    print(favie_product.model_dump_json(exclude_none = True) if favie_product else None)

if __name__ == "__main__":
    main()
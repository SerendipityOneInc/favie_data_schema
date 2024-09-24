from datetime import datetime
from favie_data_schema.favie.adapter.product.common.favie_product_adapter import FavieProductDetailAdapter
from favie_data_schema.favie.adapter.product.list_adapter.amazon_list_result_adapter import AmazoneListResultAdapter
from favie_data_schema.favie.data.interface.product.favie_product import *
from favie_data_schema.favie.adapter.product.common.list_crawler_message import ListCrawlerMessage
from favie_data_schema.favie.adapter.tools.data_mock_read import read_file
from favie_data_schema.favie.data.crawl_data.crawler.common import Source
from favie_data_schema.favie.data.crawl_data.crawler.stark_product_list import AmazonListCrawlResult
from favie_data_schema.favie.data.interface.product.product_enum import DataType
from favie_data_common.common.common_utils import CommonUtils
import logging

adapter_config = {
    "RainforestStandardV2ProductListParser":AmazoneListResultAdapter,
    "RainforestDealsProductListParser":AmazoneListResultAdapter
}

class ListCrawlerAdapter(FavieProductDetailAdapter):
    @staticmethod
    def crawl_detail_to_product_detail(message: ListCrawlerMessage) -> FavieProductDetail:
        if message is None or message.crawl_result is None:
            return None  
        parse_time = ListCrawlerAdapter.get_parse_time(message)
        adapter = adapter_config.get(message.parser_name,AmazoneListResultAdapter)
        favie_product = adapter.list_crawl_result_to_product_detail(message.crawl_result,parse_time)
        if favie_product is None:
            return None
        
        favie_product.f_meta = MetaInfo(
            source_type = Source.SPIDER,
            parser_name = message.parser_name,
            data_type = str(DataType.PRODUCT_LIST.value),
            parses_at = parse_time
        )
        
        return favie_product
        
    @staticmethod
    def get_parse_time(message: ListCrawlerMessage):    
        try:
            return str(int(CommonUtils.datetime_string_to_timestamp(message.update_time)))
        except Exception as e:
            logging.exception("get_parse_time error: %s", message.model_dump_json(exclude_none=True))
            return str(int(datetime.now().timestamp())) 
            
def main():
    messate = read_file("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/amazon_list_message.json")
    list_message = ListCrawlerMessage.deserialize(messate,AmazonListCrawlResult)
    favie_product: FavieProductDetail = ListCrawlerAdapter.crawl_detail_to_product_detail(list_message)
    print(favie_product.model_dump_json(exclude_none = True) if favie_product else None)

if __name__ == "__main__":
    main()
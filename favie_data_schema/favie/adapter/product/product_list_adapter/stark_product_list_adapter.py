from favie_data_schema.favie.adapter.product.common.currency import CurrencyConverter
from favie_data_schema.favie.adapter.product.common.favie_product_adapter import FavieProductDetailAdapter
from favie_data_schema.favie.adapter.common.spark_enum import SparkProductDataType
from favie_data_schema.favie.adapter.common.spark_message import StarkProductListMessage
from favie_data_schema.favie.data.interface.product.favie_product import *
from favie_data_schema.favie.data.crawl_data.crawler.stark_product_list import StarkProductList,Price as AmazonPrice
from favie_data_common.common.common_utils import CommonUtils
from favie_data_schema.favie.adapter.tools.data_mock_read import read_object
from favie_data_schema.favie.data.crawl_data.crawler.common import Source
from datetime import datetime
import logging

class StarkProductListAdapter(FavieProductDetailAdapter):
    @staticmethod
    def stark_list_to_favie_details(message: StarkProductListMessage) -> Optional[List[FavieProductDetail]]:
        if message is None or message.crawl_result is None:
            return None 

        stark_product_list = message.crawl_result.product_list
        if CommonUtils.list_len(stark_product_list) == 0:
            return None
        
        favie_product_list = []
        for stark_product in stark_product_list:
            favie_product = FavieProductDetail()
            parse_time = StarkProductListAdapter.get_parse_time(message)
            favie_product.sku_id = stark_product.asin
            favie_product.site = "amazon.com"
            favie_product.title = stark_product.title
            favie_product.link = stark_product.link
            favie_product.price = StarkProductListAdapter.get_price(stark_product,parse_time)
            favie_product.rrp = StarkProductListAdapter.get_rrp(stark_product,parse_time)
            favie_product.images = StarkProductListAdapter.get_images(stark_product)
            favie_product.review_summary = StarkProductListAdapter.get_review_summary(stark_product)
            favie_product.f_meta = MetaInfo(
                source_type = Source.SPIDER,
                parser_name = message.parser_name,
                data_type = str(SparkProductDataType.PRODUCT_LIST.value),
                parses_at = parse_time
            )
            favie_product_list.append(favie_product)
        return favie_product_list if CommonUtils.list_len(favie_product_list) > 0 else None
    
    @staticmethod
    def get_parse_time(message: StarkProductListMessage):    
        try:
            return str(int(CommonUtils.datetime_string_to_timestamp(message.update_time)))
        except Exception as e:
            logging.exception("get_parse_time error: %s", message.model_dump_json(exclude_none=True))
            return str(int(datetime.now().timestamp())) 
    
        
    @staticmethod
    def get_review_summary(crawl_result: StarkProductList) -> ReviewSummary:
        return ReviewSummary(
            rating = crawl_result.rating,
            ratings_total= crawl_result.ratings_total
        )
        
    @staticmethod
    def get_images(crawl_result: StarkProductList) -> Images:
        return Images(main_image=crawl_result.image) if crawl_result.image is not None else None
    
    @staticmethod
    def get_price(crawl_result: StarkProductList,parse_time:str) -> Price:
        amazon_price = crawl_result.price if crawl_result.price is not None else None
        if amazon_price is None and CommonUtils.list_len(crawl_result.prices) > 0:
            amazon_price = next(filter(lambda price  : price.is_primary,crawl_result.prices))
        return StarkProductListAdapter.convert_price(amazon_price,parse_time)

    @staticmethod
    def get_rrp(crawl_result: StarkProductList,parse_time:str) -> Price:
        if CommonUtils.list_len(crawl_result.prices) > 0:
            amazon_price = next(filter(lambda price  : price.is_rrp,crawl_result.prices))
            return StarkProductListAdapter.convert_price(amazon_price,parse_time)
        
    @staticmethod
    def convert_price(amazon_price : AmazonPrice,parse_time:str)->Price:
        if amazon_price is None:
            return None
        currency_converter = CurrencyConverter(amazon_price.currency,amazon_price.value)
        price = Price(
                currency=currency_converter.get_currency_code(),
                value = currency_converter.get_subunit_value(),
                updates_at=parse_time
            )
        return price if CommonUtils.all_not_none(price.currency,price.value) else None
    
if __name__ == "__main__":
    stark_product_list_message = read_object("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/stark_product_list_message.json", StarkProductListMessage)
    adapter = StarkProductListAdapter()
    product_list = adapter.stark_list_to_favie_details(stark_product_list_message)
    if product_list:
        for product in product_list:
            print(product.model_dump_json(exclude_none=True))
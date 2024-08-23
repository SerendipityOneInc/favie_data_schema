from favie_data_schema.favie.adapter.common.currency import CurrencyConverter
from favie_data_schema.favie.adapter.common.favie_adapter import FavieProductAdapter
from favie_data_schema.favie.adapter.common.favie_product_utils import FavieProductUtils
from favie_data_schema.favie.data.interface.product.favie_product_detail import *
from favie_data_schema.favie.data.crawl_data.crawler.amazon_list_message import AmazonListMessage,CrawlResult,Price as AmazonPrice
from favie_data_schema.favie.adapter.common.common_utils import CommonUtils
from favie_data_schema.favie.adapter.data_mock.data_mock_read import read_mock_data
from favie_data_schema.favie.data.crawl_data.crawler.common import Source

from datetime import datetime
import logging

from favie_data_schema.favie.data.interface.product.favie_product_detail import FavieProductDetail

class AmazonListAdapter(FavieProductAdapter):
    @staticmethod
    def convert_to_favie_product(amazon_message: AmazonListMessage) -> FavieProductDetail:
        if amazon_message is None or amazon_message.crawl_result is None:
            return None        
        favie_product = FavieProductDetail()
        favie_product.sku_id = amazon_message.crawl_result.asin
        favie_product.site = "amazon.com"
        favie_product.title = amazon_message.crawl_result.title
        favie_product.link = amazon_message.crawl_result.link
        favie_product.price = AmazonListAdapter.get_price(amazon_message.crawl_result)
        favie_product.rrp = AmazonListAdapter.get_rrp(amazon_message.crawl_result)
        favie_product.images = AmazonListAdapter.get_images(amazon_message.crawl_result)
        favie_product.standard_attributes = AmazonListAdapter.get_standard_attributes(amazon_message.crawl_result)
        favie_product.review_summary = AmazonListAdapter.get_review_summary(amazon_message.crawl_result)
        favie_product.f_meta = AmazonListAdapter.get_meta_info(amazon_message)
        return favie_product
    
    @staticmethod
    def get_meta_info(amazon_message: AmazonListMessage):
        return MetaInfo(
            source_type = Source.SPIDER,
            parser_name = amazon_message.parser_name,
            parses_at = amazon_message.create_time 
        )
    
    @staticmethod
    def get_review_summary(crawl_result: CrawlResult) -> ReviewSummary:
        return ReviewSummary(
            rating = crawl_result.rating,
            ratings_total= crawl_result.ratings_total
        )
    
    @staticmethod
    def get_standard_attributes(crawl_result: CrawlResult) -> StandardAttributes:
        standard_attributes = StandardAttributes()
        standard_attributes.is_member = crawl_result.is_prime
        standard_attributes.is_best_seller = crawl_result.bestseller is not None
        return standard_attributes
    
    @staticmethod
    def get_images(crawl_result: CrawlResult) -> Images:
        return Images(main_image=crawl_result.image) if crawl_result.image is not None else None
    
    @staticmethod
    def get_price(crawl_result: CrawlResult) -> Price:
        amazon_price = crawl_result.price if crawl_result.price is not None else None
        if amazon_price is None and CommonUtils.list_len(crawl_result.prices) > 0:
            amazon_price = next(filter(lambda price  : price.is_primary,crawl_result.prices))
        return AmazonListAdapter.convert_price(amazon_price)

    @staticmethod
    def get_rrp(crawl_result: CrawlResult) -> Price:
        if CommonUtils.list_len(crawl_result.prices) > 0:
            amazon_price = next(filter(lambda price  : price.is_rrp,crawl_result.prices))
            return AmazonListAdapter.convert_price(amazon_price)
        
    @staticmethod
    def convert_price(amazon_price : AmazonPrice)->Price:
        if amazon_price is None:
            return None
        currency_converter = CurrencyConverter(amazon_price.currency,amazon_price.value)
        price = Price(
                currency=currency_converter.get_currency_code(),
                value = currency_converter.get_subunit_value(),
                updates_at=str(int(datetime.now().timestamp()))
            )
        return price if CommonUtils.all_not_none(price.currency,price.value) else None
        
def main():
    amazon_message = read_mock_data("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/amazon_list_message.json",AmazonListMessage)
    favie_product: FavieProductDetail = AmazonListAdapter.convert_to_favie_product(amazon_message)
    print(favie_product.model_dump_json(exclude_none = True) if favie_product else None)

if __name__ == "__main__":
    main()
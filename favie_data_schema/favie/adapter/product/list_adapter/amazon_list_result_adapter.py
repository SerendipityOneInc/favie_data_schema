from favie_data_schema.favie.adapter.product.common.currency import CurrencyConverter
from favie_data_schema.favie.adapter.product.common.favie_product_adapter import FavieProductDetailAdapter
from favie_data_schema.favie.data.interface.product.favie_product_detail import *
from favie_data_schema.favie.data.crawl_data.crawler.amazon_list_crawler_result import AmazonListCrawlResult,Price as AmazonPrice
from favie_common.common.common_utils import CommonUtils
from favie_data_schema.favie.adapter.tools.data_mock_read import read_file

from datetime import datetime
import logging

from favie_data_schema.favie.data.interface.product.favie_product_detail import FavieProductDetail

class AmazoneListResultAdapter(FavieProductDetailAdapter):
    @staticmethod
    def convert_to_favie_product(crawl_result: AmazonListCrawlResult) -> FavieProductDetail:
        if crawl_result is None:
            return None                
        favie_product = FavieProductDetail()
        favie_product.sku_id = crawl_result.asin
        favie_product.site = "amazon.com"
        favie_product.title = crawl_result.title
        favie_product.link = crawl_result.link
        favie_product.price = AmazoneListResultAdapter.get_price(crawl_result)
        favie_product.rrp = AmazoneListResultAdapter.get_rrp(crawl_result)
        favie_product.images = AmazoneListResultAdapter.get_images(crawl_result)
        favie_product.standard_attributes = AmazoneListResultAdapter.get_standard_attributes(crawl_result)
        favie_product.review_summary = AmazoneListResultAdapter.get_review_summary(crawl_result)
        return favie_product
    
    @staticmethod
    def deserialize(message :str):
        try:
            return AmazonListCrawlResult.model_validate_json(message)
        except Exception as e:
            logging.error(f"AmazoneListResultAdapter Deserialize message error {e}")
            return None
        
    @staticmethod
    def get_review_summary(crawl_result: AmazonListCrawlResult) -> ReviewSummary:
        return ReviewSummary(
            rating = crawl_result.rating,
            ratings_total= crawl_result.ratings_total
        )
    
    @staticmethod
    def get_standard_attributes(crawl_result: AmazonListCrawlResult) -> StandardAttributes:
        standard_attributes = StandardAttributes()
        standard_attributes.is_member = crawl_result.is_prime
        standard_attributes.is_best_seller = crawl_result.bestseller is not None
        return standard_attributes
    
    @staticmethod
    def get_images(crawl_result: AmazonListCrawlResult) -> Images:
        return Images(main_image=crawl_result.image) if crawl_result.image is not None else None
    
    @staticmethod
    def get_price(crawl_result: AmazonListCrawlResult) -> Price:
        amazon_price = crawl_result.price if crawl_result.price is not None else None
        if amazon_price is None and CommonUtils.list_len(crawl_result.prices) > 0:
            amazon_price = next(filter(lambda price  : price.is_primary,crawl_result.prices))
        return AmazoneListResultAdapter.convert_price(amazon_price)

    @staticmethod
    def get_rrp(crawl_result: AmazonListCrawlResult) -> Price:
        if CommonUtils.list_len(crawl_result.prices) > 0:
            amazon_price = next(filter(lambda price  : price.is_rrp,crawl_result.prices))
            return AmazoneListResultAdapter.convert_price(amazon_price)
        
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
    amazon_message = read_file("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/amazon_list_result.json")
    favie_product: FavieProductDetail = AmazoneListResultAdapter.convert_to_favie_product(amazon_message)
    print(favie_product.model_dump_json(exclude_none = True) if favie_product else None)

if __name__ == "__main__":
    main()
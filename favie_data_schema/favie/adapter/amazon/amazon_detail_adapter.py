from favie_data_schema.favie.adapter.common.favie_adapter import FavieProductAdapter
from favie_data_schema.favie.adapter.common.favie_product_utils import FavieProductUtils
from favie_data_schema.favie.data.interface.product.favie_product_detail import *
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_detail import RainforestProductDetail
from favie_data_schema.favie.adapter.common.crawler_kakfa_message import CrawlerKafkaMessage
from favie_data_schema.favie.adapter.common.common_utils import CommonUtils
from favie_data_schema.favie.adapter.amazon.amazon_detail_convert import AmazonDetailConvert
from favie_data_schema.favie.adapter.amazon.amazon_review_adapter import AmazonReviewAdapter
from favie_data_schema.favie.adapter.data_mock.data_mock_read import read_amazon_message
from datetime import datetime
import logging

from favie_data_schema.favie.data.interface.product.favie_product_detail import FavieProductDetail
from favie_data_schema.favie.data.interface.product.favie_product_review import FavieProductReview

class AmazonDetailAdapter(FavieProductAdapter):
    @staticmethod
    def convert_to_favie_product(amazon_message: CrawlerKafkaMessage) -> FavieProductDetail:
        favie_product = AmazonDetailConvert.convert_to_favie_product(amazon_message)
        if(favie_product is None):
            return None
        favie_reviews = AmazonReviewAdapter.convert_to_favie_review(amazon_message)
        
        favie_product.f_sku_id = FavieProductUtils.gen_f_sku_id(favie_product)
        favie_product.f_spu_id = FavieProductUtils.gen_f_spu_id(favie_product)
        top_review_ids = [x.f_review_id for x in favie_reviews if x is not None] if CommonUtils.list_len(favie_reviews) > 0 else None
        favie_product.review_summary = AmazonDetailAdapter.get_review_summary(amazon_message.crawl_result,top_review_ids)
        
        return favie_product
    
    @staticmethod
    def get_review_summary(rainforest_product_detail: RainforestProductDetail,favie_reviews:list[str]):
        product = rainforest_product_detail.product if rainforest_product_detail is not None else None
        if product is None:
            return None 
        review_summary = ReviewSummary(
            rating = product.rating,
            ratings_total= product.ratings_total,
            reviews_total= product.reviews_total,
            top_reviews= favie_reviews if CommonUtils.list_len(favie_reviews) > 0 else None
        )
        return review_summary if CommonUtils.any_not_none(review_summary.rating,review_summary.ratings_total,review_summary.reviews_total) else None
        
def main():
    amazon_message = read_amazon_message("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/amazon_message.json")
    favie_product: FavieProductDetail = AmazonDetailAdapter.convert_to_favie_product(amazon_message)
    print(favie_product.model_dump_json(exclude_none = True) if favie_product else None)

if __name__ == "__main__":
    main()
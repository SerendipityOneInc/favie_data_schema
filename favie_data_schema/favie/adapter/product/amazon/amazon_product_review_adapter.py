from typing import List
from favie_data_schema.favie.adapter.product.amazon.amazon_product_detail_convert import AmazonProductDetailConvert
from favie_data_schema.favie.adapter.product.amazon.amazon_product_review_convert import AmazonProductReviewConvert
from favie_data_schema.favie.adapter.product.common.favie_product_adapter import FavieProductReviewAdapter
from favie_data_schema.favie.adapter.product.common.favie_product_utils import FavieProductUtils
from favie_data_schema.favie.adapter.product.common.product_detail_crawler_message import ProductDetailCrawlerMessage
from favie_data_schema.favie.data.interface.product.favie_product_detail import *
from favie_data_schema.favie.adapter.common.common_utils import CommonUtils
from favie_data_schema.favie.adapter.tools.data_mock_read import read_mock_data
import logging

from favie_data_schema.favie.data.interface.product.favie_product_review import FavieProductReview

class AmazonProductReviewAdapter(FavieProductReviewAdapter):
    @staticmethod
    def convert_to_favie_review(crawler_kafka_message: ProductDetailCrawlerMessage) -> list[FavieProductReview]:
        favie_reviews = AmazonProductReviewConvert.convert_to_favie_review(crawler_kafka_message)
        if favie_reviews is None:
            return None
        
        favie_product = AmazonProductDetailConvert.convert_to_favie_product(crawler_kafka_message)
        f_spu_id = FavieProductUtils.gen_f_sku_id(favie_product)
        if f_spu_id is None:    
            return None
        
        for favie_review in favie_reviews:
            favie_review.f_spu_id = f_spu_id
            favie_review.spu_id = favie_product.spu_id
            favie_review.site = favie_product.site
            favie_review.f_review_id = FavieProductUtils.gen_review_id(f_spu_id,favie_review)
            
        return favie_reviews if CommonUtils.list_len(favie_reviews) > 0 else None
    
    
def main():
    amazon_message = read_mock_data("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/amazon_message.json",ProductDetailCrawlerMessage)
    favie_reviews = AmazonProductReviewAdapter.convert_to_favie_review(amazon_message)
    if favie_reviews is None:
        return None
    for favie_review in favie_reviews:
        print(favie_review.model_dump_json())

if __name__ == "__main__":
    main()
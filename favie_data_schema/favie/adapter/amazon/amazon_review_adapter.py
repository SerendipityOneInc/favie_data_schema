from typing import List
from favie_data_schema.favie.adapter.common.favie_adapter import FavieReviewAdapter
from favie_data_schema.favie.data.interface.product.favie_product_detail import *
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_detail import RainforestProductDetail, TopReviews
from favie_data_schema.favie.adapter.common.crawler_kakfa_message import CrawlerKafkaMessage
from favie_data_schema.favie.adapter.common.favie_product_utils import FavieProductUtils
from favie_data_schema.favie.adapter.amazon.amazon_detail_convert import AmazonDetailConvert
from favie_data_schema.favie.adapter.amazon.amazon_review_convert import AmazonReviewConvert
from favie_data_schema.favie.adapter.data_mock.data_mock_read import read_amazon_message
from favie_data_schema.favie.adapter.common.common_utils import CommonUtils
import logging

from favie_data_schema.favie.data.interface.product.favie_product_review import FavieProductReview

class AmazonReviewAdapter(FavieReviewAdapter):
    @staticmethod
    def convert_to_favie_review(crawler_kafka_message: CrawlerKafkaMessage) -> list[FavieProductReview]:
        favie_reviews = AmazonReviewConvert.convert_to_favie_review(crawler_kafka_message)
        if favie_reviews is None:
            return None
        
        favie_product = AmazonDetailConvert.convert_to_favie_product(crawler_kafka_message)
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
    amazon_message = read_amazon_message("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/review_bug.json")
    favie_reviews = AmazonReviewAdapter.convert_to_favie_review(amazon_message)
    if favie_reviews is None:
        return None
    for favie_review in favie_reviews:
        print(favie_review.model_dump_json())

if __name__ == "__main__":
    main()
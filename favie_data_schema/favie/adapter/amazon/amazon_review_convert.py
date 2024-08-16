from favie_data_schema.favie.data.interface.product.favie_product import *
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_detail import RainforestProductDetail, TopReviews
from favie_data_schema.favie.adapter.common.crawler_kakfa_message import CrawlerKafkaMessage
from favie_data_schema.favie.adapter.data_mock.amazon_message_read import read_amazon_message
from favie_data_schema.favie.adapter.common.common_utils import CommonUtils
import logging

from favie_data_schema.favie.data.interface.product.favie_review import FavieReview

class AmazonReviewConvert():
    @staticmethod
    def convert_to_favie_review(crawler_kafka_message: CrawlerKafkaMessage) -> list[FavieReview]:
        if not AmazonReviewConvert.__check(crawler_kafka_message):
            return None
        reviews = crawler_kafka_message.crawl_result.product.top_reviews
        favie_reviews:List[FavieReview] = [AmazonReviewConvert.__convert_to_favie_review(x) for x in reviews if x is not None] if reviews is not None else None
        return favie_reviews if CommonUtils.list_len(favie_reviews) > 0 else None
    
    def __convert_to_favie_review(review: TopReviews)->FavieReview:
        if(review is None): 
            return None
        favie_review = FavieReview()
        favie_review.author_id = review.profile.id
        favie_review.author_name = review.profile.name
        favie_review.author_url = review.profile.link
        favie_review.review_id = review.id
        favie_review.link = review.link
        favie_review.body = review.body
        favie_review.title = review.title
        favie_review.helpful_votes = review.helpful_votes
        favie_review.vine_program = review.vine_program
        favie_review.verified_purchase = review.verified_purchase
        favie_review.is_global_review = review.is_global_review
        favie_review.review_country = review.review_country
        return favie_review
    
    @staticmethod
    def __check(crawler_kafka_message: RainforestProductDetail):
        if(crawler_kafka_message is None):
            return False
        if(crawler_kafka_message.crawl_result is None):
            return False
        if(crawler_kafka_message.crawl_result.product is None):
            return False
        if(CommonUtils.list_len(crawler_kafka_message.crawl_result.product.top_reviews) == 0):
            return False
        return True
    
def main():
    amazon_message = read_amazon_message("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/amazon_message.json")
    favie_reviews: list[FavieReview] = AmazonReviewConvert.convert_to_favie_review(amazon_message)
    if favie_reviews is not None:
        for favie_review in favie_reviews:
            if(favie_review is not None):
                print(favie_review.model_dump_json())

if __name__ == "__main__":
    main()
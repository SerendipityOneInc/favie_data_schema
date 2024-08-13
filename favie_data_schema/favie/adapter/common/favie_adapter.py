from favie_data_schema.favie.adapter.common.crawler_kakfa_message import CrawlerKafkaMessage
from favie_data_schema.favie.data.interface.product.favie_product import FavieProduct
from favie_data_schema.favie.data.interface.product.favie_review import FavieReview


class FavieProductAdapter():
    @staticmethod
    def convert_to_favie_product(crawler_kafka_message: CrawlerKafkaMessage) -> FavieProduct:
        # TODO: implement
        pass


class FavieReviewAdapter():
    @staticmethod
    def convert_to_favie_review(crawler_kafka_message: CrawlerKafkaMessage) -> list[FavieReview]:
        # TODO: implement
        pass 
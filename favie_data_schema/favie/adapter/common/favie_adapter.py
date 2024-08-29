from favie_data_schema.favie.adapter.common.crawler_kakfa_message import CrawlerKafkaMessage
from favie_data_schema.favie.data.interface.product.favie_product_detail import FavieProductDetail
from favie_data_schema.favie.data.interface.product.favie_product_review import FavieProductReview


class FavieProductAdapter():
    @staticmethod
    def convert_to_favie_product(crawler_kafka_message: CrawlerKafkaMessage) -> FavieProductDetail:
        # TODO: implement
        pass

class FavieReviewAdapter():
    @staticmethod
    def convert_to_favie_review(crawler_kafka_message: CrawlerKafkaMessage) -> list[FavieProductDetail]:
        # TODO: implement
        pass 
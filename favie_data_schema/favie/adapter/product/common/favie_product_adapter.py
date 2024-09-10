from favie_data_schema.favie.adapter.product.common.product_detail_crawler_message import ProductDetailCrawlerMessage
from favie_data_schema.favie.data.interface.product.favie_product_detail import FavieProductDetail
from favie_data_schema.favie.data.interface.product.favie_product_review import FavieProductReview


class FavieProductDetailAdapter():
    @staticmethod
    def convert_to_favie_product(crawler_kafka_message: ProductDetailCrawlerMessage) -> FavieProductDetail:
        # TODO: implement
        pass

class FavieProductReviewAdapter():
    @staticmethod
    def convert_to_favie_review(crawler_kafka_message: ProductDetailCrawlerMessage) -> list[FavieProductReview]:
        # TODO: implement
        pass 
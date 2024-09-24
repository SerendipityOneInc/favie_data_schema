from favie_data_schema.favie.adapter.product.common.product_crawler_message import ProductDetailCrawlerMessage
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_review import RainforestProductReview
from favie_data_schema.favie.data.interface.product.favie_product import FavieProductDetail, FavieProductReview, FavieProductReviewSummary
class FavieProductDetailAdapter():
    @staticmethod
    def crawl_detail_to_product_detail(crawler_detail_message: ProductDetailCrawlerMessage) -> FavieProductDetail:
        pass

class FavieProductReviewAdapter():
    @staticmethod
    def crawl_detail_to_product_review(crawler_detail_message: ProductDetailCrawlerMessage) -> list[FavieProductReview]:
        pass 
    
    @staticmethod
    def crawl_review_to_product_review_summary(crawler_review_message: RainforestProductReview) -> FavieProductReviewSummary:
        pass
    
    @staticmethod
    def crawl_review_to_product_review(crawler_review_message: RainforestProductReview) -> list[FavieProductReview]:
        pass

from typing import List, Optional
from favie_data_schema.favie.adapter.common.spark_message import StarkProductDetailMessage, StarkProductListMessage
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_review import RainforestProductReview
from favie_data_schema.favie.data.interface.product.favie_product import FavieProductDetail, FavieProductReview, FavieProductReviewSummary
class FavieProductDetailAdapter():
    @staticmethod
    def stark_detail_to_favie_detail(crawler_detail_message: StarkProductDetailMessage) -> Optional[FavieProductDetail]:
        pass
    
    @staticmethod
    def stark_list_to_favie_details(crawler_detail_message: StarkProductListMessage) -> Optional[List[FavieProductDetail]]:
        pass

class FavieProductReviewAdapter():
    @staticmethod
    def stark_detail_to_favie_review(crawler_detail_message: StarkProductDetailMessage) -> Optional[List[FavieProductReview]]:
        pass 
    
    @staticmethod
    def stark_review_to_favie_review_summary(crawler_review_message: RainforestProductReview) -> Optional[FavieProductReviewSummary]:
        pass
    
    @staticmethod
    def stark_reviews_to_favie_reviews(crawler_review_message: RainforestProductReview) -> Optional[List[FavieProductReview]]:
        pass

from favie_data_schema.favie.adapter.product.product_detail_adapter.stark_product_detail_convert import StarkProductDetailConvert
from favie_data_schema.favie.adapter.product.product_review_adapter.stark_product_review_adapter import StarkProductReviewAdapter
from favie_data_schema.favie.adapter.product.common.favie_product_adapter import FavieProductDetailAdapter
from favie_data_schema.favie.adapter.product.common.favie_product_utils import FavieProductUtils
from favie_data_schema.favie.adapter.common.spark_message import StarkProductDetailMessage
from favie_data_schema.favie.data.interface.product.favie_product import *
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_detail import RainforestProductDetail
from favie_data_common.common.common_utils import CommonUtils
from favie_data_schema.favie.adapter.tools.data_mock_read import read_object
from datetime import datetime
import logging


class StarkProductDetailAdapter(FavieProductDetailAdapter):
    @staticmethod
    def stark_detail_to_favie_detail(amazon_message: StarkProductDetailMessage) -> Optional[FavieProductDetail]:
        favie_product = StarkProductDetailConvert.convert_to_favie_product(amazon_message)
        if(favie_product is None):
            return None
        favie_reviews = StarkProductReviewAdapter.stark_detail_to_favie_review(amazon_message)
        
        favie_product.f_sku_id = FavieProductUtils.gen_f_sku_id(favie_product)
        favie_product.f_spu_id = FavieProductUtils.gen_f_spu_id(favie_product)
        top_review_ids = [x.f_review_id for x in favie_reviews if x is not None] if CommonUtils.list_len(favie_reviews) > 0 else None
        favie_product.review_summary = StarkProductDetailAdapter.get_review_summary(amazon_message.crawl_result,top_review_ids)
        
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
            top_reviews= favie_reviews if CommonUtils.list_len(favie_reviews) > 0 else None,
            f_updates_at=str(int(datetime.now().timestamp()))
        )
        return review_summary if CommonUtils.any_not_none(review_summary.rating,review_summary.ratings_total,review_summary.reviews_total) else None
        
def main():
    amazon_message = read_object("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/bug.json",StarkProductDetailMessage)
    favie_product: FavieProductDetail = StarkProductDetailAdapter.stark_detail_to_favie_detail(amazon_message)
    print(favie_product.model_dump_json(exclude_none = True) if favie_product else None)

if __name__ == "__main__":
    main()
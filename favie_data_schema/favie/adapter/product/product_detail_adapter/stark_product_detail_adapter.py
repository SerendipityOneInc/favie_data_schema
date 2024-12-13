from datetime import datetime
from typing import Optional

from favie_data_common.common.common_utils import CommonUtils

from favie_data_schema.favie.adapter.common.stark_message import StarkProductDetailMessage
from favie_data_schema.favie.adapter.product.common.favie_product_adapter import FavieProductDetailAdapter
from favie_data_schema.favie.adapter.product.common.favie_product_utils import FavieProductUtils
from favie_data_schema.favie.adapter.product.common.review_summary_generator import ReviewSummaryGeneratorProxy
from favie_data_schema.favie.adapter.product.product_detail_adapter.stark_product_detail_convert import (
    StarkProductDetailConvert,
)
from favie_data_schema.favie.adapter.product.product_review_adapter.stark_product_review_adapter import (
    StarkProductReviewAdapter,
)
from favie_data_schema.favie.adapter.tools.data_mock_read import read_object
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_detail import RainforestProductDetail
from favie_data_schema.favie.data.interface.product.favie_product import RatingBreakdown, ReviewSummary
from favie_data_schema.favie.data.interface.product.favie_product_detail import FavieProductDetail


class StarkProductDetailAdapter(FavieProductDetailAdapter):
    @staticmethod
    def stark_detail_to_favie_detail(stark_detail_message: StarkProductDetailMessage) -> Optional[FavieProductDetail]:
        favie_product = StarkProductDetailConvert.convert_to_favie_product(stark_detail_message)
        if favie_product is None:
            return None
        favie_reviews = StarkProductReviewAdapter.stark_detail_to_favie_reviews(stark_detail_message)

        favie_product.f_sku_id = FavieProductUtils.gen_f_sku_id(favie_product)
        favie_product.f_spu_id = FavieProductUtils.gen_f_spu_id(favie_product)
        top_review_ids = (
            [x.f_review_id for x in favie_reviews if x is not None] if CommonUtils.list_len(favie_reviews) > 0 else None
        )
        review_summary_link = ReviewSummaryGeneratorProxy.gen_url(favie_product.site, favie_product.sku_id)
        favie_product.review_summary = StarkProductDetailAdapter.get_review_summary(
            stark_detail_message.crawl_result, top_review_ids, review_summary_link
        )

        return favie_product

    @staticmethod
    def get_review_summary(rainforest_product_detail: RainforestProductDetail, top_reviews: list[str], link: str):
        product = rainforest_product_detail.product if rainforest_product_detail is not None else None
        if product is None:
            return None
        review_summary = ReviewSummary(
            link=link,
            rating=product.rating,
            ratings_total=product.ratings_total,
            rating_breakdown=StarkProductDetailAdapter.get_rating_breakdown(rainforest_product_detail),
            reviews_total=product.reviews_total,
            top_reviews=top_reviews if CommonUtils.list_len(top_reviews) > 0 else None,
            f_updates_at=str(int(datetime.now().timestamp())),
        )
        review_summary = FavieProductUtils.cal_percentage_to_review_summary(review_summary)
        return (
            review_summary
            if CommonUtils.any_not_none(
                review_summary.rating, review_summary.ratings_total, review_summary.reviews_total
            )
            else None
        )

    @staticmethod
    def get_rating_breakdown(rainforest_product_detail: RainforestProductDetail):
        product = rainforest_product_detail.product if rainforest_product_detail is not None else None
        if product is None:
            return None
        rating_breakdown = RatingBreakdown(
            five_star=product.rating_breakdown.five_star.count
            if product.rating_breakdown and product.rating_breakdown.five_star
            else None,
            four_star=product.rating_breakdown.four_star.count
            if product.rating_breakdown and product.rating_breakdown.four_star
            else None,
            three_star=product.rating_breakdown.three_star.count
            if product.rating_breakdown and product.rating_breakdown.three_star
            else None,
            two_star=product.rating_breakdown.two_star.count
            if product.rating_breakdown and product.rating_breakdown.two_star
            else None,
            one_star=product.rating_breakdown.one_star.count
            if product.rating_breakdown and product.rating_breakdown.one_star
            else None,
        )
        return (
            rating_breakdown
            if CommonUtils.any_not_none(
                rating_breakdown.five_star,
                rating_breakdown.four_star,
                rating_breakdown.three_star,
                rating_breakdown.two_star,
                rating_breakdown.one_star,
            )
            else None
        )


def main():
    amazon_message = read_object(
        "favie_data_schema/favie/resources/stark_product_detail_bug.json",
        StarkProductDetailMessage,
    )
    favie_product: FavieProductDetail = StarkProductDetailAdapter.stark_detail_to_favie_detail(amazon_message)
    print(favie_product.model_dump_json(exclude_none=True) if favie_product else None)


if __name__ == "__main__":
    main()

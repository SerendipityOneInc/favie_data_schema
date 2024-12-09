from typing import List, Optional

from favie_data_common.common.common_utils import CommonUtils

from favie_data_schema.favie.adapter.common.stark_message import StarkProductDetailMessage, StarkProductReviewMessage
from favie_data_schema.favie.adapter.common.stark_message_utils import StarkMessageUtils
from favie_data_schema.favie.adapter.product.common.favie_product_adapter import FavieProductReviewAdapter
from favie_data_schema.favie.adapter.product.common.favie_product_utils import FavieProductUtils
from favie_data_schema.favie.adapter.product.common.review_summary_generator import ReviewSummaryGeneratorProxy
from favie_data_schema.favie.adapter.product.product_detail_adapter.stark_product_detail_convert import (
    StarkProductDetailConvert,
)
from favie_data_schema.favie.adapter.product.product_review_adapter.stark_product_review_convert import (
    StarkProductReviewConvert,
)
from favie_data_schema.favie.adapter.tools.data_mock_read import read_object
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_review import (
    RatingBreakdown as RFRatingBreakdown,
)
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_review import Reviews, Summary
from favie_data_schema.favie.data.interface.common.favie_enum import MessageDataType
from favie_data_schema.favie.data.interface.common.favie_model import MetaInfo
from favie_data_schema.favie.data.interface.product.favie_product import RatingBreakdown, ReviewSummary
from favie_data_schema.favie.data.interface.product.favie_product_review import FavieProductReview
from favie_data_schema.favie.data.interface.product.favie_product_review_summary import FavieProductReviewSummary

class StarkProductReviewAdapter(FavieProductReviewAdapter):
    @staticmethod
    def stark_detail_to_favie_reviews(
        stark_detail_message: StarkProductDetailMessage,
    ) -> Optional[List[FavieProductReview]]:
        favie_reviews = StarkProductReviewConvert.convert_to_favie_review(stark_detail_message)
        if favie_reviews is None:
            return None

        favie_product = StarkProductDetailConvert.convert_to_favie_product(stark_detail_message)
        f_spu_id = FavieProductUtils.gen_f_spu_id(favie_product)
        if f_spu_id is None:
            return None

        for favie_review in favie_reviews:
            favie_review.f_spu_id = f_spu_id
            favie_review.spu_id = favie_product.spu_id
            favie_review.site = favie_product.site
            favie_review.sku_id = favie_product.sku_id
            favie_review.f_review_id = FavieProductUtils.gen_f_review_id(favie_review)

        return favie_reviews if CommonUtils.list_len(favie_reviews) > 0 else None

    @staticmethod
    def stark_review_to_favie_review_summary(
        stark_review_message: StarkProductReviewMessage,
    ) -> Optional[FavieProductReviewSummary]:
        if not StarkProductReviewAdapter.__crawl_review_message_check(stark_review_message):
            return None
        crawl_result = stark_review_message.crawl_result
        if crawl_result.summary is None:
            return None

        favie_review_summary = FavieProductReviewSummary()
        favie_review_summary.spu_id = crawl_result.product.parent_asin
        favie_review_summary.sku_id = crawl_result.product.asin
        favie_review_summary.site = StarkMessageUtils.get_domain(stark_review_message)
        favie_review_summary.link = ReviewSummaryGeneratorProxy.gen_url(
            favie_review_summary.site, favie_review_summary.sku_id
        )
        favie_review_summary.f_meta = MetaInfo(
            source_type=str(stark_review_message.source),
            parser_name=f"{stark_review_message.parser_name}-adapter",
            parses_at=StarkMessageUtils.get_parse_time(stark_review_message),
        )
        summary: Summary = crawl_result.summary
        rating_breakdown: RFRatingBreakdown | None = summary.rating_breakdown

        favie_review_summary.rating = summary.rating
        favie_review_summary.ratings_total = summary.ratings_total
        favie_review_summary.ratings_total_filtered = summary.ratings_total_filtered
        if rating_breakdown:
            favie_review_summary.five_star = (
                rating_breakdown.five_star.count if rating_breakdown.five_star is not None else None
            )
            favie_review_summary.four_star = (
                rating_breakdown.four_star.count if rating_breakdown.four_star is not None else None
            )
            favie_review_summary.three_star = (
                rating_breakdown.three_star.count if rating_breakdown.three_star is not None else None
            )
            favie_review_summary.two_star = (
                rating_breakdown.two_star.count if rating_breakdown.two_star is not None else None
            )
            favie_review_summary.one_star = (
                rating_breakdown.one_star.count if rating_breakdown.one_star is not None else None
            )
        favie_review_summary.reviews_total = summary.reviews_total
        favie_review_summary.reviews_total_filtered = summary.reviews_total_filtered

        return favie_review_summary

    @staticmethod
    def stark_review_to_favie_reviews(
        stark_review_message: StarkProductReviewMessage,
    ) -> Optional[List[FavieProductReview]]:
        if not StarkProductReviewAdapter.__crawl_review_message_check(stark_review_message):
            return None
        crawl_result = stark_review_message.crawl_result
        if CommonUtils.is_empty(crawl_result.reviews):
            return None
        meta = MetaInfo(
            source_type=str(stark_review_message.source),
            parser_name=f"{stark_review_message.parser_name}-adapter",
            parses_at=StarkMessageUtils.get_parse_time(stark_review_message),
            data_type=str(MessageDataType.PRODUCT_REVIEW_CRAWLER.value),
        )
        return [
            StarkProductReviewAdapter.__convert_review(
                review=review,
                site=StarkMessageUtils.get_domain(stark_review_message),
                spu_id=crawl_result.product.parent_asin,
                sku_id=crawl_result.product.asin,
                meta=meta,
            )
            for review in crawl_result.reviews
            if review is not None
        ]

    @staticmethod
    def favie_review_summary_to_defail_review_summary(
        favie_review_summary: FavieProductReviewSummary,
    ) -> Optional[ReviewSummary]:
        if favie_review_summary is None:
            return None
        review_summary = ReviewSummary()
        review_summary.link = favie_review_summary.link
        review_summary.rating = favie_review_summary.rating
        review_summary.ratings_total = favie_review_summary.ratings_total
        review_summary.ratings_total_filtered = favie_review_summary.ratings_total_filtered
        review_summary.rating_breakdown = RatingBreakdown(
            five_star=favie_review_summary.five_star,
            four_star=favie_review_summary.four_star,
            three_star=favie_review_summary.three_star,
            two_star=favie_review_summary.two_star,
            one_star=favie_review_summary.one_star,
        )
        review_summary.reviews_total = favie_review_summary.reviews_total
        review_summary.reviews_total_filtered = favie_review_summary.reviews_total_filtered
        review_summary.f_updates_at = favie_review_summary.f_meta.parses_at
        return FavieProductUtils.cal_percentage_to_review_summary(review_summary)

    @staticmethod
    def __crawl_review_message_check(stark_review_message: StarkProductReviewMessage) -> bool:
        if stark_review_message is None:
            return False
        if stark_review_message.crawl_result is None:
            return False
        if stark_review_message.crawl_result.product is None:
            return False
        if CommonUtils.all_none(
            stark_review_message.crawl_result.product.asin, stark_review_message.crawl_result.product.parent_asin
        ):
            return False
        return True

    def __convert_review(*, review: Reviews, site, spu_id, sku_id, meta) -> FavieProductReview:
        favie_review = FavieProductReview()
        favie_review.site = site
        favie_review.spu_id = spu_id
        favie_review.sku_id = sku_id
        favie_review.author_id = review.profile.id if review.profile is not None else None
        favie_review.author_name = review.profile.name if review.profile is not None else None
        favie_review.author_url = review.profile.link if review.profile is not None else None
        favie_review.review_id = review.id
        favie_review.link = review.link
        favie_review.body = review.body
        favie_review.body_html = review.body_html
        favie_review.title = review.title
        favie_review.helpful_votes = review.helpful_votes
        favie_review.unhelpful_votes = None
        favie_review.vine_program = review.vine_program
        favie_review.verified_purchase = review.verified_purchase
        favie_review.is_global_review = review.is_global_review
        favie_review.review_country = review.review_country
        favie_review.rating = review.rating
        favie_review.date_raw = review.date.raw if review.date is not None else None
        favie_review.date_utc = review.date.utc if review.date is not None else None
        favie_review.images = review.images
        if review.attributes is not None:
            favie_review.attributes = [
                FavieAttributeItem(name=x.name, value=x.value) for x in review.attributes
            ]
        else:
            favie_review.attributes = None
        favie_review.videos = None
        favie_review.position = review.position
        favie_review.stark_tag = review.stark_tag
        favie_review.f_meta = meta
        return favie_review


def test_stark_detail_to_product_review():
    amazon_message = read_object(
        "/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/stark_product_detail_message.json",
        StarkProductDetailMessage,
    )
    favie_reviews = StarkProductReviewAdapter.stark_detail_to_favie_reviews(amazon_message)
    if favie_reviews is None:
        return None
    for favie_review in favie_reviews:
        print(favie_review.model_dump_json(exclude_none=True))


def test_stark_review_to_product_review_summary():
    amazon_message = read_object(
        "/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/stark_product_review_message.json",
        StarkProductReviewMessage,
    )
    favie_review_summary = StarkProductReviewAdapter.stark_review_to_favie_review_summary(amazon_message)
    if favie_review_summary is not None:
        print(favie_review_summary.model_dump_json(exclude_none=True))


def test_favie_review_summary_to_product_review_summary():
    amazon_message = read_object(
        "/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/stark_product_review_message.json",
        StarkProductReviewMessage,
    )
    favie_review_summary = StarkProductReviewAdapter.stark_review_to_favie_review_summary(amazon_message)
    if favie_review_summary is not None:
        product_review_summary = StarkProductReviewAdapter.favie_review_summary_to_defail_review_summary(
            favie_review_summary
        )
        print(product_review_summary.model_dump_json(exclude_none=True))


def test_stark_review_to_product_review():
    amazon_message = read_object(
        "/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/review_bug.json",
        StarkProductReviewMessage,
    )
    favie_reviews = StarkProductReviewAdapter.stark_review_to_favie_reviews(amazon_message)
    if favie_reviews is None:
        return None
    for favie_review in favie_reviews:
        print(favie_review.model_dump_json(exclude_none=True))


if __name__ == "__main__":
    test_stark_review_to_product_review()
    # test_stark_detail_to_product_review()
    # test_stark_review_to_product_review_summary()
    # test_favie_review_summary_to_product_review_summary()

from typing import List

from favie_data_common.common.common_utils import CommonUtils

from favie_data_schema.favie.adapter.common.image_url_rewriter.image_url_rewriter_proxy import ImageUrlRewriterProxy
from favie_data_schema.favie.adapter.common.stark_message import StarkProductDetailMessage
from favie_data_schema.favie.adapter.common.stark_message_utils import StarkMessageUtils
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_detail import TopReviews
from favie_data_schema.favie.data.interface.common.favie_enum import FavieDataStatus, MessageDataType
from favie_data_schema.favie.data.interface.common.favie_model import MetaInfo
from favie_data_schema.favie.data.interface.product.favie_product import AttributeItem
from favie_data_schema.favie.data.interface.product.favie_product_review import FavieProductReview


class StarkProductReviewConvert:
    def __init__(self):
        self.image_rewriter = ImageUrlRewriterProxy(rewrite_size=640)

    def convert_to_favie_review(self, stark_detail_message: StarkProductDetailMessage) -> list[FavieProductReview]:
        if not self.__check(stark_detail_message):
            return None
        reviews = stark_detail_message.crawl_result.product.top_reviews
        parse_time = StarkMessageUtils.get_parse_time(stark_detail_message)
        source_site = StarkMessageUtils.get_domain(stark_detail_message)
        favie_reviews: List[FavieProductReview] = (
            [
                self.__convert_to_favie_review(
                    review=x,
                    source=stark_detail_message.source,
                    source_site=source_site,
                    parser_name=stark_detail_message.parser_name,
                    parse_time=parse_time,
                    app_key=stark_detail_message.app_key,
                )
                for x in reviews
                if x is not None
            ]
            if reviews is not None
            else None
        )
        return favie_reviews if CommonUtils.list_len(favie_reviews) > 0 else None

    def __convert_to_favie_review(
        self, *, review: TopReviews, source: int, source_site: str, parser_name: str, parse_time: str, app_key: str
    ) -> FavieProductReview:
        if review is None:
            return None
        favie_review = FavieProductReview()
        favie_review.author_id = review.profile.id if review.profile is not None else None
        favie_review.author_name = review.profile.name if review.profile is not None else None
        favie_review.author_url = review.profile.link if review.profile is not None else None
        favie_review.review_id = review.id
        favie_review.link = review.link
        favie_review.body = review.body
        favie_review.body_html = review.body_html
        favie_review.title = review.title
        favie_review.helpful_votes = review.helpful_votes
        favie_review.vine_program = review.vine_program
        favie_review.verified_purchase = review.verified_purchase
        favie_review.is_global_review = review.is_global_review
        favie_review.review_country = review.review_country
        favie_review.rating = review.rating
        favie_review.date_raw = review.date.raw if review.date is not None else None
        favie_review.date_utc = review.date.utc if review.date is not None else None
        favie_review.images = (
            [self.image_rewriter.rewrite(source, image) for image in review.stark_images if image]
            if review.stark_images
            else None
        )
        if review.stark_attributes is not None:
            favie_review.attributes = [AttributeItem(name=x.name, value=x.value) for x in review.stark_attributes]
        else:
            favie_review.attributes = None
        favie_review.videos = None
        favie_review.f_meta = MetaInfo(
            source_type=str(source),
            parser_name=f"{parser_name}-adapter",
            parses_at=parse_time,
            data_type=str(MessageDataType.PRODUCT_REVIEW_CRAWLER.value),
            app_key=app_key,
        )
        favie_review.f_status = str(FavieDataStatus.NORMAL.value)
        return favie_review

    def __check(self, stark_detail_message: StarkProductDetailMessage):
        if stark_detail_message is None:
            return False
        if stark_detail_message.crawl_result is None:
            return False
        if stark_detail_message.crawl_result.product is None:
            return False
        if CommonUtils.list_len(stark_detail_message.crawl_result.product.top_reviews) == 0:
            return False
        return True

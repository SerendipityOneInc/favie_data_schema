from typing import List
from favie_data_schema.favie.adapter.product.amazon.amazon_product_detail_convert import AmazonProductDetailConvert
from favie_data_schema.favie.adapter.product.amazon.amazon_product_review_convert import AmazonProductReviewConvert
from favie_data_schema.favie.adapter.product.common.favie_product_adapter import FavieProductReviewAdapter
from favie_data_schema.favie.adapter.product.common.favie_product_utils import FavieProductUtils
from favie_data_schema.favie.adapter.product.common.product_crawler_message import ProductDetailCrawlerMessage, ProductReviewCrawlerMessage
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_review import RatingBreakdown as RFRatingBreakdown, Summary,Reviews
from favie_data_schema.favie.data.interface.product.favie_product import FavieProductReview, FavieProductReviewSummary, MetaInfo,ReviewSummary,RatingBreakdown
from favie_common.common.common_utils import CommonUtils
from favie_data_schema.favie.adapter.tools.data_mock_read import read_mock_data
import logging


class AmazonProductReviewAdapter(FavieProductReviewAdapter):
    @staticmethod
    def crawl_detail_to_product_review(crawler_detail_message: ProductDetailCrawlerMessage) -> list[FavieProductReview]:
        favie_reviews = AmazonProductReviewConvert.convert_to_favie_review(crawler_detail_message)
        if favie_reviews is None:
            return None
        
        favie_product = AmazonProductDetailConvert.convert_to_favie_product(crawler_detail_message)
        f_spu_id = FavieProductUtils.gen_f_sku_id(favie_product)
        if f_spu_id is None:    
            return None
        
        for favie_review in favie_reviews:
            favie_review.f_spu_id = f_spu_id
            favie_review.spu_id = favie_product.spu_id
            favie_review.site = favie_product.site
            favie_review.f_review_id = FavieProductUtils.gen_review_id(favie_review)
            
        return favie_reviews if CommonUtils.list_len(favie_reviews) > 0 else None
    
    @staticmethod
    def crawl_review_to_product_review_summary(crawler_review_message: ProductReviewCrawlerMessage) -> FavieProductReviewSummary:
        if not AmazonProductReviewAdapter.__crawl_review_message_check(crawler_review_message):
            return None
        crawl_result = crawler_review_message.crawl_result
        if crawl_result.summary is None:
            return None

        favie_review_summary = FavieProductReviewSummary()
        
        favie_review_summary.spu_id = crawl_result.product.parent_asin
        favie_review_summary.sku_id = crawl_result.product.asin
        favie_review_summary.site = CommonUtils.get_domain(crawler_review_message.host)
        favie_review_summary.f_meta = MetaInfo(
            source_type = str(crawler_review_message.source),
            parser_name=f'{crawler_review_message.parser_name}-adapter',
            parses_at=str(int(CommonUtils.current_timestamp()))
        )
        
        favie_review_summary.summary = AmazonProductReviewAdapter.__get_summary(crawl_result.summary)
        return favie_review_summary
    
    @staticmethod
    def crawl_review_to_product_review(crawler_review_message: ProductReviewCrawlerMessage) -> list[FavieProductReview]:
        if not AmazonProductReviewAdapter.__crawl_review_message_check(crawler_review_message):
            return None
        crawl_result = crawler_review_message.crawl_result
        if CommonUtils.is_empty(crawl_result.reviews):
            return None
        meta = MetaInfo(
            source_type = str(crawler_review_message.source),
            parser_name=f'{crawler_review_message.parser_name}-adapter',
            parses_at=str(int(CommonUtils.current_timestamp()))
        )
        return [AmazonProductReviewAdapter.__convert_review(
                review=review,
                site=CommonUtils.get_domain(crawler_review_message.host),
                spu_id=crawl_result.product.parent_asin,
                sku_id=crawl_result.product.asin,
                meta=meta) for review in crawl_result.reviews if review is not None]
    
    @staticmethod
    def __crawl_review_message_check(crawler_review_message: ProductReviewCrawlerMessage) -> bool:
        if crawler_review_message is None:
            return False
        if crawler_review_message.crawl_result is None:
            return False
        if crawler_review_message.crawl_result.product is None:
            return False
        if CommonUtils.all_none(crawler_review_message.crawl_result.product.asin,crawler_review_message.crawl_result.product.parent_asin):
            return False
        return True
    
    @staticmethod
    def __get_summary(summary:Summary)->ReviewSummary:
        review_summary = ReviewSummary(
            rating=summary.rating,
            ratings_total=summary.ratings_total,
            ratings_total_filtered=summary.ratings_total_filtered,
            rating_breakdown=AmazonProductReviewAdapter.__convert_rating_breakdown(summary.rating_breakdown),
            reviews_total=summary.reviews_total,
            reviews_total_filtered=summary.reviews_total_filtered,
            
        )
        return review_summary
    
    def __convert_rating_breakdown(rating_breakdown:RFRatingBreakdown)->RatingBreakdown:
        return RatingBreakdown(
            five_star=rating_breakdown.five_star.count if rating_breakdown.five_star is not None else None,
            four_star=rating_breakdown.four_star.count if rating_breakdown.four_star is not None else None,
            three_star=rating_breakdown.three_star.count if rating_breakdown.three_star is not None else None,
            two_star=rating_breakdown.two_star.count if rating_breakdown.two_star is not None else None,
            one_star=rating_breakdown.one_star.count if rating_breakdown.one_star is not None else None
        )
        
    def __convert_review(*,review:Reviews,site,spu_id,sku_id,meta)->FavieProductReview:
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
        favie_review.videos = review.videos
        favie_review.position = review.position
        favie_review.f_meta = meta
        return favie_review
        
        
def test_crawl_detail_to_product_review():
    amazon_message = read_mock_data("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/amazon_message.json",ProductDetailCrawlerMessage)
    favie_reviews = AmazonProductReviewAdapter.crawl_detail_to_product_review(amazon_message)
    if favie_reviews is None:
        return None
    for favie_review in favie_reviews:
        print(favie_review.model_dump_json(exclude_none=True))

def test_crawl_review_to_product_review_summary():
    amazon_message = read_mock_data("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/crawl_product_review.json",ProductReviewCrawlerMessage)
    favie_review_summary = AmazonProductReviewAdapter.crawl_review_to_product_review_summary(amazon_message)
    if favie_review_summary is not None:
        print(favie_review_summary.model_dump_json(exclude_none=True))
        
def test_crawl_review_to_product_review():
    amazon_message = read_mock_data("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/crawl_product_review.json",ProductReviewCrawlerMessage)
    favie_reviews = AmazonProductReviewAdapter.crawl_review_to_product_review(amazon_message)
    if favie_reviews is None:
        return None
    for favie_review in favie_reviews:
        print(favie_review.model_dump_json(exclude_none=True))

if __name__ == "__main__":
    test_crawl_review_to_product_review()
    test_crawl_detail_to_product_review()
    test_crawl_review_to_product_review_summary()

import unittest

from favie_data_schema.favie.adapter.product.common.favie_product_utils import FavieProductUtils
from favie_data_schema.favie.data.interface.product.favie_product import RatingBreakdown, ReviewSummary


class TestReviewSummaryCalculations(unittest.TestCase):
    def setUp(self):
        # 创建一个用于测试的方法
        self.cal_percentage = FavieProductUtils.cal_percentage_to_review_summary  # 请替换 YourClass 为实际的类名

    def test_none_review_summary(self):
        result = self.cal_percentage(None)
        self.assertIsNone(result)

    def test_none_rating_breakdown(self):
        review_summary = ReviewSummary()
        review_summary.rating_breakdown = None
        result = self.cal_percentage(review_summary)
        self.assertEqual(result, review_summary)

    def test_zero_ratings(self):
        review_summary = ReviewSummary()
        review_summary.rating_breakdown = RatingBreakdown()
        review_summary.rating_breakdown.five_star = 0
        review_summary.rating_breakdown.four_star = 0
        review_summary.rating_breakdown.three_star = 0
        review_summary.rating_breakdown.two_star = 0
        review_summary.rating_breakdown.one_star = 0

        result = self.cal_percentage(review_summary)

        self.assertIsNone(result.rating_breakdown.five_percentage)
        self.assertIsNone(result.rating_breakdown.four_percentage)
        self.assertIsNone(result.rating_breakdown.three_percentage)
        self.assertIsNone(result.rating_breakdown.two_percentage)
        self.assertIsNone(result.rating_breakdown.one_percentage)

    def test_normal_case(self):
        review_summary = ReviewSummary()
        review_summary.rating_breakdown = RatingBreakdown()
        review_summary.rating_breakdown.five_star = 50
        review_summary.rating_breakdown.four_star = 30
        review_summary.rating_breakdown.three_star = 10
        review_summary.rating_breakdown.two_star = 5
        review_summary.rating_breakdown.one_star = 5

        result = self.cal_percentage(review_summary)

        self.assertEqual(result.rating_breakdown.five_percentage, 50)
        self.assertEqual(result.rating_breakdown.four_percentage, 30)
        self.assertEqual(result.rating_breakdown.three_percentage, 10)
        self.assertEqual(result.rating_breakdown.two_percentage, 5)
        self.assertEqual(result.rating_breakdown.one_percentage, 5)

    def test_some_none_values(self):
        review_summary = ReviewSummary()
        review_summary.rating_breakdown = RatingBreakdown()
        review_summary.rating_breakdown.five_star = 50
        review_summary.rating_breakdown.four_star = None
        review_summary.rating_breakdown.three_star = 10
        review_summary.rating_breakdown.two_star = None
        review_summary.rating_breakdown.one_star = 5

        result = self.cal_percentage(review_summary)

        self.assertEqual(result.rating_breakdown.five_percentage, 77)
        self.assertEqual(result.rating_breakdown.four_percentage, 0)
        self.assertEqual(result.rating_breakdown.three_percentage, 15)
        self.assertEqual(result.rating_breakdown.two_percentage, 0)
        self.assertEqual(result.rating_breakdown.one_percentage, 8)

    def test_rounding(self):
        review_summary = ReviewSummary()
        review_summary.rating_breakdown = RatingBreakdown()
        review_summary.rating_breakdown.five_star = 33
        review_summary.rating_breakdown.four_star = 33
        review_summary.rating_breakdown.three_star = 33
        review_summary.rating_breakdown.two_star = 0
        review_summary.rating_breakdown.one_star = 1

        result = self.cal_percentage(review_summary)

        self.assertEqual(result.rating_breakdown.five_percentage, 33)
        self.assertEqual(result.rating_breakdown.four_percentage, 33)
        self.assertEqual(result.rating_breakdown.three_percentage, 33)
        self.assertEqual(result.rating_breakdown.two_percentage, 0)
        self.assertEqual(result.rating_breakdown.one_percentage, 1)

    def test_rounding_percent_total_not_equal_100(self):
        review_summary = ReviewSummary()
        review_summary.rating_breakdown = RatingBreakdown()
        review_summary.rating_breakdown.five_star = 201
        review_summary.rating_breakdown.four_star = 23
        review_summary.rating_breakdown.three_star = 13
        review_summary.rating_breakdown.two_star = 10
        review_summary.rating_breakdown.one_star = 15

        result = self.cal_percentage(review_summary)

        self.assertEqual(result.rating_breakdown.five_percentage, 76)
        self.assertEqual(result.rating_breakdown.four_percentage, 9)
        self.assertEqual(result.rating_breakdown.three_percentage, 5)
        self.assertEqual(result.rating_breakdown.two_percentage, 4)
        self.assertEqual(result.rating_breakdown.one_percentage, 6)


if __name__ == "__main__":
    unittest.main()

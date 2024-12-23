import re
from typing import Dict, Optional

from favie_data_common.common.common_utils import CommonUtils

from favie_data_schema.favie.data.interface.product.favie_product import ReviewSummary
from favie_data_schema.favie.data.interface.product.favie_product_detail import FavieProductDetail
from favie_data_schema.favie.data.interface.product.favie_product_review import FavieProductReview


class FavieProductUtils:
    @staticmethod
    def gen_f_sku_id(product: FavieProductDetail):
        if not product:
            return None
        return FavieProductUtils.gen_f_id(id=product.sku_id, site=product.site)

    @staticmethod
    def gen_f_spu_id(product: FavieProductDetail):
        if product is None:
            return None
        spu_id = product.spu_id if product.spu_id else product.sku_id
        return FavieProductUtils.gen_f_id(id=spu_id, site=product.site)

    @staticmethod
    def gen_f_review_id(review: FavieProductReview):
        if review.site is None:
            return None
        review_id = (
            review.review_id
            if review.review_id
            else CommonUtils.md5_hash(f"{review.author_id}-{review.author_name}-{review.link}-{review.position}")
        )
        return FavieProductUtils.gen_f_id(id=review_id, site=review.site)

    @staticmethod
    def gen_f_id(*, id: str, site: str):
        return f"{id}-{site}" if id and site else None

    # @staticmethod
    # def get_product_price(product):
    #     return product.get("product_price")

    # @staticmethod
    # def get_product_image_url(product):
    #     return product.get("product_image_url")

    # @staticmethod
    # def get_product_url(product):
    #     return product.get("product_url")

    # @staticmethod
    # def check_product(product: FavieProductDetail):
    #     if product is None:
    #         return False

    #     if (product.link is None or product.f_sku_id is None) and (product.sku_id is None or product.site is None):
    #         return False

    #     return True

    @staticmethod
    def cal_percentage_to_review_summary(review_summary: Optional[ReviewSummary]) -> Optional[ReviewSummary]:
        """
        Calculate percentage for each star rating in the review summary.

        :param review_summary: The review summary object containing rating breakdown.
        :return: Updated review summary with calculated percentages, or None if input is None.
        """
        if review_summary is None or review_summary.rating_breakdown is None:
            return review_summary

        rb = review_summary.rating_breakdown
        star_counts: Dict[str, int] = {
            "five": rb.five_star or 0,
            "four": rb.four_star or 0,
            "three": rb.three_star or 0,
            "two": rb.two_star or 0,
            "one": rb.one_star or 0,
        }

        ratings_total = sum(star_counts.values())

        if ratings_total > 0:
            percentages = {star: int(round(count / ratings_total * 100)) for star, count in star_counts.items()}

            # Adjust to ensure sum is 100%
            diff = 100 - sum(percentages.values())
            if diff != 0:
                max_star = max(star_counts, key=star_counts.get)
                percentages[max_star] += diff

            rb.five_percentage = percentages["five"]
            rb.four_percentage = percentages["four"]
            rb.three_percentage = percentages["three"]
            rb.two_percentage = percentages["two"]
            rb.one_percentage = percentages["one"]
        else:
            rb.five_percentage = rb.four_percentage = rb.three_percentage = rb.two_percentage = rb.one_percentage = None

        return review_summary

    @staticmethod
    def extract_currency_and_amount(text):
        currency_info = {
            "USD": "$",
            "EUR": "€",
            "GBP": "£",
            "JPY": "¥",
            "CNY": "¥",
            "CAD": "$",
            "AUD": "$",
            "CHF": "CHF",
            "SGD": "$",
            "HKD": "$",
            "NZD": "$",
            "SEK": "kr",
            "NOK": "kr",
            "DKK": "kr",
            "INR": "₹",
            "KRW": "₩",
            "RUB": "₽",
            "ZAR": "R",
            "BRL": "R$",
            "MXN": "$",
        }
        try:
            # 创建正则表达式模式，优先匹配货币代码
            codes = "|".join(currency_info.keys())
            symbols = "|".join(re.escape(sym) for sym in set(currency_info.values()))
            pattern = rf"\b({codes})\s*([\d.,]+)\s*|\s*([\d.,]+)\s*({codes})\b|\s*({symbols})\s*([\d.,]+)\s*|\s*([\d.,]+)\s*({symbols})\s*"

            match = re.search(pattern, text, re.IGNORECASE)

            if match:
                groups = match.groups()
                if groups[0]:  # 货币代码在前
                    code, amount_str = groups[0], groups[1]
                elif groups[3]:  # 货币代码在后
                    code, amount_str = groups[3], groups[2]
                elif groups[4]:  # 货币符号在前
                    symbol, amount_str = groups[4], groups[5]
                    code = next((code for code, sym in currency_info.items() if sym == symbol), None)
                elif groups[7]:  # 货币符号在后
                    symbol, amount_str = groups[7], groups[6]
                    code = next((code for code, sym in currency_info.items() if sym == symbol), None)
                else:
                    return None, None

                # 处理金额中的逗号和点
                amount_str = amount_str.replace(",", "")
                amount = float(amount_str)

                return code.upper() if code else None, amount
            else:
                return None, None
        except Exception:
            return None, None

import logging


class ReviewSummaryGenerator:
    @staticmethod
    def gen_url(sku_id: str) -> str:
        pass


class AmazonReviewSummaryGenerator(ReviewSummaryGenerator):
    @staticmethod
    def gen_url(sku_id: str) -> str:
        return f"https://www.amazon.com/product-reviews/{sku_id}"


class ReviewSummaryGeneratorProxy:
    config = {"amazon.com": AmazonReviewSummaryGenerator}

    @staticmethod
    def gen_url(site: str, sku_id: str):
        try:
            generator = ReviewSummaryGeneratorProxy.config.get(site)
            if generator:
                return generator.gen_url(sku_id)
        except Exception:
            logging.exception("gen_url exception : site = %s , sku_id = %s", site, sku_id)
            return None

from favie_common.common.common_utils import CommonUtils

from favie_data_schema.favie.data.interface.product.favie_product import FavieProductDetail, FavieProductReview


class FavieProductUtils:
    @staticmethod
    def gen_f_sku_id(product: FavieProductDetail):
        if product is None:
            return None
        return FavieProductUtils.gen_f_id(id=product.sku_id, site=product.site)

    @staticmethod
    def gen_f_spu_id(product: FavieProductDetail):
        if product is None:
            return None
        spu_id = product.spu_id if product.spu_id is not None else product.sku_id
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
        if CommonUtils.any_none(id, site):
            return None
        return f"{id}-{site}"

    @staticmethod
    def get_product_price(product):
        return product.get("product_price")

    @staticmethod
    def get_product_image_url(product):
        return product.get("product_image_url")

    @staticmethod
    def get_product_url(product):
        return product.get("product_url")

    @staticmethod
    def check_product(product: FavieProductDetail):
        if product is None:
            return False

        if product.f_sku_id is None and (product.sku_id is None or product.site is None):
            return False

        return True

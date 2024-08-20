from favie_data_schema.favie.adapter.common.common_utils import CommonUtils
from favie_data_schema.favie.data.interface.product.favie_product import FavieProduct
from favie_data_schema.favie.data.interface.product.favie_review import FavieReview

class FavieProductUtils():    
    @staticmethod
    def gen_f_sku_id(product:FavieProduct):
        if(product is None):
            return None
        if(CommonUtils.all_not_none(product.sku_id,product.site)):
            return f"{product.sku_id}-{product.site}"
        return None

    @staticmethod
    def gen_f_spu_id(product: FavieProduct):
        if(product is None):
            return None
        spu_id = product.spu_id if product.spu_id is not None else product.sku_id
        if(CommonUtils.all_not_none(spu_id,product.site)):
            return f"{spu_id}-{product.site}"
        
    @staticmethod
    def gen_review_id(spu_id: str, review: FavieReview):
        if(CommonUtils.any_none(spu_id,review.review_id)):
            return None
        review_id = review.review_id if review.review_id is not None else CommonUtils.md5_hash(f'{review.author_id}-{review.author_name}-{review.link}-{review.position}')
        return f"{spu_id}-{review_id}"
    
    @staticmethod
    def get_product_price(product):
        return product.get('product_price')

    @staticmethod
    def get_product_image_url(product):
        return product.get('product_image_url')

    @staticmethod
    def get_product_url(product):
        return product.get('product_url')
    
    @staticmethod
    def check_product(product: FavieProduct):
        if product is None:
            return False
        
        if product.f_sku_id is None and (product.sku_id is None or product.site is None):
            return False
        
        return True
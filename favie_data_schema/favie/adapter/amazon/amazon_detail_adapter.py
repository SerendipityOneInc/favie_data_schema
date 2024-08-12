from favie_data_schema.favie.data.interface.product.favie_product import *
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_detail import RainforestProductDetail
from favie_data_schema.favie.adapter.common.currency import CurrencyConverter
from favie_data_schema.favie.adapter.common.favie_product_status import FavieProductStatus
from favie_data_schema.favie.adapter.common.crawler_kakfa_message import CrawlerKafkaMessage
from favie_data_schema.favie.adapter.common.common_utils import CommonUtils
from favie_data_schema.favie.adapter.data_mock.amazon_message_read import read_amazon_message
from datetime import datetime
import logging

class AmazoneDetailAdapter:
    def __init__(self):
        pass

    @staticmethod
    def convert_to_favie_product(amazon_message: CrawlerKafkaMessage) -> FavieProduct:
        rainforest_product_detail = amazon_message.crawl_result
        if not AmazoneDetailAdapter.rainforest_product_detail_check(rainforest_product_detail):
            logging.error("rainforest_product_detail is invalid: %s", rainforest_product_detail)
            return None
        favie_product = FavieProduct()
        favie_product.sku_id = rainforest_product_detail.product.asin
        favie_product.spu_id = rainforest_product_detail.product.parent_asin
        favie_product.site = CommonUtils.host_trip_www(amazon_message.host)
        favie_product.title = rainforest_product_detail.product.title
        favie_product.link = rainforest_product_detail.product.link
        favie_product.sub_title = rainforest_product_detail.product.sub_title.text if rainforest_product_detail.product.sub_title is not None else None
        favie_product.sub_title_link = rainforest_product_detail.product.sub_title.link if rainforest_product_detail.product.sub_title is not None else None
        favie_product.description = rainforest_product_detail.product.description
        favie_product.description_external_link = None
        favie_product.rich_product_description = None
        favie_product.price = AmazoneDetailAdapter.get_price(rainforest_product_detail)
        favie_product.rrp = AmazoneDetailAdapter.get_rrp(rainforest_product_detail)
        favie_product.images = AmazoneDetailAdapter.get_images(rainforest_product_detail)
        favie_product.f_images = None
        favie_product.videos = AmazoneDetailAdapter.get_videos(rainforest_product_detail)
        favie_product.categories = AmazoneDetailAdapter.get_categories(rainforest_product_detail)
        favie_product.f_categories = None
        favie_product.brand = AmazoneDetailAdapter.get_brand(rainforest_product_detail)
        favie_product.f_brand = None
        favie_product.feature_bullets = rainforest_product_detail.product.feature_bullets        
        favie_product.attributes = AmazoneDetailAdapter.get_attributes(rainforest_product_detail)
        favie_product.specifications = AmazoneDetailAdapter.get_specifications(rainforest_product_detail)
        favie_product.standard_attributes = AmazoneDetailAdapter.get_standard_attributes(rainforest_product_detail)
        favie_product.offers = None
        favie_product.seller = AmazoneDetailAdapter.get_seller(rainforest_product_detail)
        favie_product.inventory = None
        favie_product.keywords = rainforest_product_detail.product.keywords
        favie_product.search_alias = None
        favie_product.deal = AmazoneDetailAdapter.get_deal(rainforest_product_detail)
        favie_product.shipping = None
        favie_product.fulfillment = None
        favie_product.returns_policy = None
        favie_product.variants = None
        favie_product.promotion = AmazoneDetailAdapter.get_promotion(rainforest_product_detail)
        favie_product.f_meta = MetaInfo(
            source_type = str(amazon_message.source),
            parser_name = f"{amazon_message.parser_name}-adapter",
            parses_at = str(int(datetime.now().timestamp()))
        )
        favie_product.f_status = FavieProductStatus.SKU_NORMAL.name
        return favie_product

    @staticmethod
    def get_best_seller_rank(rainforest_product_detail: RainforestProductDetail):
        if rainforest_product_detail.product.bestsellers_rank is not None and len(rainforest_product_detail.product.bestsellers_rank) > 0:
            ranks = [SellerRank(
                category = x.category,
                rank = x.rank,
                link = x.link
                ) for x in rainforest_product_detail.product.bestsellers_rank if CommonUtils.all_not_none(x.category,x.rank)]
            return ranks if len(ranks) > 0 else None
        return None

    @staticmethod
    def get_promotion(rainforest_product_detail: RainforestProductDetail):
        if rainforest_product_detail.product.promotions is not None and len(rainforest_product_detail.product.promotions) > 0:
            promotion = Promotion(why_buy=[x.name for x in rainforest_product_detail.product.promotions if x.name is not None])
            return promotion if len(promotion.why_buy) > 0 else None
        return None

    @staticmethod
    def get_variants(rainforest_product_detail: RainforestProductDetail):
        if(rainforest_product_detail.product.variants is not None and len(rainforest_product_detail.product.variants) > 0): 
            variants = [SimpleProduct(
                    sku_id=x.asin,
                    title=None, #variants 的schema定义有误，缺少title字段，多了一个text字段
                    link=x.link,
                    price=AmazoneDetailAdapter.convert_price(x.price)
                ) for x in rainforest_product_detail.product.variants if x.asin is not None]
            return variants if len(variants) > 0 else None
        return None
    
    @staticmethod
    def convert_price(amazon_price)->Price:
        if amazon_price is None:
            return None
        currency_converter = CurrencyConverter(amazon_price.currency,amazon_price.value)
        price = Price(
                currency=currency_converter.get_currency_code(),
                value = currency_converter.get_subunit_value(),
                updates_at=str(int(datetime.now().timestamp()))
            )
        return price if CommonUtils.all_not_none(price.currency,price.value) else None

    @staticmethod
    def get_deal(rainforest_product_detail: RainforestProductDetail):
        if(rainforest_product_detail.product.buybox_winner is not None and rainforest_product_detail.product.buybox_winner.deal is not None):
            was_price = AmazoneDetailAdapter.convert_price(rainforest_product_detail.product.buybox_winner.price)
            if(was_price is None):
                return None
            
            claimed = rainforest_product_detail.product.buybox_winner.deal.claimed
            percentage = claimed.percentage if claimed is not None else None
            if(percentage is None):
                return None
            
            deal_price = Price(
                    currency=was_price.currency,
                    value = int(was_price.value * percentage / 100),
                    updates_at=str(int(datetime.now().timestamp()))
            )
            return Deal(
                was_price = was_price,
                deal_price = deal_price ,
                description = rainforest_product_detail.product.buybox_winner.deal.claimed.raw,
                ends_at= rainforest_product_detail.product.buybox_winner.deal.timing.ends_at
            )
        return None
    
    @staticmethod
    def get_seller(rainforest_product_detail: RainforestProductDetail):
        if(rainforest_product_detail.product.buybox_winner is not None):
            return Seller(
                id=rainforest_product_detail.product.buybox_winner.offer_id
          )
        return None
    
    @staticmethod
    def get_standard_attributes(rainforest_product_detail: RainforestProductDetail):
        return None
    
    @staticmethod
    def get_specifications(rainforest_product_detail: RainforestProductDetail):
        if rainforest_product_detail.product.specifications is not None and len(rainforest_product_detail.product.specifications) > 0:
            specifications = [AttributeItem(
                name = x.name,
                value = x.value
            ) for x in rainforest_product_detail.product.specifications if CommonUtils.all_not_none(x.name,x.value)]
            return specifications if len(specifications) > 0 else None
        return None
    
    @staticmethod
    def get_attributes(rainforest_product_detail: RainforestProductDetail):
        if rainforest_product_detail.product.attributes is not None and len(rainforest_product_detail.product.attributes) > 0:
            attributes = [AttributeItem(
                name = x.name,
                value = x.value
            ) for x in rainforest_product_detail.product.attributes if CommonUtils.all_not_none(x.name,x.value)] 
            return attributes if len(attributes) > 0 else None
        return None
    
    @staticmethod
    def get_brand(rainforest_product_detail: RainforestProductDetail):
        if rainforest_product_detail.product.brand is not None:
            return Brand(
                name = rainforest_product_detail.product.brand
            )
        return None
    
    @staticmethod
    def get_categories(rainforest_product_detail: RainforestProductDetail):
        if rainforest_product_detail.product.categories is not None and len(rainforest_product_detail.product.categories) > 0:
            categories = [ CategoryItem(
                id = x.category_id,
                name = x.name,
                ) for x in rainforest_product_detail.product.categories if x.category_id is not None]
            return categories if len(categories) > 0 else None
        return None

    @staticmethod
    def get_price(rainforest_product_detail: RainforestProductDetail):
        if rainforest_product_detail.product.buybox_winner is not None:
            return AmazoneDetailAdapter.convert_price(rainforest_product_detail.product.buybox_winner.price)
        return None
    
    @staticmethod
    def get_rrp(rainforest_product_detail: RainforestProductDetail):
        if rainforest_product_detail.product.buybox_winner is not None:
            return AmazoneDetailAdapter.convert_price(rainforest_product_detail.product.buybox_winner.rrp)
        return None
    
    @staticmethod
    def get_images(rainforest_product_detail: RainforestProductDetail):
        if rainforest_product_detail.product.images is not None or rainforest_product_detail.product.main_image is not None:
            images = Images(
                main_image = rainforest_product_detail.product.main_image.link if rainforest_product_detail.product.main_image is not None else None,
                images = [x.link for x in rainforest_product_detail.product.images if x.link is not None]
            )
            return images if images.main_image is not None or len(images.image_list) > 0 else None
        return None
    
    @staticmethod
    def get_videos(rainforest_product_detail: RainforestProductDetail):
        if rainforest_product_detail.product.videos is not None and len(rainforest_product_detail.product.videos) > 0:
            videos = [
                Video(
                    link = x.url,
                    title = x.title,
                    duration_seconds= x.duration_seconds,
                    thumbnail = x.thumbnail,
                    height= x.height,
                    width= x.width,
                    is_hero_video= x.is_hero_video
                ) 
                for x in rainforest_product_detail.product.videos
                if x.url is not None    
            ]
            return videos if len(videos) > 0 else None
        return None
    
    @staticmethod
    def rainforest_product_detail_check(rainforest_product_detail: RainforestProductDetail) -> bool:
        if rainforest_product_detail is None:
            return False
        if rainforest_product_detail.product is None:
            return False
        return True
        
def main():
    amazon_message = read_amazon_message("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/amazon_message.json")
    favie_product = AmazoneDetailAdapter.convert_to_favie_product(amazon_message)
    print(favie_product.model_dump_json(exclude_none = True) if favie_product else None)


if __name__ == "__main__":
    main()
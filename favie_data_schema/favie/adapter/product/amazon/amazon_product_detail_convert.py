from lxml import html
import re
from favie_data_schema.favie.adapter.product.common.currency import CurrencyConverter
from favie_data_schema.favie.adapter.product.common.favie_product_detail_status import FavieProductDetailStatus
from favie_data_schema.favie.adapter.product.common.favie_product_utils import FavieProductUtils
from favie_data_schema.favie.adapter.product.common.product_crawler_message import ProductDetailCrawlerMessage
from favie_data_schema.favie.data.interface.product.favie_product import *
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_detail import RainforestProductDetail
from favie_data_common.common.common_utils import CommonUtils
from favie_data_schema.favie.adapter.tools.data_mock_read import read_object
from favie_data_schema.favie.adapter.common.html_utils import HtmlUtils
from datetime import datetime
import time
from favie_data_schema.favie.data.crawl_data.crawler.common import Source
from favie_data_schema.favie.data.interface.product.product_enum import DataType
import logging

class AmazonProductDetailConvert():
    @staticmethod
    def convert_to_favie_product(amazon_message: ProductDetailCrawlerMessage) -> FavieProductDetail:
        crawl_result = amazon_message.crawl_result
        raw_result = amazon_message.raw_result
        
        if not AmazonProductDetailConvert.rainforest_product_detail_check(crawl_result):
            logging.error("rainforest_product_detail is invalid: %s", crawl_result)
            return None
        parse_time = AmazonProductDetailConvert.get_parse_time(amazon_message)
        favie_product = FavieProductDetail()
        favie_product.sku_id = crawl_result.product.asin
        favie_product.spu_id = crawl_result.product.parent_asin
        favie_product.site = CommonUtils.get_domain(amazon_message.host)
        favie_product.title = crawl_result.product.title
        favie_product.link = crawl_result.product.link
        favie_product.spu_title = crawl_result.product.title_excluding_variant_name
        favie_product.sub_title = crawl_result.product.sub_title.text if crawl_result.product.sub_title is not None else None
        favie_product.sub_title_link = crawl_result.product.sub_title.link if crawl_result.product.sub_title is not None else None
        favie_product.description = crawl_result.product.description
        favie_product.description_external_link = None
        favie_product.rich_product_description = None
        favie_product.price = AmazonProductDetailConvert.get_price(crawl_result,parse_time)
        favie_product.rrp = AmazonProductDetailConvert.get_rrp(crawl_result,parse_time)
        favie_product.images = AmazonProductDetailConvert.get_images(crawl_result)
        favie_product.f_images = None
        favie_product.videos = AmazonProductDetailConvert.get_videos(crawl_result)
        favie_product.categories = AmazonProductDetailConvert.get_categories(crawl_result)
        favie_product.f_categories = None
        favie_product.brand = AmazonProductDetailConvert.get_brand(crawl_result)
        favie_product.f_brand = None
        favie_product.feature_bullets = crawl_result.product.feature_bullets        
        favie_product.attributes = AmazonProductDetailConvert.get_attributes(crawl_result)
        favie_product.specifications = AmazonProductDetailConvert.get_specifications(crawl_result)
        favie_product.standard_attributes = AmazonProductDetailConvert.get_standard_attributes(amazon_message)
        favie_product.offers = None
        favie_product.seller = AmazonProductDetailConvert.get_seller(crawl_result)
        favie_product.inventory = None
        favie_product.keywords = crawl_result.product.keywords
        favie_product.search_alias = None
        favie_product.deal = AmazonProductDetailConvert.get_deal(crawl_result,parse_time)
        favie_product.shipping = None
        favie_product.fulfillment = None
        favie_product.returns_policy = None
        favie_product.variants = None
        favie_product.f_sku_id = FavieProductUtils.gen_f_sku_id(favie_product)
        favie_product.f_spu_id = FavieProductUtils.gen_f_spu_id(favie_product)
        favie_product.promotion = AmazonProductDetailConvert.get_promotion(crawl_result)
        favie_product.best_seller_rank = AmazonProductDetailConvert.get_best_seller_rank(crawl_result)
        favie_product.variants = AmazonProductDetailConvert.get_variants(crawl_result,parse_time)
        favie_product.f_meta = MetaInfo(
            source_type = str(amazon_message.source),
            parser_name = f"{amazon_message.parser_name}-adapter",
            data_type= str(DataType.PRODUCT_DETAIL.value),
            parses_at = parse_time
        )
        favie_product.f_status = FavieProductDetailStatus.SKU_NORMAL.name
        return favie_product
    

    @staticmethod
    def get_parse_time(message: ProductDetailCrawlerMessage):    
        try:
            return str(int(CommonUtils.datetime_string_to_timestamp(message.update_time)))
        except Exception as e:
            logging.exception("get_parse_time error: %s", message.model_dump_json(exclude_none=True))
            return str(int(datetime.now().timestamp()))        

    @staticmethod
    def get_best_seller_rank(rainforest_product_detail: RainforestProductDetail):
        if CommonUtils.list_len(rainforest_product_detail.product.bestsellers_rank) > 0:
            ranks = [SellerRank(
                category = x.category,
                rank = x.rank,
                link = x.link
                ) for x in rainforest_product_detail.product.bestsellers_rank if CommonUtils.all_not_none(x.category,x.rank)]
            return ranks if CommonUtils.list_len(ranks) > 0 else None
        return None

    @staticmethod
    def get_promotion(rainforest_product_detail: RainforestProductDetail):
        if CommonUtils.list_len(rainforest_product_detail.product.promotions) > 0:
            promotion = Promotion(why_buy=[x.name for x in rainforest_product_detail.product.promotions if x.name is not None])
            return promotion if CommonUtils.list_len(promotion.why_buy) > 0 else None
        return None

    @staticmethod
    def get_variants(rainforest_product_detail: RainforestProductDetail,parse_time:str):
        if(CommonUtils.list_len(rainforest_product_detail.product.variants) > 0): 
            variants = [SimpleProduct(
                    sku_id=x.asin,
                    title=None, #variants 的schema定义有误，缺少title字段，多了一个text字段
                    link=x.link,
                    price=AmazonProductDetailConvert.convert_price(x.price,parse_time)
                ) for x in rainforest_product_detail.product.variants if x.asin is not None]
            return variants if CommonUtils.list_len(variants) > 0 else None
        return None
    
    @staticmethod
    def convert_price(amazon_price,parse_time)->Price:
        if amazon_price is None:
            return None
        currency_converter = CurrencyConverter(amazon_price.currency,amazon_price.value)
        price = Price(
                currency=currency_converter.get_currency_code(),
                value = currency_converter.get_subunit_value(),
                updates_at=parse_time
            )
        return price if CommonUtils.all_not_none(price.currency,price.value) else None

    @staticmethod
    def get_deal(rainforest_product_detail: RainforestProductDetail,parse_time:str):
        if(rainforest_product_detail.product.buybox_winner is not None and rainforest_product_detail.product.buybox_winner.deal is not None):
            was_price = AmazonProductDetailConvert.convert_price(rainforest_product_detail.product.buybox_winner.price,parse_time)
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
            timing = rainforest_product_detail.product.buybox_winner.deal.timing
            return Deal(
                was_price = was_price,
                deal_price = deal_price ,
                description = rainforest_product_detail.product.buybox_winner.deal.claimed.raw,
                ends_at= timing.ends_at if timing is not None else None
            )
        return None
    
    @staticmethod
    def get_seller(rainforest_product_detail: RainforestProductDetail):
        if(rainforest_product_detail.product.buybox_winner is not None):
            return Seller(
                id=rainforest_product_detail.product.buybox_winner.offer_id
            ) if rainforest_product_detail.product.buybox_winner.offer_id else None
        return None
    
    @staticmethod
    def get_standard_attributes(message : ProductDetailCrawlerMessage):
        try:
            standard_attributes = StandardAttributes()
            if message.source == Source.SPIDER.value:
                standard_attributes.last_month_sell_amount = AmazonProductDetailConvert.get_last_month_sell_amount(message.raw_result)
            standard_attributes.is_bundle = message.crawl_result.product.is_bundle
            standard_attributes.has_coupon = message.crawl_result.product.has_coupon
            standard_attributes.coupon_text = message.crawl_result.product.coupon_text
            standard_attributes.platform_choice = AmazonProductDetailConvert.get_platform_choice(message.crawl_result)
            
            if message.crawl_result.product.buybox_winner is not None: 
                if message.crawl_result.product.buybox_winner.fulfillment is not None:
                    standard_attributes.is_marketplace_item = message.crawl_result.product.buybox_winner.fulfillment.is_sold_by_third_party
                standard_attributes.is_member = message.crawl_result.product.buybox_winner.is_prime
                standard_attributes.is_member_exclusive_deal = message.crawl_result.product.buybox_winner.is_prime_exclusive_deal
            return standard_attributes
        except Exception as e:
            logging.warn("get_standard_attributes error: %s-%s",message.product_id,message.host)
            return None
        
    
    @staticmethod
    def get_platform_choice(rainforest_product_detail: RainforestProductDetail):
        if rainforest_product_detail.product.amazons_choice is not None:
            return PlatformChoice(
                keywords=rainforest_product_detail.product.amazons_choice.keywords,
                link=rainforest_product_detail.product.amazons_choice.link
            )
        return None
    
    @staticmethod
    def get_last_month_sell_amount(encoded_html_content):
        """从 HTML 内容中提取 XPath 内容"""
        try:
            html_content = HtmlUtils.decode_and_decompress_html(encoded_html_content)
            tree = html.fromstring(html_content)
            element = tree.xpath('//*[@id="social-proofing-faceout-title-tk_bought"]/span')
            if element:
                text = element[0].text_content()
                # 使用正则表达式提取数量部分
                match = re.match(r"(\d+(\.\d+)?[KM]?)", text)
                if match:
                    number_str = match.group(1)
                    if "K" in number_str:
                        number = float(number_str.replace("K", "")) * 1_000
                    elif "M" in number_str:
                        number = float(number_str.replace("M", "")) * 1_000_000
                    else:
                        number = float(number_str)
                    return int(number)
                return None
            else:
                return None
        except Exception:
            return None
    
    @staticmethod
    def get_specifications(rainforest_product_detail: RainforestProductDetail):
        if CommonUtils.list_len(rainforest_product_detail.product.specifications) > 0:
            specifications = [AttributeItem(
                name = x.name,
                value = x.value
            ) for x in rainforest_product_detail.product.specifications if CommonUtils.all_not_none(x.name,x.value)]
            return specifications if CommonUtils.list_len(specifications) > 0 else None
        return None
    
    @staticmethod
    def get_attributes(rainforest_product_detail: RainforestProductDetail):
        if CommonUtils.list_len(rainforest_product_detail.product.attributes) > 0:
            attributes = [AttributeItem(
                name = x.name,
                value = x.value
            ) for x in rainforest_product_detail.product.attributes if CommonUtils.all_not_none(x.name,x.value)] 
            return attributes if CommonUtils.list_len(attributes) > 0 else None
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
        if CommonUtils.list_len(rainforest_product_detail.product.categories) > 0:
            categories = [ CategoryItem(
                id = x.category_id,
                name = x.name,
                ) for x in rainforest_product_detail.product.categories if (x.name is not None and x.name.strip() != "All Departments") or x.name is None]
            return categories if CommonUtils.list_len(categories) > 0 else None
        return None

    @staticmethod
    def get_price(rainforest_product_detail: RainforestProductDetail,parse_time:str):
        if rainforest_product_detail.product.buybox_winner is not None:
            return AmazonProductDetailConvert.convert_price(rainforest_product_detail.product.buybox_winner.price,parse_time)
        return None
    
    @staticmethod
    def get_rrp(rainforest_product_detail: RainforestProductDetail,parse_time:str):
        if rainforest_product_detail.product.buybox_winner is not None:
            return AmazonProductDetailConvert.convert_price(rainforest_product_detail.product.buybox_winner.rrp,parse_time)
        return None
    
    @staticmethod
    def get_images(rainforest_product_detail: RainforestProductDetail):
        if rainforest_product_detail.product.images is not None or rainforest_product_detail.product.main_image is not None:
            images = Images(
                main_image = rainforest_product_detail.product.main_image.link if rainforest_product_detail.product.main_image is not None else None,
                images = [x.link for x in rainforest_product_detail.product.images if x.link is not None] if rainforest_product_detail.product.images is not None else None
            )
            return images if images.main_image is not None or CommonUtils.list_len(images.image_list) > 0 else None
        return None
    
    @staticmethod
    def get_videos(rainforest_product_detail: RainforestProductDetail):
        if CommonUtils.list_len(rainforest_product_detail.product.videos) > 0:
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
            return videos if CommonUtils.list_len(videos) > 0 else None
        return None
    
    @staticmethod
    def rainforest_product_detail_check(rainforest_product_detail: RainforestProductDetail) -> bool:
        if rainforest_product_detail is None:
            return False
        if rainforest_product_detail.product is None:
            return False
        return True
        
def main():
    amazon_message = read_object("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/amozon_message_source_1.json",ProductDetailCrawlerMessage)
    favie_product = AmazonProductDetailConvert.convert_to_favie_product(amazon_message)
    print(favie_product.model_dump_json(exclude_none = True) if favie_product else None)

if __name__ == "__main__":
    main()
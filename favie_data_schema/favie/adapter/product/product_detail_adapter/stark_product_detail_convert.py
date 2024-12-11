import logging
import re
from datetime import datetime

from favie_data_common.common.common_utils import CommonUtils
from lxml import html

from favie_data_schema.favie.adapter.common.html_utils import HtmlUtils
from favie_data_schema.favie.adapter.common.stark_message import StarkProductDetailMessage
from favie_data_schema.favie.adapter.common.stark_message_utils import StarkMessageUtils
from favie_data_schema.favie.adapter.product.common.currency import CurrencyConverter
from favie_data_schema.favie.adapter.product.common.favie_product_utils import FavieProductUtils
from favie_data_schema.favie.data.crawl_data.crawler.common import Source
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_detail import (
    RainforestProductDetail,
    Variants,
)
from favie_data_schema.favie.data.interface.common.favie_enum import FavieDataStatus, MessageDataType
from favie_data_schema.favie.data.interface.common.favie_model import MetaInfo
from favie_data_schema.favie.data.interface.product.favie_product import (
    AttributeItem,
    Brand,
    CategoryItem,
    Deal,
    ExtendedInfo,
    Images,
    PlatformChoice,
    Price,
    Promotion,
    Seller,
    SellerRank,
    SimpleProduct,
    Video,
)
from favie_data_schema.favie.data.interface.product.favie_product_detail import FavieProductDetail


class HashableAttributeItem(AttributeItem):
    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


class StarkProductDetailConvert:
    @staticmethod
    def convert_to_favie_product(stark_detail_message: StarkProductDetailMessage) -> FavieProductDetail:
        crawl_result = stark_detail_message.crawl_result
        stark_detail_message.raw_result

        if not StarkProductDetailConvert.rainforest_product_detail_check(crawl_result):
            logging.error("rainforest_product_detail is invalid: %s", crawl_result)
            return None
        parse_time = StarkMessageUtils.get_parse_time(stark_detail_message)
        favie_product = FavieProductDetail()
        favie_product.sku_id = crawl_result.product.asin
        favie_product.spu_id = crawl_result.product.parent_asin
        favie_product.site = StarkMessageUtils.get_domain(stark_detail_message)
        favie_product.title = crawl_result.product.title
        favie_product.link = crawl_result.product.link
        # favie_product.spu_title = crawl_result.product.title_excluding_variant_name
        favie_product.sub_title = (
            crawl_result.product.sub_title.text if crawl_result.product.sub_title is not None else None
        )
        favie_product.sub_title_link = (
            crawl_result.product.sub_title.link if crawl_result.product.sub_title is not None else None
        )
        favie_product.description = crawl_result.product.description
        favie_product.description_external_link = None
        favie_product.rich_product_description = None
        price = StarkProductDetailConvert.get_price(stark_detail_message, parse_time)
        favie_product.price = price
        rrp = StarkProductDetailConvert.get_rrp(stark_detail_message, parse_time)
        favie_product.rrp = rrp if rrp else price
        favie_product.images = StarkProductDetailConvert.get_images(crawl_result)
        favie_product.f_images = None
        favie_product.videos = StarkProductDetailConvert.get_videos(crawl_result)
        favie_product.categories = StarkProductDetailConvert.get_categories(crawl_result)
        favie_product.f_categories = None
        favie_product.brand = StarkProductDetailConvert.get_brand(crawl_result)
        favie_product.f_brand = None
        favie_product.feature_bullets = crawl_result.product.feature_bullets
        favie_product.attributes = StarkProductDetailConvert.get_attributes(crawl_result)
        favie_product.specifications = StarkProductDetailConvert.get_specifications(crawl_result)
        favie_product.extended_info = StarkProductDetailConvert.get_extended_info(stark_detail_message)
        # favie_product.offers = None
        favie_product.seller = StarkProductDetailConvert.get_seller(crawl_result)
        favie_product.inventory = None
        favie_product.keywords = crawl_result.product.keywords
        # favie_product.search_alias = None
        favie_product.deal = StarkProductDetailConvert.get_deal(stark_detail_message, parse_time)
        # favie_product.shipping = None
        # favie_product.fulfillment = None
        favie_product.returns_policy = None
        favie_product.f_sku_id = FavieProductUtils.gen_f_sku_id(favie_product)
        favie_product.f_spu_id = FavieProductUtils.gen_f_spu_id(favie_product)
        favie_product.promotion = StarkProductDetailConvert.get_promotion(crawl_result)
        favie_product.best_seller_rank = StarkProductDetailConvert.get_best_seller_rank(crawl_result)
        favie_product.variants = StarkProductDetailConvert.get_variants(stark_detail_message, parse_time)
        favie_product.f_meta = MetaInfo(
            source_type=str(stark_detail_message.source),
            parser_name=f"{stark_detail_message.parser_name}-adapter",
            data_type=str(MessageDataType.PRODUCT_DETAIL_CRAWLER.value),
            parses_at=parse_time,
            app_key=stark_detail_message.app_key,
        )
        favie_product.shop_id = crawl_result.product.stark_shop.id if crawl_result.product.stark_shop else None
        favie_product.shop_name = crawl_result.product.stark_shop.name if crawl_result.product.stark_shop else None
        favie_product.shop_site = (
            StarkMessageUtils.get_domain_by_url(crawl_result.product.stark_shop.host)
            if crawl_result.product.stark_shop
            else None
        )
        favie_product.link_in_shop = crawl_result.product.stark_link_in_shop
        favie_product.request_sku_id = stark_detail_message.product_id
        favie_product.f_status = str(FavieDataStatus.NORMAL.value)
        return favie_product

    @staticmethod
    def get_best_seller_rank(rainforest_product_detail: RainforestProductDetail):
        if CommonUtils.list_len(rainforest_product_detail.product.bestsellers_rank) > 0:
            ranks = [
                SellerRank(category=x.category, rank=x.rank, link=x.link)
                for x in rainforest_product_detail.product.bestsellers_rank
                if CommonUtils.all_not_none(x.category, x.rank)
            ]
            return ranks if CommonUtils.list_len(ranks) > 0 else None
        return None

    @staticmethod
    def get_promotion(rainforest_product_detail: RainforestProductDetail):
        if CommonUtils.list_len(rainforest_product_detail.product.promotions) > 0:
            promotion = Promotion(
                why_buy=[x.name for x in rainforest_product_detail.product.promotions if x.name is not None]
            )
            return promotion if CommonUtils.list_len(promotion.why_buy) > 0 else None
        return None

    @staticmethod
    def get_variants(stark_detail_message: StarkProductDetailMessage, parse_time: str):
        rainforest_product_detail = stark_detail_message.crawl_result
        if CommonUtils.list_len(rainforest_product_detail.product.variants) > 0:
            variants = [
                SimpleProduct(
                    sku_id=x.asin,
                    title=x.text,
                    link=x.link,
                    dimensions=StarkProductDetailConvert.get_dimensions(x),
                    price=StarkProductDetailConvert.convert_price(
                        rainforest_price=x.price,
                        source_type=stark_detail_message.source,
                        parser_name=stark_detail_message.parser_name,
                        parse_time=parse_time,
                    ),
                )
                for x in rainforest_product_detail.product.variants
                if x.asin is not None
            ]
            return variants if CommonUtils.list_len(variants) > 0 else None
        return None

    @staticmethod
    def convert_price(*, rainforest_price, source_type, parser_name, parse_time) -> Price:
        if rainforest_price is None:
            return None
        currency_converter = CurrencyConverter(rainforest_price.currency, rainforest_price.value)
        price = Price(
            currency=currency_converter.get_currency_code(),
            value=currency_converter.get_subunit_value(),
            parser_name=parser_name,
            source_type=str(source_type) if source_type else None,
            updates_at=parse_time,
        )
        return price if CommonUtils.all_not_none(price.currency, price.value) else None

    @staticmethod
    def get_deal(stark_detail_message: StarkProductDetailMessage, parse_time: str):
        rainforest_product_detail = stark_detail_message.crawl_result
        if (
            rainforest_product_detail.product.buybox_winner is not None
            and rainforest_product_detail.product.buybox_winner.deal is not None
        ):
            was_price = StarkProductDetailConvert.convert_price(
                rainforest_price=rainforest_product_detail.product.buybox_winner.price,
                source_type=stark_detail_message.source,
                parser_name=stark_detail_message.parser_name,
                parse_time=parse_time,
            )
            if was_price is None:
                return None

            claimed = rainforest_product_detail.product.buybox_winner.deal.claimed
            percentage = claimed.percentage if claimed is not None else None
            if percentage is None:
                return None

            deal_price = Price(
                currency=was_price.currency,
                value=int(was_price.value * percentage / 100),
                updates_at=str(int(datetime.now().timestamp())),
            )
            timing = rainforest_product_detail.product.buybox_winner.deal.timing
            return Deal(
                was_price=was_price,
                deal_price=deal_price,
                description=rainforest_product_detail.product.buybox_winner.deal.claimed.raw,
                ends_at=timing.ends_at if timing is not None else None,
            )
        return None

    @staticmethod
    def get_seller(rainforest_product_detail: RainforestProductDetail):
        if rainforest_product_detail.product.buybox_winner is not None:
            return (
                Seller(id=rainforest_product_detail.product.buybox_winner.offer_id)
                if rainforest_product_detail.product.buybox_winner.offer_id
                else None
            )
        return None

    @staticmethod
    def get_extended_info(message: StarkProductDetailMessage):
        try:
            extended_info = ExtendedInfo()
            if message.source == Source.SPIDER.value:
                extended_info.last_month_sell_amount = StarkProductDetailConvert.get_last_month_sell_amount(
                    message.raw_result
                )
            extended_info.is_bundle = message.crawl_result.product.is_bundle
            extended_info.has_coupon = message.crawl_result.product.has_coupon
            extended_info.coupon_text = message.crawl_result.product.coupon_text
            extended_info.platform_choice = StarkProductDetailConvert.get_platform_choice(message.crawl_result)

            if message.crawl_result.product.buybox_winner is not None:
                if message.crawl_result.product.buybox_winner.fulfillment is not None:
                    extended_info.is_marketplace_item = (
                        message.crawl_result.product.buybox_winner.fulfillment.is_sold_by_third_party
                    )
            return extended_info
        except Exception:
            logging.warning("get_standard_attributes error: %s-%s", message.product_id, message.host)
            return None

    @staticmethod
    def get_platform_choice(rainforest_product_detail: RainforestProductDetail):
        if rainforest_product_detail.product.amazons_choice is not None:
            return PlatformChoice(
                keywords=rainforest_product_detail.product.amazons_choice.keywords,
                link=rainforest_product_detail.product.amazons_choice.link,
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
    def valid_attributes(items):
        return (
            (
                HashableAttributeItem(name=x.name, value=x.value)
                for x in items
                if CommonUtils.all_not_none(x.name, x.value)
            )
            if items
            else iter(())
        )

    @staticmethod
    def get_specifications(rainforest_product_detail: RainforestProductDetail):
        product = rainforest_product_detail.product
        specs = set(StarkProductDetailConvert.valid_attributes(product.attributes))
        specs.update(StarkProductDetailConvert.valid_attributes(product.specifications))
        return list(specs) if specs else None

    @staticmethod
    def get_dimensions(variants: Variants):
        demissions = set(StarkProductDetailConvert.valid_attributes(variants.dimensions))
        return list(demissions) if demissions else None

    @staticmethod
    def get_attributes(rainforest_product_detail: RainforestProductDetail):
        product = rainforest_product_detail.product
        attributes = set(StarkProductDetailConvert.valid_attributes(product.attributes))
        return list(attributes) if attributes else None

    @staticmethod
    def get_brand(rainforest_product_detail: RainforestProductDetail):
        if rainforest_product_detail.product.brand is not None:
            return Brand(name=rainforest_product_detail.product.brand)
        return None

    @staticmethod
    def get_categories(rainforest_product_detail: RainforestProductDetail):
        if CommonUtils.list_len(rainforest_product_detail.product.categories) > 0:
            categories = [
                CategoryItem(
                    id=x.category_id,
                    name=x.name,
                )
                for x in rainforest_product_detail.product.categories
                if (x.name is not None and x.name.strip() != "All Departments") or x.name is None
            ]
            return categories if CommonUtils.list_len(categories) > 0 else None
        return None

    @staticmethod
    def get_price(stark_detail_message: StarkProductDetailMessage, parse_time: str):
        rainforest_product_detail = stark_detail_message.crawl_result
        if rainforest_product_detail.product.buybox_winner is not None:
            return StarkProductDetailConvert.convert_price(
                rainforest_price=rainforest_product_detail.product.buybox_winner.price,
                source_type=stark_detail_message.source,
                parser_name=stark_detail_message.parser_name,
                parse_time=parse_time,
            )
        return None

    @staticmethod
    def get_rrp(stark_detail_message: StarkProductDetailMessage, parse_time: str):
        rainforest_product_detail = stark_detail_message.crawl_result
        if rainforest_product_detail.product.buybox_winner is not None:
            return StarkProductDetailConvert.convert_price(
                rainforest_price=rainforest_product_detail.product.buybox_winner.rrp,
                source_type=stark_detail_message.source,
                parser_name=stark_detail_message.parser_name,
                parse_time=parse_time,
            )
        return None

    @staticmethod
    def get_images(rainforest_product_detail: RainforestProductDetail):
        if (
            rainforest_product_detail.product.images is not None
            or rainforest_product_detail.product.main_image is not None
        ):
            images = Images(
                main_image=rainforest_product_detail.product.main_image.link
                if rainforest_product_detail.product.main_image is not None
                else None,
                images=[x.link for x in rainforest_product_detail.product.images if x.link is not None]
                if rainforest_product_detail.product.images is not None
                else None,
            )
            return images if images.main_image is not None or CommonUtils.list_len(images.images) > 0 else None
        return None

    @staticmethod
    def get_videos(rainforest_product_detail: RainforestProductDetail):
        if CommonUtils.list_len(rainforest_product_detail.product.videos) > 0:
            videos = [
                Video(
                    link=x.url,
                    title=x.title,
                    duration_seconds=x.duration_seconds,
                    thumbnail=x.thumbnail,
                    height=x.height,
                    width=x.width,
                    is_hero_video=x.is_hero_video,
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

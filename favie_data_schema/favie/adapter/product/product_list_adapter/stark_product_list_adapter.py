from favie_data_common.common.common_utils import CommonUtils

from favie_data_schema.favie.adapter.common.stark_enum import StarkProductDataType
from favie_data_schema.favie.adapter.common.stark_message import StarkProductListMessage
from favie_data_schema.favie.adapter.common.stark_message_utils import StarkMessageUtils
from favie_data_schema.favie.adapter.product.common.currency import CurrencyConverter
from favie_data_schema.favie.adapter.product.common.favie_product_adapter import FavieProductDetailAdapter
from favie_data_schema.favie.adapter.product.common.favie_product_utils import FavieProductUtils
from favie_data_schema.favie.adapter.tools.data_mock_read import read_object
from favie_data_schema.favie.data.crawl_data.crawler.common import Source
from favie_data_schema.favie.data.crawl_data.crawler.stark_product_list import Price as StarkPrice
from favie_data_schema.favie.data.crawl_data.crawler.stark_product_list import ProductListItem
from favie_data_schema.favie.data.interface.product.favie_product import *


class StarkProductListAdapter(FavieProductDetailAdapter):
    @staticmethod
    def stark_list_to_favie_details(message: StarkProductListMessage) -> Optional[List[FavieProductDetail]]:
        if message is None or message.crawl_result is None:
            return None

        stark_product_list = message.crawl_result.product_list
        if CommonUtils.list_len(stark_product_list) == 0:
            return None

        favie_product_list: List[ProductListItem] = []
        for stark_product_item in stark_product_list:
            favie_product = FavieProductDetail()
            parse_time = StarkMessageUtils.get_parse_time(message)
            favie_product.sku_id = stark_product_item.asin
            favie_product.site = StarkMessageUtils.get_domain(message)
            favie_product.title = stark_product_item.title
            favie_product.link = stark_product_item.link
            favie_product.price = StarkProductListAdapter.get_price(stark_product_item, parse_time)
            favie_product.rrp = StarkProductListAdapter.get_rrp(stark_product_item, parse_time)
            favie_product.images = StarkProductListAdapter.get_images(stark_product_item)
            favie_product.review_summary = StarkProductListAdapter.get_review_summary(stark_product_item)
            favie_product.f_meta = MetaInfo(
                source_type=Source.SPIDER,
                parser_name=message.parser_name,
                data_type=str(StarkProductDataType.PRODUCT_LIST.value),
                parses_at=parse_time,
            )
            favie_product_list.append(favie_product)
        return favie_product_list if CommonUtils.list_len(favie_product_list) > 0 else None

    @staticmethod
    def get_review_summary(stark_product_item: ProductListItem) -> ReviewSummary:
        return ReviewSummary(rating=stark_product_item.rating, ratings_total=stark_product_item.ratings_total)

    @staticmethod
    def get_images(stark_product_item: ProductListItem) -> Images:
        return Images(main_image=stark_product_item.image) if stark_product_item.image is not None else None

    @staticmethod
    def get_price(stark_product_item: ProductListItem, parse_time: str) -> Price:
        if CommonUtils.not_empty(stark_product_item.prices):
            # 优先使用primary_price,且优先取value
            primary_price = next(filter(lambda price: price.is_primary, stark_product_item.prices), None)
            favie_price = StarkProductListAdapter.convert_price(primary_price, parse_time)
            if favie_price:
                return favie_price

            # 其次使用asin_price,且优先取raw
            asin_price = next(
                filter(lambda price: price.asin == stark_product_item.asin, stark_product_item.prices), None
            )
            favie_price = StarkProductListAdapter.convert_price(asin_price, parse_time, raw_first=True)
            if favie_price:
                return favie_price

            # 再次从list中选取第一个可用的price
            for stark_price in stark_product_item.prices:
                favie_price = StarkProductListAdapter.convert_price(stark_price, parse_time)
                if favie_price:
                    return favie_price

        # 最后使用price字段
        return StarkProductListAdapter.convert_price(stark_product_item.price, parse_time)

    @staticmethod
    def get_rrp(stark_product_item: ProductListItem, parse_time: str) -> Price:
        if CommonUtils.not_empty(stark_product_item.prices):
            # 优先使用primary_price,且优先取value
            rrp_price = next(filter(lambda price: price.is_rrp, stark_product_item.prices), None)
            favie_price = StarkProductListAdapter.convert_price(rrp_price, parse_time)
            if favie_price:
                return favie_price

            # 其次使用asin_price,且优先取raw
            asin_price = next(
                filter(lambda price: price.asin == stark_product_item.asin, stark_product_item.prices), None
            )
            favie_price = StarkProductListAdapter.convert_price(asin_price, parse_time, raw_first=True)
            if favie_price:
                return favie_price

            # 再次从list中选取第一个可用的price
            for stark_price in stark_product_item.prices:
                favie_price = StarkProductListAdapter.convert_price(stark_price, parse_time)
                if favie_price:
                    return favie_price

        # 最后使用price字段
        return StarkProductListAdapter.convert_price(stark_product_item.rrp, parse_time)

    @staticmethod
    def convert_price(stark_price: StarkPrice, parse_time: str, raw_first: bool = False) -> Price:
        if stark_price is None:
            return None

        if stark_price.raw and (raw_first or CommonUtils.any_none(stark_price.currency, stark_price.value)):
            currency_code, value = FavieProductUtils.extract_currency_and_amount(stark_price.raw)
            price = StarkProductListAdapter.__convert_price(currency_code, value, parse_time)
            if price:
                return price

        return StarkProductListAdapter.__convert_price(stark_price.currency, stark_price.value, parse_time)

    @staticmethod
    def __convert_price(currency_code: str, value: float, parse_time: str) -> Price:
        currency_converter = CurrencyConverter(currency_code, value)
        price = Price(
            currency=currency_converter.get_currency_code(),
            value=currency_converter.get_subunit_value(),
            updates_at=parse_time,
        )
        return price if CommonUtils.all_not_none(price.currency, price.value) else None


if __name__ == "__main__":
    stark_product_list_message = read_object(
        "/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/stark_product_list_message.json",
        StarkProductListMessage,
    )
    adapter = StarkProductListAdapter()
    product_list = adapter.stark_list_to_favie_details(stark_product_list_message)
    if product_list:
        for product in product_list:
            print(product.model_dump_json(exclude_none=True))

from favie_data_common.common.common_utils import CommonUtils

from favie_data_schema.favie.adapter.common.stark_enum import StarkProductDataType
from favie_data_schema.favie.adapter.common.stark_message import StarkProductListMessage
from favie_data_schema.favie.adapter.common.stark_message_utils import StarkMessageUtils
from favie_data_schema.favie.adapter.product.common.currency import CurrencyConverter
from favie_data_schema.favie.adapter.product.common.favie_product_adapter import FavieProductDetailAdapter
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
        stark_price = stark_product_item.price if stark_product_item.price is not None else None
        if stark_price is None and CommonUtils.list_len(stark_product_item.prices) > 0:
            stark_price = next(filter(lambda price: price.is_primary, stark_product_item.prices))
        return StarkProductListAdapter.convert_price(stark_price, parse_time)

    @staticmethod
    def get_rrp(stark_product_item: ProductListItem, parse_time: str) -> Price:
        if CommonUtils.list_len(stark_product_item.prices) > 0:
            stark_price = next(filter(lambda price: price.is_rrp, stark_product_item.prices))
            return StarkProductListAdapter.convert_price(stark_price, parse_time)

    @staticmethod
    def convert_price(stark_price: StarkPrice, parse_time: str) -> Price:
        if stark_price is None:
            return None
        currency_converter = CurrencyConverter(stark_price.currency, stark_price.value)
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

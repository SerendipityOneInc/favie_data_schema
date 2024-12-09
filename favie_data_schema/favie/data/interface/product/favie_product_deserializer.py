import logging
from typing import Dict, List

from favie_data_common.common.pydantic_utils import PydanticUtils

from favie_data_schema.favie.data.interface.product.favie_product import Price


class HistoricalPricesDeserializer:
    @staticmethod
    def deserialize(value: str):
        try:
            if not value:
                return None
            return PydanticUtils.deserialize_data(List[Price], value)

        except Exception:
            try:
                prices = PydanticUtils.deserialize_data(dict[str, List[Price]], value)
                return HistoricalPricesDeserializer.group_to_list(prices)
            except Exception as e:
                logging.exception("Deserialize HistoricalPrices failed: %s", e)
                return None

    @staticmethod
    def group_to_list(prices: Dict[str, List[Price]]):
        if not prices:  # 如果 prices 是空的，返回 None
            return None

        result = []  # 创建一个空列表用于存放所有的 Price 对象
        for price_list in prices.values():  # 遍历字典中的每个 value（每个 value 是一个 Price 列表）
            for price in price_list:  # 遍历当前 Price 列表中的每个 Price 对象
                result.append(price)  # 将它追加到结果列表中
        return result

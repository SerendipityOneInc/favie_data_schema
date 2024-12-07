import json
import unittest
from typing import Dict, List, Optional

from favie_data_common.common.pydantic_utils import PydanticUtils
from pydantic import BaseModel, field_validator

from favie_data_schema.favie.data.interface.common.favie_utils import deserialize_data
from favie_data_schema.favie.data.interface.product.favie_product import FavieProductDetail


class Address(BaseModel):
    city: Optional[str] = None
    street: Optional[str] = None
    zip_code: Optional[str] = None


# 一个简单的 Pydantic 模型
class Product(BaseModel):
    id: Optional[int] = None

    @field_validator("id", mode="before")
    def validate_id(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "id")
        return deserialize_data(expected_type, value)

    name: Optional[str] = None

    @field_validator("name", mode="before")
    def validate_name(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "name")
        return deserialize_data(expected_type, value)

    colors: Optional[List[str]] = None

    @field_validator("colors", mode="before")
    def validate_colors(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "colors")
        return deserialize_data(expected_type, value)

    addresses: Optional[List[Address]] = None

    @field_validator("addresses", mode="before")
    def validate_addresses(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "addresses")
        return deserialize_data(expected_type, value)

    main_address: Optional[Address] = None

    @field_validator("main_address", mode="before")
    def validate_main_address(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "main_address")
        return deserialize_data(expected_type, value)

    attributes: Optional[Dict[str, str]] = None

    @field_validator("attributes", mode="before")
    def validate_attributes(cls, value):
        expected_type = PydanticUtils.get_native_field_type(cls, "attributes")
        return deserialize_data(expected_type, value)


class TestDeserializeData(unittest.TestCase):
    def test_basic_types(self):
        json_str = '{"id": 1, "name": "Item1"}'
        json_data = json.loads(json_str)
        self.assertEqual(Product(**json_data), Product(id=1, name="Item1"))

        json_str = '{"id": "1", "name": "Item1"}'
        json_data = json.loads(json_str)
        self.assertEqual(Product(**json_data), Product(id=1, name="Item1"))

    def test_list_types(self):
        json_str = '{"colors": ["red", "green", "blue"]}'
        json_data = json.loads(json_str)
        self.assertEqual(Product(**json_data), Product(colors=["red", "green", "blue"]))

        json_str = '{"colors": "[\\"red\\", \\"green\\", \\"blue\\"]"}'
        json_data = json.loads(json_str)
        self.assertEqual(Product(**json_data), Product(colors=["red", "green", "blue"]))

    def test_pydantic_types(self):
        json_str = '{"main_address": {"city": "Shanghai", "street": "Nanjing Road", "zip_code": "200000"}}'
        json_data = json.loads(json_str)
        self.assertEqual(
            Product(**json_data),
            Product(main_address=Address(city="Shanghai", street="Nanjing Road", zip_code="200000")),
        )

        json_str = '{"main_address": "{\\"city\\": \\"Shanghai\\", \\"street\\": \\"Nanjing Road\\", \\"zip_code\\": \\"200000\\"}"}'
        json_data = json.loads(json_str)
        self.assertEqual(
            Product(**json_data),
            Product(main_address=Address(city="Shanghai", street="Nanjing Road", zip_code="200000")),
        )

        json_str = '{"addresses": [{"city": "Shanghai", "street": "Nanjing Road", "zip_code": "200000"}, {"city": "Beijing", "street": "Wangfujing", "zip_code": "100000"}]}'
        json_data = json.loads(json_str)
        self.assertEqual(
            Product(**json_data),
            Product(
                addresses=[
                    Address(city="Shanghai", street="Nanjing Road", zip_code="200000"),
                    Address(city="Beijing", street="Wangfujing", zip_code="100000"),
                ]
            ),
        )

        json_str = '{"addresses": "[{\\"city\\": \\"Shanghai\\", \\"street\\": \\"Nanjing Road\\", \\"zip_code\\": \\"200000\\"}, {\\"city\\": \\"Beijing\\", \\"street\\": \\"Wangfujing\\", \\"zip_code\\": \\"100000\\"}]"}'
        json_data = json.loads(json_str)
        self.assertEqual(
            Product(**json_data),
            Product(
                addresses=[
                    Address(city="Shanghai", street="Nanjing Road", zip_code="200000"),
                    Address(city="Beijing", street="Wangfujing", zip_code="100000"),
                ]
            ),
        )

    def test_model_validate_json(self):
        input_str = """
            {
                "f_sku_id": "46710969663721-shop.app",
                "price": "{\\"value\\":-100,\\"currency\\":\\"USD\\",\\"updates_at\\":\\"1732687436\\",\\"source_type\\":\\"1\\",\\"parser_name\\":\\"ShopProductDetailParser\\"}",
                "f_meta": {
                    "source_type": "5",
                    "parser_name": "DataCleaning",
                    "data_type": "1",
                    "parses_at": "1733552065"
                }
            }
        """
        product = FavieProductDetail.model_validate_json(input_str)
        self.assertEqual(product.f_sku_id, "46710969663721-shop.app")


if __name__ == "__main__":
    unittest.main()

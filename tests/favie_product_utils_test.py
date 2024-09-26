import unittest

from favie_data_schema.favie.adapter.product.common.favie_product_utils import FavieProductUtils  # 请替换为实际的模块名


class TestExtractCurrencyAndAmount(unittest.TestCase):
    def test_currency_code_before_amount(self):
        self.assertEqual(FavieProductUtils.extract_currency_and_amount("USD 100"), ("USD", 100.0))

    def test_currency_code_after_amount(self):
        self.assertEqual(FavieProductUtils.extract_currency_and_amount("100 EUR"), ("EUR", 100.0))

    def test_currency_symbol_before_amount(self):
        self.assertEqual(FavieProductUtils.extract_currency_and_amount(r"\$50.5"), ("USD", 50.5))

    def test_currency_symbol_after_amount(self):
        self.assertEqual(FavieProductUtils.extract_currency_and_amount("200¥"), ("JPY", 200.0))

    def test_currency_symbol_after_amount(self):
        self.assertEqual(FavieProductUtils.extract_currency_and_amount("CNY 200¥"), ("CNY", 200.0))

    def test_amount_with_comma(self):
        self.assertEqual(FavieProductUtils.extract_currency_and_amount("1,000.50 kr"), ("SEK", 1000.5))

    def test_amount_with_multiple_commas(self):
        self.assertEqual(FavieProductUtils.extract_currency_and_amount("1,000,000.50 USD"), ("USD", 1000000.5))

    def test_amount_only(self):
        self.assertEqual(FavieProductUtils.extract_currency_and_amount("100"), None)

    def test_no_match(self):
        self.assertEqual(FavieProductUtils.extract_currency_and_amount("No price here"), None)

    def test_mixed_case_currency_code(self):
        self.assertEqual(FavieProductUtils.extract_currency_and_amount("gBp 75"), ("GBP", 75.0))

    def test_currency_with_spaces(self):
        self.assertEqual(FavieProductUtils.extract_currency_and_amount("  €  50  "), ("EUR", 50.0))

    def test_multiple_currency_symbols(self):
        self.assertEqual(FavieProductUtils.extract_currency_and_amount(r"\$100$"), ("USD", 100.0))

    def test_currency_code_and_symbol(self):
        self.assertEqual(FavieProductUtils.extract_currency_and_amount(r"USD \$100"), ("USD", 100.0))


if __name__ == "__main__":
    unittest.main()

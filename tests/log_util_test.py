import base64
import unittest

from favie.utils.log_util import (
    compress_and_encode_html,
    decode_and_decompress_html,
    is_encoded_html,
)


class TestHtmlEncoding(unittest.TestCase):
    def test_compress_and_encode_html(self):
        html_string = "<html><body><h1>Hello, World!</h1></body></html>"
        encoded_html_string = compress_and_encode_html(html_string)

        # 测试是否返回了非空字符串
        self.assertTrue(len(encoded_html_string) > 0)

    def test_decode_and_decompress_html(self):
        html_string = "<html><body><h1>Hello, World!</h1></body></html>"
        encoded_html_string = compress_and_encode_html(html_string)
        decoded_html_string = decode_and_decompress_html(encoded_html_string)

        # 测试解压缩和解码是否返回原始HTML
        self.assertEqual(html_string, decoded_html_string)

    def test_is_encoded_html(self):
        html_string = "<html><body><h1>Hello, World!</h1></body></html>"
        encoded_html_string = compress_and_encode_html(html_string)

        # 测试是否识别为已编码
        self.assertTrue(is_encoded_html(encoded_html_string))

        # 测试非编码字符串
        self.assertFalse(is_encoded_html(html_string))

        # 测试无效的Base64字符串
        invalid_base64_string = "invalid_base64_string"
        self.assertFalse(is_encoded_html(invalid_base64_string))

        # 测试有效的Base64但无效的gzip数据
        valid_base64_invalid_gzip = base64.b64encode(b"invalid gzip data").decode("utf-8")
        self.assertFalse(is_encoded_html(valid_base64_invalid_gzip))


if __name__ == "__main__":
    unittest.main()

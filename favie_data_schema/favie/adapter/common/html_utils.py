import base64
import gzip
from lxml import html
import re
import hashlib
from favie_data_schema.favie.adapter.data_mock.data_mock_read import read_file

class HtmlUtils():
    @staticmethod
    def decode_and_decompress_html(encoded_html_string):
        """解码并解压缩 HTML 字符串"""
        try:
            # Base64解码
            compressed_html = base64.b64decode(encoded_html_string)

            # 解压缩
            decompressed_html = gzip.decompress(compressed_html)

            # 将字节串转换为字符串
            html_string = decompressed_html.decode("utf-8")

            return html_string
        except Exception:
            return encoded_html_string
    


if __name__ == "__main__":
    encoded_data = read_file('/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/encoded_html.txt')
    html_content = HtmlUtils.decode_and_decompress_html(encoded_data)
    tree = html.fromstring(html_content)
    element = tree.xpath('//*[@id="social-proofing-faceout-title-tk_bought"]/span')
    print(element is not None)

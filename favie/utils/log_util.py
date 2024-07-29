import base64
import gzip


def compress_and_encode_html(html_string):
    # 压缩HTML字符串
    compressed_html = gzip.compress(html_string.encode("utf-8"))

    # Base64编码
    encoded_html = base64.b64encode(compressed_html)

    # 将Base64编码后的字节串转换为字符串
    encoded_html_string = encoded_html.decode("utf-8")

    return encoded_html_string


def decode_and_decompress_html(encoded_html_string):
    try:
        # Base64解码
        compressed_html = base64.b64decode(encoded_html_string)

        # 解压缩
        decompressed_html = gzip.decompress(compressed_html)

        # 将字节串转换为字符串
        html_string = decompressed_html.decode("utf-8")

        return html_string
    except (base64.binascii.Error, gzip.BadGzipFile):
        return None


def is_encoded_html(encoded_html_string):
    try:
        # Base64解码
        compressed_html = base64.b64decode(encoded_html_string)

        # 尝试解压缩
        gzip.decompress(compressed_html)

        return True
    except (base64.binascii.Error, gzip.BadGzipFile):
        return False

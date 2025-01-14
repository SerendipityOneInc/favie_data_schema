import logging
import re

from favie_data_schema.favie.adapter.common.image_url_rewriter.image_url_rewriter import ImageUrlRewriter


class AmazoneImageUrlRewriter(ImageUrlRewriter):
    def __init__(self, rewrite_size: int = 640):
        super().__init__(rewrite_size)
        self.domain = "amazon.com"
        self.logger = logging.getLogger(__name__)

    def rewrite(self, source_site: str, image_url: str):
        if not image_url:
            return image_url

        if source_site != self.domain:
            self.logger.warning(f"source_site is not {self.domain}, source_site: {source_site}, image_url: {image_url}")
            return image_url

        # 使用正则表达式匹配类似 "_SY88" 的部分
        match = re.search(r"_SY(\d+)", image_url)
        if match:
            # 提取数字部分
            number = int(match.group(1))
            if number < 640:
                # 构建新的字符串
                modified_url = image_url.replace(f"_SY{number}", f"_SY{self.rewrite_size}")
                return modified_url
        # 如果找不到匹配部分或者不需要修改，返回原始 URL
        return image_url

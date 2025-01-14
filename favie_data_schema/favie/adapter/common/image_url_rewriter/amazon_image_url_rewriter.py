import logging
import re

from favie_data_schema.favie.adapter.common.image_url_rewriter.image_url_rewriter import ImageUrlRewriter


# https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png
# https://m.media-amazon.com/images/I/81G8btUlZVL._SY88.jpg
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

        modified_url = self.__match_sx(image_url)
        if modified_url:
            return modified_url
        modified_url = self.__match_sy(image_url)
        if modified_url:
            return modified_url
        return image_url

    def __match_sx(self, image_url):
        match = re.search(r"_SX(\d+)_", image_url)
        if match:
            number = int(match.group(1))
            if number < 640:
                modified_url = image_url.replace(f"_SX{number}_", f"_SX{self.rewrite_size}_")
                return modified_url

    def __match_sy(self, image_url):
        match = re.search(r"_SY(\d+)", image_url)
        if match:
            # 提取数字部分
            number = int(match.group(1))
            if number < 640:
                # 构建新的字符串
                modified_url = image_url.replace(f"_SY{number}", f"_SY{self.rewrite_size}")
                return modified_url

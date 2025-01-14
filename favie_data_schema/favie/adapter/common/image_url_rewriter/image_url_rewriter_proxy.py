from favie_data_schema.favie.adapter.common.image_url_rewriter.amazon_image_url_rewriter import AmazoneImageUrlRewriter
from favie_data_schema.favie.adapter.common.image_url_rewriter.image_url_rewriter import ImageUrlRewriter


class ImageUrlRewriterProxy(ImageUrlRewriter):
    def __init__(self, rewrite_size: int = 640):
        super().__init__(rewrite_size)
        self.proxy_config = {
            "amazon.com": AmazoneImageUrlRewriter(rewrite_size=rewrite_size),
        }
        self.default_rewriter = ImageUrlRewriter(rewrite_size=rewrite_size)

    def rewrite(self, source_site: str, image_url: str) -> str:
        rewriter = self.proxy_config.get(source_site, self.default_rewriter)
        return rewriter.rewrite(source_site, image_url)

class ImageUrlRewriter:
    def __init__(self, rewrite_size: int = 640):
        self.rewrite_size = rewrite_size

    def rewrite(self, source_site: str, image_url: str) -> str:
        return image_url

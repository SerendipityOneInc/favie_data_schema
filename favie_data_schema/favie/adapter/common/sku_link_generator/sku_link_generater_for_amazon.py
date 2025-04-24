import logging

from favie_data_schema.favie.adapter.common.sku_link_generator.sku_link_generater import SkuLinkGenerater


class SkuLinkGeneraterForAmazon(SkuLinkGenerater):
    site = "amazon.com"

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)

    def gen_sku_link(self, site: str, sku_id: str) -> str:
        if site != self.site:
            self.logger.error("Invalid site: %s, expected: %s", site, self.site)
            return None

        return f"https://www.amazon.com/dp/{sku_id}"

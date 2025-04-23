import logging

from favie_data_schema.favie.adapter.common.sku_link_generator.sku_link_generater import SkuLinkGenerater
from favie_data_schema.favie.adapter.common.sku_link_generator.sku_link_generater_for_amazon import (
    SkuLinkGeneraterForAmazon,
)


class SkuLinkGeneraterProxy(SkuLinkGenerater):
    def __init__(self):
        super().__init__()
        self.router = {"amazon.com": SkuLinkGeneraterForAmazon()}
        self.logger = logging.getLogger(__name__)

    def gen_sku_link(self, site: str, sku_id: str) -> str:
        generator = self.router.get(site)
        if not generator:
            self.logger.error("Invalid site: %s, expected: %s", site, self.router.keys())
            return None
        if not sku_id:
            self.logger.error("Invalid sku_id: %s", sku_id)
            return None
        return generator.gen_sku_link(site, sku_id)


if __name__ == "__main__":
    generator = SkuLinkGeneraterProxy()
    print(generator.gen_sku_link("amazon.com", "B0BHZT5S12"))  # Example SKU ID

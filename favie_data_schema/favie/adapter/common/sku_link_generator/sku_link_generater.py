class SkuLinkGenerater:
    def gen_sku_link(self, site: str, sku_id: str) -> str:
        """
        生成SKU链接
        :param site: site
        :param sku_id: SKU ID
        :return: SKU链接
        """
        # 假设链接格式为 "https://example.com/sku/{sku_id}"

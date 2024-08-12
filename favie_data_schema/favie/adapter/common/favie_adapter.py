from favie_data_schema.favie.adapter.common.crawler_kakfa_message import CrawlerKafkaMessage
from favie_data_schema.favie.data.interface.product.favie_product import FavieProduct


class FavieAdapter():
    @staticmethod
    def convert_to_favie_product(crawler_kafka_message: CrawlerKafkaMessage) -> FavieProduct:
        # TODO: implement
        pass
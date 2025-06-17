import json
import logging

from mock_data.mock_data_read import read_file

from favie_data_schema.favie.data.interface.gensmo_feed.gensmo_moodboard import GemMoodboard


class GemFeedAdapter:
    """
    Adapter class for GemFeed.
    This class is responsible for adapting the GemFeed data to the required format.
    """

    MOODBOARD = "moodboard"
    TRY_ON = "try_on"

    def __init__(self):
        """
        Initialize the GemFeedAdapter with a GemFeed instance.

        :param gem_feed: An instance of GemFeed.
        """
        self.logger = logging.getLogger(__name__)

    def adapt(self, feed_message):
        try:
            if not feed_message:
                self.logger.warning("feed_message is None or empty")
                return None
            feed_data = json.loads(feed_message)  # Ensure the value is valid JSON
            if feed_data is None:
                self.logger.warning(f"feed message deserialize failed: {feed_message}")
                return None
            if GemFeedAdapter.MOODBOARD == self.__get_feed_type(feed_data):
                return self.__convert_by_moodboard(feed_data)
            else:
                return self.__convert_by_try_on(feed_data)
        except Exception as e:
            self.logger.exception(f"Error in DeserializeStarkDetailMessageFunction: content = {feed_message} {e}")
            return None

    def __get_feed_type(self, feed_data: dict) -> str:
        """
        根据feed_data中的type字段获取feed的类型
        """
        return GemFeedAdapter.MOODBOARD if feed_data.get("moodboard_id") else GemFeedAdapter.TRY_ON

    def __convert_by_moodboard(self, feed_data: dict) -> dict:
        """
        Convert the feed data to moodboard format.
        """
        gem_feed = GemMoodboard()
        gem_feed.moodboard_id = feed_data.get("moodboard_id")
        gem_feed.moodboard_image_url = feed_data.get("image")
        gem_feed.moodboard_type = GemFeedAdapter.MOODBOARD
        gem_feed.product_ids = self.__get_product_ids_of_moodboard(feed_data)
        return gem_feed

    def __convert_by_try_on(self, feed_data: dict) -> dict:
        """
        Convert the feed data to try_on format.
        """
        gem_feed = GemMoodboard()
        gem_feed.moodboard_id = feed_data.get("try_on_task_id")
        gem_feed.moodboard_image_url = feed_data.get("try_on_cover_image")
        gem_feed.moodboard_type = GemFeedAdapter.TRY_ON
        gem_feed.product_ids = self.__get_product_ids_of_tryon(feed_data)
        return gem_feed

    def __get_product_ids_of_moodboard(self, feed_data: dict) -> list:
        """
        获取产品ID列表
        """
        try:
            moodboards = json.loads(feed_data.get("moodboards"))
            products = moodboards.get("products", [])
            return [product.get("global_id") for product in products if product.get("global_id")]
        except json.JSONDecodeError as e:
            self.logger.exception(f"""Error decoding moodboards JSON: {feed_data.get("moodboards")}""")

    def __get_product_ids_of_tryon(self, feed_data: dict) -> list:
        """
        获取产品ID列表
        """
        try:
            products = feed_data.get("products", [])
            return [product.get("global_id") for product in products if product.get("global_id")]
        except KeyError as e:
            self.logger.exception(f"KeyError in get_product_ids_of_tryon: {e}")
            return []


if __name__ == "__main__":
    adapter = GemFeedAdapter()
    feed_message = read_file("/workspace/jobs/resources/moodboard_message.json")
    moodboard = adapter.adapt(feed_message)

    if moodboard:
        print(moodboard.model_dump_json(exclude_none=True))

    feed_message = read_file("/workspace/jobs/resources/tryon_message.json")
    moodboard = adapter.adapt(feed_message)

    if moodboard:
        print(moodboard.model_dump_json(exclude_none=True))

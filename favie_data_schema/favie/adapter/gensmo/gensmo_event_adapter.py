import json
import logging

from favie_data_schema.favie.adapter.tools.data_mock_read import read_file
from favie_data_schema.favie.data.interface.gensmo_feed.gensmo_event import EventItem, GensmoEvent


class GensmoEventAdapter:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def convert_gensmo_event(self, gensmo_event_message) -> GensmoEvent:
        try:
            event_data = json.loads(gensmo_event_message)
            gensmo_event = GensmoEvent()
            gensmo_event.user_id = event_data.get("gensmo_user_id")
            gensmo_event.device_id = event_data.get("gensmo_active_id")
            gensmo_event.event_version = event_data.get("event_version")
            gensmo_event.refer = event_data.get("refer")
            gensmo_event.ap_name = event_data.get("item_list_name")
            gensmo_event.event_name = event_data.get("event_name")
            gensmo_event.event_method = event_data.get("method")
            gensmo_event.event_action_type = event_data.get("action_type")
            gensmo_event.user_login_type = event_data.get("gensmo_user_type")
            gensmo_event.event_timestamp = int(event_data.get("gensmo_timestamp"))
            gensmo_event.event_items = self.__get_event_items(event_data)
            gensmo_event.appsflyer_id = event_data.get("appsflyer_id")
            gensmo_event.event_ab_infos = self.__get_ab_infos(event_data)
            gensmo_event.platform = event_data.get("platform")
            gensmo_event.app_version = event_data.get("version")
            return gensmo_event
        except json.JSONDecodeError as e:
            logging.exception(f"Failed to decode JSON: {e}")
            return None

    def __get_ab_infos(self, event_data) -> list[str] | None:
        try:
            ab_infos = event_data.get("ab_info")
            if not ab_infos:
                return None
            json_ab_infos = json.loads(ab_infos)
            if not isinstance(json_ab_infos, list):
                logging.warning("ab_info is not a list")
                return None
            return json_ab_infos
        except Exception as e:
            logging.exception(f"Failed to process AB infos: {e}")
            return None

    def __get_event_items(self, event_data) -> list[str] | None:
        try:
            items = event_data.get("items", [])
            if not items:
                return None

            return [
                EventItem(
                    item_id=item.get("item_id"),
                    item_name=item.get("item_name"),
                    item_type=item.get("item_category"),
                    item_index=item.get("index"),
                )
                for item in items
                if isinstance(item, dict)
            ]
        except Exception as e:
            logging.exception(f"Failed to process event items: {e}")
            return None


if __name__ == "__main__":
    adapter = GensmoEventAdapter()
    message_str = read_file("./favie_data_schema/favie/resources/gensmo_event_message.json")
    # webpage_message = DeserializeUtils.deserialize_webpage_message(webpage_message_str)
    gensmo_event = adapter.convert_gensmo_event(message_str)
    if gensmo_event:
        print(gensmo_event.model_dump_json(exclude_none=True))

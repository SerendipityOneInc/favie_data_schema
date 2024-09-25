import logging
from datetime import datetime

from favie_data_common.common.common_utils import CommonUtils

from favie_data_schema.favie.adapter.common.stark_message import StarkMessage


class StarkMessageUtils:
    @staticmethod
    def get_parse_time(message: StarkMessage):
        try:
            return str(int(CommonUtils.datetime_string_to_timestamp(message.update_time)))
        except Exception:
            logging.exception("get_parse_time error: %s", message.model_dump_json(exclude_none=True))
            return str(int(datetime.now().timestamp()))

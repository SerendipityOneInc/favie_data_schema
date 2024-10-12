import logging
from datetime import datetime

from favie_data_common.common.common_utils import CommonUtils

from favie_data_schema.favie.adapter.common.stark_message import StarkMessage


class StarkMessageUtils:
    @staticmethod
    def get_parse_time(message: StarkMessage):
        try:
            parse_time = CommonUtils.datetime_string_to_timestamp(message.update_time)
            if parse_time:
                return str(int(parse_time))
            else:
                return str(int(datetime.now().timestamp()))
        except Exception:
            logging.exception("get_parse_time error: %s", message.model_dump_json(exclude_none=True))
            return str(int(datetime.now().timestamp()))

    @staticmethod
    def get_domain(message: StarkMessage):
        if message.host:
            return StarkMessageUtils.get_domain_by_url(message.host)
        elif message.url:
            return StarkMessageUtils.get_domain_by_url(message.url)
    @staticmethod
    def get_domain_by_url(url: str)->str|None:
        return CommonUtils.host_trip_www(CommonUtils.get_full_subdomain(url))
    
    
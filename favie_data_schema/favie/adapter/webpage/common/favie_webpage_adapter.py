from favie_data_schema.favie.adapter.common.stark_message import StarkWebpageMessage
from favie_data_schema.favie.data.interface.webpage.favie_webpage import FavieWebpage


class FavieWebpageAdapter:
    @staticmethod
    def stark_webpage_to_favie_webpage(webpage_message: StarkWebpageMessage) -> FavieWebpage:
        # TODO: implement
        pass

    @staticmethod
    def _message_check(webpage_message: StarkWebpageMessage) -> bool:
        if webpage_message is None:
            return False

        if webpage_message.crawl_result is None:
            return False

        if webpage_message.crawl_result.original_status != 200 and webpage_message.crawl_result.pc_status != 200:
            return False

        if webpage_message.crawl_result.original_url is None:
            return False

        if webpage_message.crawl_result.webpage is None:
            return False

        if webpage_message.crawl_result.webpage.parsed_webpage_content is None:
            return False

        return True

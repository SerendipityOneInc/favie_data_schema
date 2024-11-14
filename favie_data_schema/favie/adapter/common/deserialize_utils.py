import json
import logging

from favie_data_common.common.common_utils import CommonUtils

from favie_data_schema.favie.adapter.common.stark_message import StarkNewWebpageMessage, StarkWebpageMessage
from favie_data_schema.favie.adapter.tools.data_mock_read import read_file
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_review import RainforestProductReview


class DeserializeUtils:
    new_webpage_parser_names = ["InstagramPostListParser", "ContentPWParser"]

    @staticmethod
    def deserialize_rainforest_product_review(data: str) -> RainforestProductReview:
        try:
            if not data:
                return None
            message_dict = json.loads(data)
            if not message_dict:
                return None
            reviews = message_dict.get("reviews")
            if CommonUtils.list_len(reviews) >= 0:
                for review in reviews:
                    if review and CommonUtils.list_len(review.get("images")) > 0:
                        if isinstance(review["images"][0], dict):
                            review["images"] = [image["link"] for image in review["images"]]

            return RainforestProductReview(**message_dict)
        except Exception as e:
            logging.exception(f"Error in deserialize_rainforest_product_review: {message_dict} {e}")
            return None

    @staticmethod
    def deserialize_webpage_message(data: str) -> StarkNewWebpageMessage | StarkWebpageMessage:
        try:
            if not data:
                return None
            message_dict = json.loads(data)
            if not message_dict:
                return None
            parser_name = message_dict.get("parser_name")
            if parser_name in DeserializeUtils.new_webpage_parser_names:
                return StarkNewWebpageMessage(**message_dict)
            else:
                return StarkWebpageMessage(**message_dict)
        except Exception as e:
            logging.exception(f"Error in deserialize_rainforest_product_review: {message_dict} {e}")
            return None


if __name__ == "__main__":
    # data = read_file("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/rainforest_product_review_1.json")
    # rainforest_product_review = DeserializeUtils.deserialize_rainforest_product_review(data)
    # print(rainforest_product_review.model_dump_json() if rainforest_product_review else None)

    webpage_data_new = read_file(
        "/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/stark_webpage_message_new.json"
    )
    webpage_new = DeserializeUtils.deserialize_webpage_message(webpage_data_new)
    print(webpage_new.model_dump_json(exclude_none=True) if webpage_new else None)
    webpage_data = read_file(
        "/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/stark_webpage_message.json"
    )
    webpage = DeserializeUtils.deserialize_webpage_message(webpage_data)
    print(webpage.model_dump_json(exclude_none=True) if webpage else None)

import json
import logging

from favie_data_common.common.common_utils import CommonUtils
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_review import RainforestProductReview
from favie_data_schema.favie.adapter.tools.data_mock_read import read_file

class DeserializeUtils:
    @staticmethod
    def deserialize_rainforest_product_review(data: str)->RainforestProductReview:
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
        

if __name__ == "__main__":
    data = read_file("/Users/pangbaohui/workspace-srp/favie_data_schema/favie_data_schema/favie/resources/rainforest_product_review_1.json")
    rainforest_product_review = DeserializeUtils.deserialize_rainforest_product_review(data)
    print(rainforest_product_review.model_dump_json() if rainforest_product_review else None)
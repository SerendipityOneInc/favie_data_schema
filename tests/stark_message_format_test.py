import unittest
from favie_data_schema.favie.data.crawl_data.rainforest.rainforest_product_detail import RainforestProductDetail
from tests.read_json_util import read_object
from favie_data_schema.favie.adapter.common.stark_message import StarkMessage, StarkProductDetailMessage
    
# 测试类
class TestStarkMessageMission(unittest.TestCase):
    
# 从文件读取 JSON 数据，并反序列化为 AmazonKafkaMessage 对象
    def test_mission_valid_value(self):
        """测试为 mission 属性赋值字符串是否成功"""
        value=read_object("tests/stark_product_detail.json",StarkMessage)
        self.assertEqual(value.mission, "refresh deal products")
    
    def test_mission_type(self):
        msg=StarkMessage(mission="123")
        self.assertEqual(msg, StarkMessage(mission="123"))
        

    
if __name__ == "__main__":
    #value=read_object("tests/stark_product_detail.json",StarkProductDetailMessage)
    #print(value.model_dump_json())
    unittest.main()
    



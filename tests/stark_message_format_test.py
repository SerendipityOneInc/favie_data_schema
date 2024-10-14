import unittest
from pydantic import BaseModel, ValidationError

from typing import Optional


from favie_data_schema.favie.adapter.common.stark_message import StarkMessage
# 测试类
class TestStarkMessageMission(unittest.TestCase):
    def test_mission_valid_value(self):
        """测试为 mission 属性赋值字符串是否成功"""
        msg = StarkMessage(mission="TestMission")
        self.assertEqual(msg.mission, "TestMission")
        
    def test_mission_type(self):
        msg=StarkMessage(mission="123")
        self.assertEqual(msg, StarkMessage(mission="123"))


if __name__ == "__main__":
    unittest.main()
    

import unittest

from favie_data_schema.favie.adapter.common.image_url_rewriter.image_url_rewriter_proxy import ImageUrlRewriterProxy


# 测试类
class TestStarkMessageMission(unittest.TestCase):
    # 从文件读取 JSON 数据，并反序列化为 AmazonKafkaMessage 对象
    def test_amazon_rewrite(self):
        rewriter = ImageUrlRewriterProxy()
        old_url = "https://m.media-amazon.com/images/I/81G8btUlZVL._SY88.jpg"
        new_url = rewriter.rewrite("amazon.com", old_url)
        self.assertEqual(new_url, "https://m.media-amazon.com/images/I/81G8btUlZVL._SY640.jpg")

        old_url = (
            "https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"
        )
        new_url = rewriter.rewrite("amazon.com", old_url)
        self.assertEqual(
            new_url,
            "https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX640_.png",
        )

    def test_not_amazon_rewrite(self):
        rewriter = ImageUrlRewriterProxy()
        old_url = "https://m.media-amazon.com/images/I/81G8btUlZVL._SY88.jpg"
        new_url = rewriter.rewrite("shop.app", old_url)
        self.assertEqual(new_url, "https://m.media-amazon.com/images/I/81G8btUlZVL._SY88.jpg")


if __name__ == "__main__":
    unittest.main()

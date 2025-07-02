from enum import Enum, IntEnum
class Source(IntEnum):
    # 未知
    UNKNOWN = 0
    # 爬虫爬取页面
    SPIDER = 1
    # 数据服务写入
    DATA_SERVICE = 2
    # 爬虫调用RF API获取
    SPIDER_CALL_RF_API = 3
    # 外部购买数据
    EXTERNAL_PURCHASE_DATA = 4
    #内部处理数据，包含离线修复数据
    INTERNAL_PROCESS = 5


class CrawlStatus(Enum):
    SUCCESS         = (1, "success")            # 网页爬取成功
    DUPLICATE       = (3, "duplicate")          # 网页重复爬取
    FAILED          = (-1, "failed")            # 网页爬取失败
    NOT_FOUND       = (-2, "not found")         # 网页不存在【网页没有出现任何有效信息（商品信息、商品列表等）/第三方API接口应答确认有效信息（商品信息、商品列表等）不存在】
    PARSE_FAILED    = (-3, "parse failed")      # 解析网页URL失败

    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
from enum import IntEnum


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
    

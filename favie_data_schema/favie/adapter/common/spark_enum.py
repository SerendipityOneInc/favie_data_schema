from enum import Enum, IntEnum, auto

class SparkProductDataType(IntEnum):
    UNKNOWN = 0
    PRODUCT_DETAIL = 1
    PRODUCT_LIST = 2
    PRODUCT_REVIEW = 3
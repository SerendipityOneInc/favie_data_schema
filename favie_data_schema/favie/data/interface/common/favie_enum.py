from enum import IntEnum


class FavieSourceType(IntEnum):
    UNKNOWN = 0
    PRODUCT_DETAIL = 1
    PRODUCT_REVIEW = 2
    WEB_PAGE = 3
    AD = 4


class ProductDataType(IntEnum):
    UNKNOWN = 0
    PRODUCT_DETAIL_CRAWLER = 1
    PRODUCT_LIST_CRAWLER = 2
    PRODUCT_REVIEW_CRAWLER = 3
    PRODUCT_CATEGORY_PREDICT = 4
    PRODUCT_IMAGE_CRAWLER = 5

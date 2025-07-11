from enum import Enum, IntEnum


class FavieSourceType(IntEnum):
    UNKNOWN = 0
    PRODUCT_DETAIL = 1
    PRODUCT_REVIEW = 2
    WEB_PAGE = 3
    PRODUCT_DETAIL_BASE = 4
    AD = 5


class MessageDataType(IntEnum):
    UNKNOWN = 0
    PRODUCT_DETAIL_CRAWLER = 1
    PRODUCT_LIST_CRAWLER = 2
    PRODUCT_REVIEW_CRAWLER = 3
    PRODUCT_CATEGORY_PREDICT = 4
    PRODUCT_IMAGE_CRAWLER = 5
    PRODUCT_REVIEW_IMAGE_CRAWLER = 6
    WEBPAGE_CONTENT_CRAWLER = 7
    WEBPAGE_IMAGE_CRAWLER = 8
    DATA_CLEANING = 9
    DATA_DELETE = 10
    DATA_ARCHIVE = 11


class FavieDataStatus(IntEnum):
    NORMAL = 0
    DELETED = 1
    INTERCEPTED = 2
    ARCHIVED = 3


class FavieImageStatus(IntEnum):
    NORMAL = 0
    DELETED = 1
    DOWNLOAD_FAILED = 2
    TOO_SMALL = 3


class CategoriesMapType(IntEnum):
    MAP = 0
    PREDICT = 1


class DataAction(Enum):
    DELETE_FIELDS = "delete_fields"
    RECRAWL_IMAGES = "recrawl_images"
    ARCHIVE = "archive"


class InventoryStatus(Enum):
    IN_STOCK = "in_stock"
    OUT_OF_STOCK = "out_of_stock"
    UNKNOWN = "unknown"

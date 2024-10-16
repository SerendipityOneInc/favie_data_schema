from enum import Enum, IntEnum, auto


class FavieProductDetailStatus(Enum):
    SKU_INIT = auto()
    SKU_NORMAL = auto()
    SKU_NOT_FOUND = auto()


class CategoriesMapType(IntEnum):
    MAP = 0
    PREDICT = 1

from enum import Enum, IntEnum, auto
class FavieProductDetailStatus(Enum):
    SKU_INIT = auto()
    SKU_NORMAL = auto()
    SKU_NOT_FOUND = auto()
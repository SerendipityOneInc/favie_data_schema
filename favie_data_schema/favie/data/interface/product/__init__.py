# 导入产品基础模型类
from .favie_product import (  # 基础数据模型; 产品信息分组模型; 分类预测响应
    AttributeItem,
    AttrInfo,
    BaseInfo,
    Brand,
    CategoryItem,
    Deal,
    DescInfo,
    ExtendedInfo,
    FavieCategoriesPredictResponse,
    Images,
    Inventory,
    MediaInfo,
    PlatformChoice,
    Price,
    PriceInfo,
    Promotion,
    RatingBreakdown,
    ReturnPolicy,
    ReviewSummary,
    SaleInfo,
    Seller,
    SellerRank,
    SimpleProduct,
    Video,
)

# 导入反序列化工具
from .favie_product_deserializer import HistoricalPricesDeserializer

# 导入产品详情模型
from .favie_product_detail import FavieProductDetail

# 导入产品详情基础模型
from .favie_product_detail_base import FavieProductDetailBase

# 导入产品评论模型
from .favie_product_review import FavieProductReview

# 导入产品评论汇总模型
from .favie_product_review_summary import FavieProductReviewSummary

# 定义模块的公开接口
__all__ = [
    # 基础数据模型
    "Price",
    "Images",
    "CategoryItem",
    "Video",
    "Brand",
    "AttributeItem",
    "PlatformChoice",
    "SellerRank",
    "Seller",
    "Inventory",
    "Deal",
    "ReturnPolicy",
    "RatingBreakdown",
    "SimpleProduct",
    "Promotion",
    "ExtendedInfo",
    "ReviewSummary",
    # 产品信息分组模型
    "BaseInfo",
    "AttrInfo",
    "DescInfo",
    "MediaInfo",
    "PriceInfo",
    "SaleInfo",
    # 分类预测响应
    "FavieCategoriesPredictResponse",
    # 主要产品模型
    "FavieProductDetail",
    "FavieProductDetailBase",
    "FavieProductReview",
    "FavieProductReviewSummary",
    # 工具类
    "HistoricalPricesDeserializer",
]

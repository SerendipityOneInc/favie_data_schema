# 导入网页相关模型类
from .favie_webpage import (  # 媒体数据模型; 网页作者信息; 字幕块; 评论相关; 主要网页模型
    FavieWebpage,
    ImageData,
    ProductData,
    ReferenceData,
    VideoData,
    WebpageAuthor,
    WebpageComment,
    WebpageReviewSummary,
    WebpageSubtitleChunk,
)

# 定义模块的公开接口
__all__ = [
    # 媒体数据模型
    "ImageData",
    "VideoData",
    "ReferenceData",
    "ProductData",
    # 网页作者信息
    "WebpageAuthor",
    # 字幕块
    "WebpageSubtitleChunk",
    # 评论相关
    "WebpageComment",
    "WebpageReviewSummary",
    # 主要网页模型
    "FavieWebpage",
]

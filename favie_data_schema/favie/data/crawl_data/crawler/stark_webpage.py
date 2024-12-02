'''
Author: ace-srp ace@srp.one
Date: 2024-12-02 17:59:25
LastEditors: ace-srp ace@srp.one
LastEditTime: 2024-12-02 18:44:33
FilePath: /favie_data_schema/favie_data_schema/favie/data/crawl_data/crawler/stark_webpage.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

from typing import List, Optional
from pydantic import BaseModel

class WebpageImage(BaseModel):
    url: Optional[str] = None
    desc: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None

class WebpageVideo(BaseModel):
    url: Optional[str] = None
    desc: Optional[str] = None

class WebpageProduct(BaseModel):
    url: Optional[str] = None
    title: Optional[str] = None
    subhead: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None
    images: Optional[List[WebpageImage]] = None
    videos: Optional[List[WebpageVideo]] = None

class WebpageReference(BaseModel):
    url: Optional[str] = None
    desc: Optional[str] = None

class WebpageItem(BaseModel):
    url: Optional[str] = None
    host: Optional[str] = None
    domain: Optional[str] = None
    favicon: Optional[str] = None
    language: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    author: Optional[str] = None
    keywords: Optional[List[str]] = None
    robots: Optional[List[str]] = None
    content: Optional[str] = None # text content of the webpage
    content_type: Optional[str] = None
    excerpt: Optional[str] = None
    comments: Optional[List[str]] = None
    subtitles: Optional[List[str]] = None
    images: Optional[List[WebpageImage]] = None
    videos: Optional[List[WebpageVideo]] = None
    references: Optional[List[WebpageReference]] = None
    products: Optional[List[WebpageProduct]] = None
    json_lds: Optional[List[str]] = None
    open_graphs: Optional[List[str]] = None
    twitter_cards: Optional[List[str]] = None
    page_type: Optional[str] = None
    ext_data: Optional[str] = None
    create_time: Optional[str] = None
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional, Union
from uuid import UUID

from pydantic import BaseModel, Field


class RedditPost(BaseModel):
    id: Optional[str]
    type_name: Optional[str]
    oid: Optional[str]
    uid: Optional[str]
    url: Optional[str]
    upvotes_count: Optional[str]
    comments_count: Optional[str]
    creation_time: Optional[str]
    json_data: Optional[str]
    crawl_time: Optional[str]

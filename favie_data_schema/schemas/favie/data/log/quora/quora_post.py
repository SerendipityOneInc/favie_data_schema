from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional, Union
from uuid import UUID

from pydantic import BaseModel, Field


class QuoraPost(BaseModel):
    id: Optional[str]
    type_name: Optional[str]
    id_str: Optional[str]
    oid: Optional[str]
    uid: Optional[str]
    url: Optional[str]
    views_count: Optional[str]
    upvotes_count: Optional[str]
    shares_count: Optional[str]
    comments_count: Optional[str]
    creation_time: Optional[str]
    updated_time: Optional[str]
    cursor: Optional[str]
    json_raw: Optional[str]
    crawl_time: Optional[str]

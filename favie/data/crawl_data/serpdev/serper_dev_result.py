
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict, Union
from uuid import UUID

from pydantic import BaseModel, Field


class SearchParameters(BaseModel):
    q: str
    gl: str
    hl: str
    autocorrect: bool
    page: int
    type: str


class Attributes(BaseModel):
    Headquarters: str
    CEO: str
    Founded: str
    Sales: str
    Products: str
    Founders: str
    Subsidiaries: str


class KnowledgeGraph(BaseModel):
    title: str
    type: str
    website: str
    imageUrl: str
    description: str
    descriptionSource: str
    descriptionLink: str
    attributes: Attributes


class Sitelinks(BaseModel):
    title: str
    link: str


class Organic(BaseModel):
    title: str
    link: str
    snippet: str
    sitelinks: Optional[List[Sitelinks]]
    position: int
    date: Optional[str]


class PeopleAlsoAsk(BaseModel):
    question: str
    snippet: str
    title: str
    link: str


class RelatedSearches(BaseModel):
    query: str


class SerperDevResult(BaseModel):
    searchParameters: SearchParameters
    knowledgeGraph: KnowledgeGraph
    organic: List[Organic]
    peopleAlsoAsk: List[PeopleAlsoAsk]
    relatedSearches: List[RelatedSearches]

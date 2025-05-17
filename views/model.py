# -*- coding: utf-8 -*-
"""
@Author: ZBY
@date: 2025/05/10
@Description: 
"""
from typing import Optional

from pydantic import BaseModel


class BodyModel(BaseModel):
    id: str
    age: int
    name: str


class QueryModel(BaseModel):
    number: Optional[int] = None

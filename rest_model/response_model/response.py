# -*- coding: utf-8 -*-
"""
@Author: ZBY
@date: 2025/05/10
@Description: 一些常用的响应
"""
from typing import Optional, Union

from pydantic import BaseModel

from rest_model.base_response import BaseResponse


class SuccessRespWithData(BaseResponse):
    """
    带有data字段的成功的响应
    """
    code: int = 200
    message: str = "success"
    data: Optional[Union[dict, BaseModel]] = None


class FailedResp(BaseResponse):
    """
    失败响应
    """
    code: int = 500


class FailedRespWithData(FailedResp):
    """
    带有data字段的失败响应
    """
    data: Optional[Union[dict, BaseModel]] = None

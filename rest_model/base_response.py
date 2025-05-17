# -*- coding: utf-8 -*-
"""
@Author: ZBY
@date: 2025/05/10
@Description: 
"""
from flask import Response, make_response
from pydantic import BaseModel


class BaseResponse(BaseModel):
    """
    响应必有code和message
    """
    code: int = 500
    message: str = ""


def make_flask_response(model: BaseModel, status_code=400) -> Response:
    js = model.model_dump_json()
    response = make_response(js, status_code)
    response.mimetype = "application/json"

    return response

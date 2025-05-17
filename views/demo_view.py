# -*- coding: utf-8 -*-
"""
@Author: ZBY
@date: 2025/05/10
@Description: 一个实例的demo请求
"""
from typing import Optional

from flask import Blueprint
from pydantic import BaseModel

from request.flask_view import FlaskView
from rest_model.base_response import BaseResponse
from views.model import QueryModel, BodyModel

test_view = Blueprint("test_view", __name__)


class GetSquare(FlaskView):
    """
    Get请求，返回一个json串uuid
    """

    def validate(self) -> Optional[BaseModel]:
        pass

    def handle_request(self) -> BaseModel:
        pass


class PostSquare(FlaskView):
    """
    post请求
    """
    request_param = QueryModel
    request_body = BodyModel

    def validate(self) -> Optional[BaseModel]:
        raise ValueError("sdffff")

    def handle_request(self) -> BaseModel:
        return BaseResponse(message="成功")

    methods = ["post"]


test_view.add_url_rule("/get_square", view_func=GetSquare.as_view("get_square"))
test_view.add_url_rule("/post_square", view_func=PostSquare.as_view("post_square"))

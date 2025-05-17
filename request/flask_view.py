# -*- coding: utf-8 -*-
"""
@Author: ZBY
@date: 2025/05/10
@Description: flask view 视图基类
"""
import abc
from abc import ABCMeta
from typing import Optional, Type

from flask import request
from flask.views import View
from pydantic import BaseModel, ValidationError

from common.common_request_class import CommonRequest
from common.global_var import COMMON_REQ
from common.my_exception import CommonException, ReqValidError
from rest_model.base_response import make_flask_response
from rest_model.response_model.response import FailedRespWithData
from utils.request_context import RequestContext
from utils.log_utils import log


class FlaskView(View, metaclass=ABCMeta):
    """
    视图函数基类
    """
    # 以下子类需要重写这些变量
    request_param: Optional[Type[BaseModel]] = None
    request_body: Optional[Type[BaseModel]] = None
    request_form: Optional[Type[BaseModel]] = None
    request_header = None

    # 接口请求类型
    methods = ["GET"]

    err = dict()

    # 私有变量, p代表param形成的BaseModel子类，b代表body形成的BaseModel子类，无需关注
    __p, __b = None, None

    @abc.abstractmethod
    def validate(self) -> Optional[BaseModel]:
        pass

    @abc.abstractmethod
    def handle_request(self) -> BaseModel:
        """
        返回一个BaseModel模型，用于响应请求
        """
        pass

    def post_request(self) -> None:
        return None

    def dispatch_request(self):

        log.info(f"flask request is enter")

        # 第一步，校验请求参数格式
        self.validate_request()
        if self.err:
            log.error("request validate failed.")
            return make_flask_response(FailedRespWithData(message="请求参数校验失败", data=self.err))

        # 如果检验成功，则封装请求参数，并且置于上下文中
        self.convert_request()

        # 第二步，用户自定义子类的业务校验， 可以直接抛出异常或者直接返回BaseModel模型
        result = self.validate()
        # 如果用户子类直接返回响应，则基类也直接返回响应
        if result:
            return result

        # 第三步，实际请求的逻辑
        result = self.handle_request()

        if not isinstance(result, BaseModel):
            raise CommonException(message="返回的响应不是BaseModel类型!")

        # 第四步，请求后处理
        self.post_request()

        log.info("flask request class is exit")

        return make_flask_response(result)

    def validate_request(self):
        """
        现在仅支持param和body参数
        """
        # post方法子类必须定义request_body或者request_params参数为BaseModel类型
        if ("post" in self.methods or "POST" in self.methods) and not self.request_body and not self.request_param:
            raise ReqValidError(message="post方法必须包含param或者body其中之一")

        url_params: Optional[dict] = None
        request_data: Optional[dict] = None
        if request.args:
            url_params = request.args.to_dict(flat=True)

        if request.get_json():
            request_data = request.get_json()

        # 开始校验
        try:
            if self.request_param:
                self.__p = self.request_param(**url_params)

        except ValidationError as ve:
            self.err["request_params"] = ve.errors()

        try:
            if self.request_body:
                self.__b = self.request_body(**request_data)
        except ValidationError as ve:
            self.err["request_body"] = ve.errors()

    def convert_request(self):
        common_request = CommonRequest(self.__p, self.__b)
        RequestContext.set_property(COMMON_REQ, common_request)

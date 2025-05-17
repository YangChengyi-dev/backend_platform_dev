# -*- coding: utf-8 -*-
"""
@Author: ZBY
@date: 2025/05/10
@Description: flask请求通用类，封装flask请求的参数
"""

from pydantic import BaseModel


class CommonRequest:
    """
    CommonReqeust类用于承载flask请求参数
    """

    def __init__(self, reqeust_param: BaseModel, request_body: BaseModel, request_form=None, request_header=None):
        """
        构造函数
        """
        # http请求param
        self.request_param = reqeust_param
        # http请求头
        self.request_header = request_header
        # http请求体，json格式
        self.request_body = request_body
        # http请求表格
        self.request_form = request_form

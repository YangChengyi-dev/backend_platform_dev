# -*- coding: utf-8 -*-
"""
@Author: ZBY
@date: 2025/05/10
@Description: 项目中的异常
"""
from common.base_exception import ApiException


class CommonException(ApiException):
    """
    通用异常
    """
    message = "内部错误"


class InputParamError(ApiException):
    """
    输入参数有误
    """
    message = "输入参数有误"


class FileNotExistsError(ApiException):
    """
    文件找不到
    """
    message = "文件找不到"


class ConstructError(ApiException):
    """
    构造函数异常
    """
    message = "构造函数异常"


class ReqValidError(ApiException):
    message = "请求校验失败"

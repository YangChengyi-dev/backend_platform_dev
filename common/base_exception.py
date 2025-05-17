# -*- coding: utf-8 -*-
"""
@Author: ZBY
@date: 2025/05/10
@Description: 
"""
import traceback

from flask import jsonify
from flask.app import HTTPException


class ApiException(HTTPException):
    """
    项目定义的restful接口和普通异常的顶级异常，所有flask异常均继承此异常
    """
    code = 500
    message = "failed"
    error_code = 500

    def __init__(self, message):
        """
        构造函数仅可以指定message
        """
        super().__init__()
        self.message = message

    @property
    def get_message(self):
        """
        return 报错信息
        """
        return self.message

    @property
    def trace_back(self):
        """
        异常堆栈
        """
        return traceback.format_exc()

    def get_body(self, environ=None):
        return jsonify({
            "code": self.error_code,
            "message": self.message,
        })

    def __str__(self):
        return f"error code: [{self.error_code}]; err msg: [{self.message}]"

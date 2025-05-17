# -*- coding: utf-8 -*-
"""
@Author: ZBY
@date: 2025/05/10
@Description: 基于flask g对象实现线程请求中的线程上下文，仅只能用于flask请求中
"""
from flask import g
from utils.log_utils import log


class RequestContext:
    """
    基于g对象的线程上下文，需要在app flask环境中使用，如果脱离flask框架，需要加上
    with app.app_context():
        RequestContext.get_property("xxx")
    """

    @staticmethod
    def get_property(property_name: str):
        value = g.__getattr__(property_name)
        log.info(f"request context get [{property_name}], value is [{str(value)}]")
        return value

    @staticmethod
    def set_property(property_name: str, _object):
        log.info(f"request context set [{property_name}], value is [{str(_object)}]")
        g.__setattr__(property_name, _object)

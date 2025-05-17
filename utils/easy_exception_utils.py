# -*- coding: utf-8 -*-
"""
@Author: ZBY
@date: 2025/05/10
@Description: 异常处理
"""

from common.my_exception import CommonException


class EasyExceptionUtils(object):

    @staticmethod
    def object_not_null(message, _object):
        """
        判断单个对象非空，为空则抛异常
        """
        if _object is None or not _object:
            raise CommonException(message)

    @staticmethod
    def need_true(message, param: bool):
        """
        判断表达式为True, 为false则抛异常
        """
        if not param:
            raise CommonException(message)

    @staticmethod
    def all_object_not_null(message, *args):
        """
        判断所有传入对象非空，任意一个为空则抛异常
        """
        if not args:
            raise CommonException(message)

        for elem in args:
            if not elem:
                raise CommonException(message)

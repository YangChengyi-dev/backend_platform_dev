# -*- coding: utf-8 -*-
"""
@Author: ZBY
@date: 2025/05/10
@Description: 字符串工具
"""
from common.my_exception import InputParamError


class StringUtils(object):

    @staticmethod
    def convert_string2bool(string: str) -> bool:
        """
        string到bool类型的转换
        :param string:
        :return:
        """
        string_uppercase = string.upper()
        if string_uppercase == "TRUE":
            return True
        elif string_uppercase == "FALSE":
            return False
        else:
            raise InputParamError(f"string [{string}] is invalid.")

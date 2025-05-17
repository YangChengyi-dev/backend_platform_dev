# -*- coding: utf-8 -*-
"""
@Author: ZBY
@date: 2025/05/10
@Description: 配置类读取，包含一些项目常用关键全局变量
"""
import abc
import configparser
import os.path
from typing import Any

import yaml
from common.my_exception import FileNotExistsError

FILE_TYPE_LIST = ["ini", "yaml"]


class BaseConfig(object):

    def __init__(self, file_path):
        self.path = file_path
        self.config = None

    @abc.abstractmethod
    def get(self, section, item):
        pass


class IniConfigUtils(BaseConfig):

    def __init__(self, file_path):
        """
        Ini配置文件的读取
        :param file_path: 配置文件
        """
        super(IniConfigUtils, self).__init__(file_path)
        if not os.path.exists(file_path):
            raise FileNotExistsError(f"config path [{file_path}] is not exists.")
        self.config = configparser.ConfigParser()
        self.config.read(file_path)

    def get(self, section, item):
        try:
            value = self.config.get(section, item)
        except Exception:
            return None
        return value


class YamlConfigUtils(BaseConfig):

    def __init__(self, file_path):
        super(YamlConfigUtils, self).__init__(file_path)
        self.config = yaml.load(open(file_path, encoding="utf8"), Loader=yaml.FullLoader)

    def get(self, section, item) -> Any:
        """
        yaml格式比较多，这里仅用于拿到key value形式的数据，后续可以扩展
        如：
        person:
         - age: 18
         - name :zzz
        :param section: key: person
        :param item: value: age
        :return: 18
        """
        try:
            value = self.config[section][item]
        except Exception:
            return None
        return value

    def get_yaml(self):
        return self.config

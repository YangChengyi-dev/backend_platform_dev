# -*- coding: utf-8 -*-
"""
@Author: ZBY
@date: 2025/05/10
@Description: 底层库的日志类，应用层可以继承实现
"""
import os
import time

import loguru
from loguru import logger
from loguru._logger import Logger

from common.global_var import BASE_DIR
from utils import ini_config
from utils.singleton_utils import singleton
from utils.string_utils import StringUtils


class BaseLogConfig:

    def __init__(self):
        self.log_path = ini_config.get("Log", "logPath")
        self.rotation = ini_config.get("Log", "rotation")
        self.retention = ini_config.get("Log", "retention")
        self.isMutilProcess = StringUtils.convert_string2bool(ini_config.get("Log", "isMutilProcess"))
        self.log_dir = os.path.join(BASE_DIR, self.log_path)
        self.time = time.strftime('%Y%m%d')
        self.pid = 0
        if self.isMutilProcess:
            self.pid = os.getpid()

    def get_log_from_config(self, bind_name: str) -> Logger:
        logger.add(
            f"{self.log_dir}/app_{self.time}_{self.pid}.log",
            rotation=self.rotation,
            encoding="utf8",
            enqueue=True,
            retention=self.retention,
            level="DEBUG",
            format="[{time:YYYY-MM-DD HH:mm:ss}|{thread}|{level}|{file}:{line}]  {message}"
        )

        return logger.bind(name=bind_name)


class ProfileLogConfig(BaseLogConfig):
    def __init__(self):
        super(ProfileLogConfig, self).__init__()

    def get_log_from_config(self, bind_name: str = "profile"):
        logger.add(
            f"{self.log_dir}/app_{self.time}_{self.pid}.plog",
            encoding="utf8",
            enqueue=True,
            level="INFO",
            format="[{time:YYYY-MM-DD HH:mm:ss}|{thread}|{level}]  {message}"
        )
        return logger.bind(name=bind_name)


@singleton
class BaseLogging(object):

    def __init__(self):
        """
        基础日志类
        """
        self.__logger: Logger = BaseLogConfig().get_log_from_config("base")

    def get_logger(self) -> Logger:
        return self.__logger


class ProfileLog(BaseLogging):

    def __init__(self):
        super(ProfileLog, self).__init__()
        self.__logger: loguru.logger = ProfileLogConfig().get_log_from_config()


log = BaseLogging().get_logger()

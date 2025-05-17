# -*- coding: utf-8 -*-
"""
@Author: ZBY
@date: 2025/05/10
@Description: 
"""
from utils.log_utils import BaseLogging

if __name__ == '__main__':
    log = BaseLogging().get_logger()
    log1 = BaseLogging().get_logger()
    log.debug("this is debug")
    log.info("this is info")
    log.error("this is err")
    log1.error("this is err")
    log1.error("this is err")
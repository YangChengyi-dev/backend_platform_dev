# -*- coding: utf-8 -*-
"""
@Author: ZBY
@date: 2025/05/10
@Description: 
"""
import os

# 项目的根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 主体配置文件
BASE_INI_CONFIG_FILE_PATH = os.path.join(BASE_DIR, "base_config", "base_config.ini")

# 全局变量
COMMON_REQ = "common_req"

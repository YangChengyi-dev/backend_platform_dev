import pytest

from utils.config_utils import IniConfigUtils, YamlConfigUtils


@pytest.fixture
def init_ini_config():
    config = IniConfigUtils("../test_data/config.ini")
    return config


@pytest.fixture
def init_yml_config():
    config = YamlConfigUtils("../test_data/config.yaml")
    return config


class TestConfigUtils:

    def test_ini(self, init_ini_config):
        assert init_ini_config.get("mysql", "pass") == "1222"
        assert init_ini_config.get("log", "aaa") == "bbb"
        assert init_ini_config.get("mysql", "xxx") is None
        assert init_ini_config.get("log", "ttt") is None

    def test_yaml(self, init_yml_config):
        assert init_yml_config.get("log", "time1") == 111
        assert init_yml_config.get("log", "time2") == "222"
        assert init_yml_config.get("mysql", "pass") == "jade"
        assert init_yml_config.get("mysql", "port") is None
        assert init_yml_config.get("model", "port") is None

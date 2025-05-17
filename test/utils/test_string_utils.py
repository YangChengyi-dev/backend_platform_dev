import pytest

from common.base_exception import InputParamError
from utils.string_utils import StringUtils


class TestStringUtils:

    def test_convert_string2bool(self):
        string = "true"
        res = StringUtils.convert_string2bool(string)
        assert res is True

        string = "TrUe"
        res = StringUtils.convert_string2bool(string)
        assert res is True

        string = "false"
        res = StringUtils.convert_string2bool(string)
        assert res is False

        string = "False"
        res = StringUtils.convert_string2bool(string)
        assert res is False

        string = "no"
        with pytest.raises(InputParamError):
            StringUtils.convert_string2bool(string)

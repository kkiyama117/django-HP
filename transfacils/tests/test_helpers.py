import os

import pytest

from conftest import is_omit_test
from transfacils.helpers import get_trans_api_data, initializer


class GetAPIDataTest:
    @pytest.mark.parametrize(('line_cd', 'line_name'), [
        (33001, "京阪本線"),
    ])
    def test_line_data(self, line_cd, line_name):
        assert get_trans_api_data.get_line_data(line_cd) == {
            "line_cd": line_cd,
            "line_name": line_name}

    @pytest.mark.parametrize(('station_cd', 'station_name'), [
        (3300142, "出町柳"),
    ])
    def test_station_data(self, station_cd, station_name):
        station_data = get_trans_api_data.get_station_data(station_cd)
        assert station_data["station_cd"] == station_cd
        assert station_data["station_name"] == station_name


class InitializerTest:

    @pytest.mark.skipif(is_omit_test() is True, reason='not all test')
    def test_initialize_db(self):
        initializer.initialize_lines_db("test_data2.json")
        base_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "fixtures")
        with open(os.path.join(base_dir, "test_data.json"), "r") as f1, open(
                os.path.join(base_dir, "test_data2.json"), "r") as f2:
            assert f1.read() == f2.read()

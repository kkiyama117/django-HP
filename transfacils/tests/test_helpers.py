import pytest

from transfacils.helpers import get_trans_api_data


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

from transfacils.helpers import get_trans_api_data


class Get_api_data:
    def test_line_data(self, line_cd):
        assert get_trans_api_data.get_line_data() == {"line_cd": line_cd,
                                                      "line_name": "京阪本線"}

    def test_station_data(self):
        pass

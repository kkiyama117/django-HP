import json
import os

from transfacils import models
from transfacils.helpers.get_trans_api_data import line_data_generator, \
    get_line_data


def initialize():
    initialize_lines_db()


def initialize_lines_db(filename: str = "initial_data.json"):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(base_dir, "fixtures/", filename), "w") as file:
        data_list = initialize_line_data()
        json.dump(data_list, file, sort_keys=True, ensure_ascii=False,
                  indent=4)


def initialize_line_data():
    data_dicts = []
    line = get_line_data()
    line_dict = {"model": "transfacils.route", "pk": line["line_cd"],
                 "fields": {"name": line["line_name"],
                            "kind": models.Route.TRAIN}}
    data_dicts.append(line_dict)
    for station in line_data_generator():
        data_dict = {"model": "transfacils.station",
                     "pk": station["station_cd"],
                     "fields": {"name": station["station_name"],
                                "route": station["line_cd"],
                                "group_cd": station["station_g_cd"],
                                "next_station": station["next"],
                                "previous_station": station["previous"]}}
        data_dicts.append(data_dict)
    return data_dicts

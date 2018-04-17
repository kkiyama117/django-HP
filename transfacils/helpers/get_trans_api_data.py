import requests
from bs4 import BeautifulSoup


def gen_helper(url):
    # Requestsを使って、webから取得
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    return BeautifulSoup(r.text, 'lxml-xml')


# LINE
def lines_generator(prefecture_cd=26):
    """路線図一覧

    Args:
        prefecture_cd (int): 都道府県番号

    Returns:
        dict: { "line_cd": `int` , "line": `str` }

    """
    url = "http://www.ekidata.jp/api/p/{0}.xml".format(prefecture_cd)
    lines = gen_helper(url).find_all("line")
    for line in lines:
        line_cd = int(line.find("line_cd").string)
        line_name = line.find("line_name").string
        yield {"line_cd": line_cd,
               "line": line_name}


def get_line_data(line_cd=33001):
    url = "http://www.ekidata.jp/api/l/{0}.xml".format(line_cd)
    line = gen_helper(url).find("line")
    return {"line_cd": int(line.find("line_cd").string),
            "line_name": line.find("line_name").string}


# LINE -> STATION

def line_station_generator(line_cd=33001):
    """路線中の駅のジェネレーター

    Args:
        line_cd (int): 路線番号

    Yields:
        `get_station_data`

    """
    url = "http://www.ekidata.jp/api/l/{0}.xml".format(line_cd)
    line = gen_helper(url)
    stations = line.find_all("station")
    for station in stations:
        station_cd = int(station.find("station_cd").string)
        yield get_station_data(station_cd)


def line_data_generator(line_cd=33001):
    for station in line_station_generator(line_cd):
        near_dict = get_near_station_in_line(station["station_cd"])
        station.update(near_dict)
        yield station


def get_near_station_in_line(line_cd, station_cd):
    url = "http://www.ekidata.jp/api/n/{0}.xml".format(line_cd)
    line = gen_helper(url)
    next_station = None
    previous_station = None
    for station_join in line.find_all("station_join"):
        if station_join.find(name="station_cd1", text=str(station_cd)):
            previous_station = int(station_join.find("station_cd2").string)
        if station_join.find(name="station_cd2", text=str(station_cd)):
            next_station = int(station_join.find("station_cd1").string)
    return {"next": next_station, "previous": previous_station}


# STATION

def get_station_data(station_cd):
    """駅のデータの取得

    Args:
        station_cd: 駅番号

    Returns:
        dict
    """
    url = "http://www.ekidata.jp/api/s/{0}.xml".format(station_cd)
    station = gen_helper(url)
    station_cd = int(station.find("station_cd").string)
    station_name = station.find("station_name").string
    station_g_cd = int(station.find("station_g_cd").string)
    line_cd = int(station.find("line_cd").string)
    line_name = station.find("line_name").string
    station_info = {"station_cd": station_cd, "station_name": station_name,
                    "station_g_cd": station_g_cd, "line_cd": line_cd}
    return station_info


# STATION -> STATIONS

def get_station_route_list(station_id):
    url = "http://www.ekidata.jp/api/g/{0}.xml".format(station_id)
    groups = gen_helper(url).find_all("station_g")
    line_list = []
    for group in groups:
        cd = int(group.find("line_cd").string)
        line_list.append(cd)
    return line_list

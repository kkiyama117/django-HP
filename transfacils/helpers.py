import requests
from bs4 import BeautifulSoup


def gen_helper(url):
    # Requestsを使って、webから取得
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    return BeautifulSoup(r.text, "lxml-xml")


def lines_data_generator(prefecture_id=26):
    url = "http://www.ekidata.jp/api/p/{0}.xml".format(prefecture_id)
    lines = gen_helper(url).find_all("line")
    for line in lines:
        line_cd = line.find("line_cd").string
        line_name = line.find("line_name").string
        yield {"line_cd": line_cd,
               "line": line_name}


def line_data_generator(line_id=33001):
    url = "http://www.ekidata.jp/api/l/{0}.xml".format(line_id)
    line = gen_helper(url)
    stations = line.find_all("station")
    for station in stations:
        yield {"station_name": station.find("station_name").string}


if __name__ == '__main__':
    for i in line_data_generator():
        print(i)

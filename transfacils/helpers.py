import requests
from bs4 import BeautifulSoup


def trans_data_generator(prefecture_id=26):
    url = "http://www.ekidata.jp/api/p/{0}.xml".format(prefecture_id)
    # Requestsを使って、webから取得
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    bs = BeautifulSoup(r.text, "lxml-xml")
    lines = bs.find_all("line")
    for line in lines:
        line_cd = line.find("line_cd").string
        line_name = line.find("line_name").string
        yield {"line_cd": line_cd,
               "line": line_name}


if __name__ == '__main__':
    for i in trans_data_generator():
        print(i)

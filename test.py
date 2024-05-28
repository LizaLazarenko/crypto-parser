import json
import requests
import lxml
from bs4 import BeautifulSoup as bs

from currency.currency import Currency
from market.ascendex import Ascendex
from market.gate_io import GateIo
from market.huobi import Huobi
from market.mexc import Mexc

res = requests.get("https://futures.mexc.com/api/v1/contract/depth_step/BTC_USDT")
print("res")
print(res.text)
# Парсим ответ с помощью lxml - библиотеки для обработки xml
soup = bs(res.text, "lxml")
print("soup")
print(soup)
# Парсим результат soup в json
load = json.loads(soup.text)
print("load")
print(load)
print("prices: ")
print("asks: ", load["data"]["asks"], "bids: ", load["data"]["bids"])

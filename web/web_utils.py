import json
import requests
import lxml
from bs4 import BeautifulSoup as bs

from currency.currency import Currency
from market.ascendex import Ascendex
from market.gate_io import GateIo
from market.huobi import Huobi
from market.mexc import Mexc


def init_markets():
    return [Mexc(), GateIo(), Huobi(), Ascendex()]


def parse_currency(main_currency, second_currency, currs):
    markets = init_markets()

    # Словарь с биржами для валюты и ценами в них
    prices = {}

    for market in markets:
        try:
            # Подменить в шаблоне url строки на нужные валюты
            url = market.get_api_url(main_currency, second_currency)
            # Создание запроса GET к нашему URL, сохраняем ответ в res
            res = requests.get(url)
            # Парсим ответ с помощью lxml - библиотеки для обработки xml
            # Warning - MarkupResemblesLocatorWarning: The input looks more like a filename than markup. You may want
            # to open this file and pass the filehandle into Beautiful Soup.
            #   soup = bs(res.text, "lxml")
            # нормальный
            soup = bs(res.text, "lxml")
            # Парсим результат soup в json
            load = json.loads(soup.text)
            # Сохранение цены после парсинга в каждой бирже
            price = market.get_prices(load)
            prices[market.name] = price
        except:
            price = market.get_prices('')
            prices[market.name] = price

    currency = Currency(main_currency, prices)

    currs.append(currency)

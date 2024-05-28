import datetime
import pprint
from time import sleep

from utils import csv_utils
from web import web_utils
from currency.currency import Currency
from threading import Thread
import currency.static as static

currencies = []
threads = []
second_curr = "usdt"


def main():
    # Создаем название для файла с текущей датой
    file_name = datetime.datetime.now().strftime("%m.%d.%Y %H-%M-%S")
    # Создаем потоки для каждой валюты
    for curr in static.currencies:
        threads.append(Thread(target=web_utils.parse_currency, args=(curr, second_curr, currencies)))
    # Начинаем потоки
    for t in threads:
        t.start()
    # Ждем окончания потоков
    for t in threads:
        t.join()
    # Сохранение в файл данных
    csv_utils.save_currencies(currencies, "results/" + file_name)


# main файл
if __name__ == "__main__":
    main()

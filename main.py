import datetime

from utils import csv_utils
from threading import Thread
import currency.static as static

currencies = []
threads = []
second_curr = "usdt"


def main():
    # Создаем файл с текущей датой
    file_name = datetime.datetime.now().strftime("%m.%d.%Y %H-%M-%S")
    # Создаем потоки для каждой валюты
    for curr in static.currencies:
        threads.append(Thread())
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

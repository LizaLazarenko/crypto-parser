import csv
import os
from currency.currency import Currency


def save_currencies(currencies: list[Currency], file_name: str):
    # Создание нужного файла
    os.makedirs(os.path.dirname(file_name), exist_ok=True)

    with open(file_name + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Начинаем создавать заголовки
        header_row = ["Currency"]
        for n in currencies[0].markets:
            # Создаем заголовки с названиями бирж и действием
            header_row.append(f"Asks {n}")
            header_row.append(f"Bids {n}")

        for i in range(6):
            # создаем 6 diff для 4 бирж
            header_row.append("diff")

        # записываем заголовки
        writer.writerow(header_row)

        for curr in currencies:
            # Записываем название валюты
            row = [curr.name]
            for m in curr.markets:
                try:
                    # Записываем первые значения asks и bids
                    row.append(curr.markets[m]["asks"][0][0])
                    row.append(curr.markets[m]["bids"][0][0])
                except:
                    row.append("unavailable")
                    row.append("unavailable")
            for m in curr.get_diff():
                row.append(m)
            writer.writerow(row)

    print("saved as " + file_name)

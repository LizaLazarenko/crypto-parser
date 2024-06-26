class Market:

    def __init__(self, name, url, upper_case):
        self.name = name
        self.url = url
        self.upper_case = upper_case

    def get_api_url(self, main_curr, second_curr):
        # проверка на флаг, какими буквами (заглавными или маленькими) писать
        if not self.upper_case:
            main_curr = main_curr.lower()
            second_curr = second_curr.lower()
        else:
            main_curr = main_curr.upper()
            second_curr = second_curr.upper()
        # Подменяем в шаблоне URL main на main_curr, second на second_curr, убираем пробелы
        return self.url.substitute(main=main_curr, second=second_curr).replace(" ", "")

    def get_prices(self, load):
        pass

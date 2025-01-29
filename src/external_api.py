import os
from typing import Any

import requests
from dotenv import load_dotenv

from src import decorators

load_dotenv(".env")

API_KEY = os.getenv("API_KEY_COURSE")


@decorators.log(filename="mylog.txt")
def currency_conversion(transactions: dict = {}) -> Any:
    """Функция выполняет конвертацию суммы. Сумма получает значение из словаря по ключу "operationAmount" -> "amount"
    В currency определяется тип валюты. По ссылке url, подставляется значение currency - "Тип валюты", amount - "Сумма"
    В response происходит вызов конвертации, отправка через API ключ по URL, получая значение с сервера
    конвертированной валюты в Рубли"""

    amount = float(transactions["operationAmount"]["amount"])  # Сумма из словаря транзакций
    currency = transactions["operationAmount"]["currency"]["code"]  # Значение кодировки валюты

    # Ключ апи для запроса по значению ключа, оформлен в виде словаря чтобы можно было использовать не сколько ключей
    my_headers = {"apikey": API_KEY}

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    response = requests.request("GET", url, headers=my_headers)  # Вызов конвертации через метод GET
    result = response.json()  # Результат выводится в формате JSON

    return float(round(result.get("result"), 2))

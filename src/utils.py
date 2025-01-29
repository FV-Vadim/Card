import json
from typing import Any

from src import decorators
from src.external_api import currency_conversion


@decorators.log(filename="mylog.txt")
def get_json_transaction(filename: str = "") -> Any:
    """Функция принимает на вход путь до JSON-файла, возвращает список
    словарей с данными о финансовых транзакциях. Если файл пустой,
    содержит не список или не найден, функция возвращает пустой список."""

    try:
        transactions = json.load(open(filename, encoding="utf-8"))  # Открытие файла с кодировкой UTF-8
    except FileNotFoundError:  # Исключение если файл не найден
        return []  # Возвращает пустой список

    except json.decoder.JSONDecodeError:  # Если декодирование JSON файла не удалось
        return []  # Возвращает пустой список

    else:
        return transactions  # Возвращает список открытый из файла


@decorators.log(filename="mylog.txt")
def get_transaction_amount(transactions: dict) -> float | None:
    """Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.
    Если транзакция в RUB, то просто возвращает значение функции"""

    if isinstance(transactions, dict):
        transactions = [transactions]
        # Если транзакции являются не списком словарей, переводим в список

    print(transactions)  # Выводит список транзакций
    for transaction in transactions:
        # Возьмем значение из словаря
        if transaction["operationAmount"]["currency"]["code"] == "RUB":  # Если значение кодировки валюты равно рублю
            # Возвращаем значение суммы затраты

            return float(transaction["operationAmount"]["amount"])
        else:
            # Если кодировка валюты не равна рублям

            return float(currency_conversion(transaction))  # Конвертируем сумму в рубли

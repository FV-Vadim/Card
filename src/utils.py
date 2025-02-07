import json
import os
from typing import Any

from src import decorators
from src.external_api import currency_conversion
from src.logging import get_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../logs", "utils.log")
logger = get_logger("utils", file_path)


@decorators.log(filename="mylog.txt")
def get_json_transaction(filename: str = "") -> Any:
    """Функция принимает на вход путь до JSON-файла, возвращает список
    словарей с данными о финансовых транзакциях. Если файл пустой,
    содержит не список или не найден, функция возвращает пустой список."""

    try:
        logger.info("Открываем исходный JSON-файл и возвращаем Python объект список словарей.")
        transactions = json.load(open(filename, encoding="utf-8"))  # Открытие файла с кодировкой UTF-8
    except FileNotFoundError:  # Исключение если файл не найден
        logger.error("Файл не найден.")
        return []  # Возвращает пустой список

    except json.decoder.JSONDecodeError:  # Если декодирование JSON файла не удалось
        logger.error("Ошибка декодирования JSON файла.")
        return []  # Возвращает пустой список

    else:
        logger.info("Список транзакций успешно преобразован из JSON-файла, в Python объект.")
        return transactions  # Возвращает список открытый из файла


@decorators.log(filename="mylog.txt")
def get_transaction_amount(transactions: list[dict[str, Any]]) -> float | None:
    """Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.
    Если транзакция в RUB, то просто возвращает значение функции"""

    try:
        logger.info("Получаем сумму операции из словаря транзакции.")
        if isinstance(transactions, dict):
            logger.info("Транзакции являются не списком словарей, переводим в список")
            transactions = [transactions]
            # Если транзакции являются не списком словарей, переводим в список

        logger.info("Открываем исходный JSON-файл и возвращаем Python объект список словарей.")
        print(transactions)  # Выводит список транзакций

        for transaction in transactions:
            # Возьмем значение из словаря
            if (
                transaction["operationAmount"]["currency"]["code"] == "RUB"
            ):  # Если значение кодировки валюты равно рублю
                # Возвращаем значение суммы затраты

                sum_amount = float(transaction["operationAmount"]["amount"])  # Сумма из словаря транзакций

            else:
                # Если кодировка валюты не равна рублям

                sum_amount = currency_conversion(transaction)  # Конвертируем сумму в рубли

            logger.info(f"Сумма операции в рублях. {sum_amount} рублей.")
            return sum_amount
    except Exception as exception:
        logger.error(f"Ошибка при получении суммы операции: {str(exception)}")
        return None

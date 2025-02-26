import collections
import os
import re

from src.my_logging import get_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../logs", "search_operations.log")
logger = get_logger("search_operations", file_path)


def search_transactions_dict(transactions: list, query: str = "") -> list:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска, а возвращать список словарей с
    данными, у которых в описании есть данная строка.
    :return:
    """

    find_transactions = []

    logger.info(f"Обработка словаря: {transactions}, по запросу {query}")
    for transaction in transactions:
        description = transaction.get("description")

        if isinstance(description, str) and re.search(query, description, flags=re.IGNORECASE) is not None:
            find_transactions.append(transaction)

    logger.info(f"Обнаружено {len(find_transactions)} операций, содержащих запрос: {query}")
    return find_transactions


def transaction_category_count(transactions: list = [], categories: list = []) -> dict:
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий, а возвращает словарь,
    в котором ключи - категории, а значения - количество операций в каждой категории.
    :return:
    """

    transactions_categories_count = []

    logger.info(f"Обработка словаря: {transactions}, с категориями: {categories}")

    for transaction in transactions:
        try:
            if transaction["description"] in categories:
                transactions_categories_count.append(transaction["description"])
        except KeyError:
            logger.warning(f"Отсутствует описание для операции: {transaction}")
            continue

    result = collections.Counter(transactions_categories_count)
    logger.info(f"Подсчет категорий: {result}")
    result.subtract(categories)

    return dict(result)

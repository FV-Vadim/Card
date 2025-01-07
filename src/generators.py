from typing import Generator


def filter_by_currency(transactions: list, currency: str = "USD") -> Generator:
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)"""

    # Генератор с лямбда функцией который переходит в список словарей по ключу сравнивает значения и выдает результат
    result = list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions))
    yield result


def transaction_descriptions(transactions: list) -> Generator:
    """Генератор принимает список словарей с транзакциями и возвращает описание каждой поочередно"""

    # Генератор с лямбда функцией который переходит в словарь по ключу сравнивает значения и выдает результат
    result = map(lambda description: description["description"], transactions)
    for value_description in result:
        yield value_description


def card_number_generator(start: int, stop: int) -> Generator:
    """Функция генерирует номера банковских карт в заданном диапазоне
    в формате 'ХХХХ ХХХХ ХХХХ ХХХХ'"""

    if type(start) is int and type(stop) is int:  # Если значения старт и стоп число
        for number in range(start, stop):  # Цикл генерации значений
            number_card = "0" * (16 - len(str(number))) + str(number)  # Формирование числа из 16 символов
            yield f"{number_card[:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:17]}"
    else:  # Если значения старт и стоп не число
        yield "Ошибка: некорректный ввод"

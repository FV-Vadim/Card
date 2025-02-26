from typing import Any, Dict, List

from src import decorators


@decorators.log(filename="mylog.txt")  # Декорирование функции
def filter_by_state(list_of_dict: List[Dict[str, Any]], state: str = "EXECUTED") -> str | list[dict[str, Any]]:
    """Функция принимает на вход словарь list_of_dict,
    фильтрует словарь банковских операций по параметру state,
    записывает в словарь filtered_list_of_dict фильтрованный словарь."""

    if not list_of_dict:  # Если список пустой
        return "Словарь с данными отсутствует"

    if not state:  # Если значение state не передано
        state = "EXECUTED"

    filtered_list_of_dict = []  # Пустой список для фильтрованных значений

    for dictionary_key in list_of_dict:
        # Проверяем, есть ли ключ "state" в словаре
        if "state" in dictionary_key and dictionary_key["state"] == state:
            filtered_list_of_dict.append(dictionary_key)

    return filtered_list_of_dict


@decorators.log(filename="mylog.txt")  # Декорирование функции
def sort_by_date(list_of_dict: List[Dict[str, Any]], reverse_date: bool = True) -> str | list[dict[str, Any]]:
    """Функция sort_by_date принимает на вход словарь list_of_dict,
    ключ словаря лямбда функция со значением ключа: data
    направление "по возрастанию" или "по убыванию" зависит от булевого значения
    по умолчанию значение True"""

    if not list_of_dict or list_of_dict is None:  # Если словарь пустой или его нет
        return "Словарь с данными отсутствует"
    else:
        valid_records = [record for record in list_of_dict if "date" in record]
        sorted_list_of_dict = sorted(
            valid_records, key=lambda dictionary_key: dictionary_key["date"], reverse=reverse_date
        )  # возвращает значение сортировки
    return sorted_list_of_dict

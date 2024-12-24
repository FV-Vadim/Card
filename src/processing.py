from typing import Any, Dict, List


def filter_by_state(list_of_dict: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция принимает на вход словарь list_of_dict,
    фильтрует словарь банковских операций по параметру state,
    записывает в словарь filtered_list_of_dict фильтрованный словарь."""

    if list_of_dict is None:  # Если словарь пустой
        list_of_dict = []
    filtered_list_of_dict = []  # пустой словарь для фильтрованных значений

    for dictionary_key in list_of_dict:
        if dictionary_key["state"] == state:  # По заданному ключу state, сверяет значения
            filtered_list_of_dict.append(dictionary_key)  # Добавляет в словарь если значения совпали
    return filtered_list_of_dict


def sort_by_date(list_of_dict: List[Dict[str, Any]], reverse_date: bool = True) -> List[Dict[str, Any]]:
    """Функция sort_by_date принимает на вход словарь list_of_dict,
    ключ словаря лямбда функция со значением ключа: data
    направление "по возрастанию" или "по убыванию" зависит от булевого значения
    по умолчанию значение True"""

    if list_of_dict is None:  # Если словарь пустой
        list_of_dict = []
    return sorted(
        list_of_dict, key=lambda dictionary_key: dictionary_key["date"], reverse=reverse_date
    )  # возвращает значение сортировки

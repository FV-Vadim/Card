from typing import Any, Dict, List


def filter_by_state(list_of_dict: List[Dict[str, Any]], state: str = "EXECUTED") -> str | list[dict[str, Any]]:
    """Функция принимает на вход словарь list_of_dict,
    фильтрует словарь банковских операций по параметру state,
    записывает в словарь filtered_list_of_dict фильтрованный словарь."""

    if list_of_dict is None or not list_of_dict:  # Если словарь пустой или не имеет значений
        return "Словарь с данными отсутствует"
    else:
        filtered_list_of_dict = []  # пустой словарь для фильтрованных значений

        if not state or state is None:  # Если нет значения или значение является пустым
            state = "EXECUTED"
            for dictionary_key in list_of_dict:
                if dictionary_key["state"] == state:  # По заданному ключу state, сверяет значения
                    filtered_list_of_dict.append(dictionary_key)  # Добавляет в словарь если значения совпали
        else:
            for dictionary_key in list_of_dict:
                if dictionary_key["state"] == state:  # По заданному ключу state, сверяет значения
                    filtered_list_of_dict.append(dictionary_key)  # Добавляет в словарь если значения совпали
    return filtered_list_of_dict


def sort_by_date(list_of_dict: List[Dict[str, Any]], reverse_date: bool = True) -> str | list[dict[str, Any]]:
    """Функция sort_by_date принимает на вход словарь list_of_dict,
    ключ словаря лямбда функция со значением ключа: data
    направление "по возрастанию" или "по убыванию" зависит от булевого значения
    по умолчанию значение True"""

    if not list_of_dict or list_of_dict is None:  # Если словарь пустой или его нет
        return "Словарь с данными отсутствует"
    else:
        if not reverse_date:
            var_reverse_date = reverse_date is True
            sorted_list_of_dict = sorted(
                list_of_dict, key=lambda dictionary_key: dictionary_key["date"], reverse=var_reverse_date
            )  # возвращает значение сортировки
        else:
            sorted_list_of_dict = sorted(
                list_of_dict, key=lambda dictionary_key: dictionary_key["date"], reverse=reverse_date
            )  # возвращает значение сортировки
    return sorted_list_of_dict

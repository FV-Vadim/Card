def filter_by_state(list_of_dict: list = [], state: str = "EXECUTED") -> list:
    """
    Функция принимает на вход словарь list_of_dict,
    фильтрует словарь банковских операций по параметру state,
    записывает в словарь filtered_list_of_dict фильтрованный словарь.
    """

    filtered_list_of_dict = []  # пустой словарь для фильтрованных значений

    for dictionary in list_of_dict:
        if dictionary["state"] == state:  # По заданному ключу state, сверяет значения
            filtered_list_of_dict.append(dictionary)  # Добавляет в словарь если значения совпали
    return filtered_list_of_dict


def sort_by_date(list_of_dict: list = [], reverse_date: bool = True) -> list:
    """
    Функция sort_by_date принимает на вход словарь list_of_dict,
    ключ словаря лямбда функция со значением ключа: data
    направление "по возрастанию" или "по убыванию" зависит от булевого значения
    по умолчанию значение True
    """

    return sorted(
        list_of_dict, key=lambda dictionary: dictionary["date"], reverse=reverse_date
    )  # возвращает значение сортировки

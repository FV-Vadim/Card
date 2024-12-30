from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

# импорт функций при помощи абсолютным путём

"""Запрос функций, для маскировки номера карты в числовом значении, маскируется '*'. """

# Вывод функции
if __name__ == "__main__":

    print("____Homework_10_1_1____")  # упоминание какая по счету домашка №1
    # Вызов функции
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))

# импорт функций при помощи абсолютным путём

"""Запрос функций, для обработки информации и счетов."""

# Вывод функции
if __name__ == "__main__":

    print("____Homework_10_1_2____")  # упоминание какая по счету домашка №2
    # Вызов функции
    print(mask_account_card("Maestro", 1596837868705199))
    print(mask_account_card("Счет", 64686473678894779589))
    print(mask_account_card("MasterCard", 7158300734726758))
    print(mask_account_card("Счет", 35383033474447895560))
    print(mask_account_card("Visa Classic", 6831982476737658))
    print(mask_account_card("Visa Platinum", 8990922113665229))
    print(mask_account_card("Visa Gold", 5999414228426353))
    print(mask_account_card("Счет", 73654108430135874305))

# импорт функций при помощи абсолютным путём

"""Запрос функций, для обработки информации и счетов."""

# Вывод функции
if __name__ == "__main__":

    print("____Homework_10_1_3____")  # упоминание какая по счету домашка №3
    # Вызов функции
    print(get_date("2024-03-11T02:26:18.671407"))

# импорт функций при помощи абсолютным путём

"""Запрос функций, для фильтрации словаря банковских операций по параметру state."""

# Вывод функции
if __name__ == "__main__":

    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
        )
    )

# импорт функций при помощи абсолютным путём

"""Запрос функций, для сортировки словаря по дате, параметр: date."""

# Вывод функции
if __name__ == "__main__":

    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
        )
    )

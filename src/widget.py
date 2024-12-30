from typing import Union

from src.alphabetical import alphabetical
from src.masks import get_mask_account, get_mask_card_number  # импорт функций


def mask_account_card(name_card: str, number_card: Union[int, str]) -> str:
    """Функция обрабатывает информацию о картах и о счетах"""

    str_account_card = ""
    if not name_card and not number_card:
        str_account_card = "Введите тип и номер карты, счета."
    else:
        for letter in str(name_card).lower():
            if letter not in alphabetical:
                return "Введите сначала тип карты, а после номер"
            else:
                if len(str(number_card)) < 20:

                    number_card_mask = str(get_mask_card_number(number_card))  # шифрует номер счета

                    # Формирование строки пользователю: наименование карты
                    str_account_card = str(name_card.title()) + " " + str(number_card_mask)

                else:

                    number_count_mask = str(get_mask_account(number_card))  # шифрует номер счета

                    # Формирование строки пользователю: наименование счета
                    str_account_card = str(name_card.title()) + " " + str(number_count_mask)
            return str_account_card
    return str_account_card


def get_date(date: str) -> str:
    """Функция форматирует строку с датой в установленный образец (ДД.ММ.ГГГГ)"""

    if date is None or not date:
        return "Введите дату."
    else:
        format_date = date.split("T")

        new_format_date = format_date[0].split("-")

        return new_format_date[2] + "." + new_format_date[1] + "." + new_format_date[0]

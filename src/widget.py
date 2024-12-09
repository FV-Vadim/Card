from typing import Union

from src.masks import get_mask_account, get_mask_card_number  # импорт функций


def mask_account_card(name: str, number_card: Union[int, str]) -> str:
    """Функция обрабатывает информацию о картах и о счетах"""

    if len(str(number_card)) > 16:

        # если количество цифр номера больше 16, это счет

        number_card = str(get_mask_account(number_card))  # шифрует номер счета

    else:

        number_card = str(get_mask_card_number(number_card))  # шифрует номер карты

    str_account_card = str(name) + " " + str(number_card)

    return str_account_card


def get_date(date: str) -> str:
    """Функция форматирует строку с датой в установленный образец (ДД.ММ.ГГГГ)"""

    format_date = date.split("T")

    new_format_date = format_date[0].split("-")

    new_date = new_format_date[2] + "." + new_format_date[1] + "." + new_format_date[0]

    return new_date

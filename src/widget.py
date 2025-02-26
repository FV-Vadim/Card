from src import decorators
from src.masks import get_mask_account, get_mask_card_number  # импорт функций


@decorators.log(filename="mylog.txt")  # Декорирование функции
def mask_account_card(input_str: str) -> str:
    """
    Функция обрабатывает информацию о картах и о счетах

    :param input: Строка с информацией о карте или счете
    :return: Отформатированная информация
    """

    if "Счет" in input_str:
        return f"{input_str[0:len(input_str) - 20]}{get_mask_account(input_str[-20:])}"
    else:
        return f"{input_str[0:len(input_str) - 16]}{get_mask_card_number(input_str[-16:])}"


@decorators.log(filename="mylog.txt")  # Декорирование функции
def get_date(input_date: str) -> str:
    """Функция форматирует строку с датой в установленный образец (ДД.ММ.ГГГГ)"""

    splited_date = input_date.split("-")

    splited_date.reverse()

    splited_date[0] = splited_date[0][0:2]

    formated_date = ".".join(splited_date)

    return formated_date

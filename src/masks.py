from typing import Union


def get_mask_card_number(number_card: Union[int, str]) -> str:
    """Функция принимает на вход номер карты и шифрует его"""

    if number_card == list:
        for number_key in number_card:
            if len(number_key) > 16:
                str_number_key = str(number_key)  # Преобразование числа в строку
                str_number_key_no_space = ''
                for letter in str_number_key:
                    if letter != ' ':
                        str_number_key_no_space += letter
                    else:
                        continue
                return f"{str_number_key_no_space[0:4]} {str_number_key_no_space[4:6]}** **** {str_number_key_no_space[-4:]}"

        str_number_card = str(number_card)  # Преобразование числа в строку

        if not number_card:
            return '0'
        elif len(str_number_card) > 16:
            str_number_card_no_space = ''
            for letter in str_number_card:
                if letter != ' ':
                    str_number_card_no_space += letter
                else:
                    continue
            return f"{str_number_card_no_space[0:4]} {str_number_card_no_space[4:6]}** **** {str_number_card_no_space[-4:]}"
        else:
            # кодировка номера, которая заменяет среднюю часть
            return f"{str_number_card[0:4]} {str_number_card[4:6]}** **** {str_number_card[-4:]}"




def get_mask_account(number_card: Union[int, str]) -> str:
    """Функция на вход номер счета и возвращает последние четыре цифры"""

    str_number_card: str = str(number_card)  # Преобразование числа в строку

    if not number_card:
        return '0'
    else:
        # кодировка номера, которая выводит последние 4 цифры с кодировкой
        return f"**{str_number_card[-4:]}"



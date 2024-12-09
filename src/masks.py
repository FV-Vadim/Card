def get_mask_card_number(number_card: int) -> str:
    """Функция принимает на вход номер карты и шифрует его"""

    str_number_card = str(number_card)  # Преобразование числа в строку

    # кодировка номера, которая заменяет среднюю часть
    return f"{str_number_card[0:4]} {str_number_card[4:6]}** **** {str_number_card[-4:]}"


def get_mask_account(number_card: int) -> str:
    """Функция на вход номер счета и возвращает последние четыре цифры"""

    str_number_card = str(number_card)  # Преобразование числа в строку

    # кодировка номера, которая выводит последние 4 цифры с кодировкой
    return f"**{str_number_card[-4:]}"

from typing import Union


def get_mask_card_number(number_card: Union[int, str]) -> str:
    """Функция принимает на вход номер карты и шифрует его"""

    str_number_card = str(number_card)  # Преобразование числа в строку, исключение пробелов
    coder_number_card = ""
    if number_card is None or not number_card:  # Если в номер карты передается пустой список или ничего не передается
        coder_number_card = "0"
    elif 12 <= len(str(number_card)) <= 20:  # Если количество символов больше 12 и меньше 20 с учетом пробелов
        str_number_card_correct = ""
        verification_numbers = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"  # Проверочные числа
        for letter in str_number_card:  # Цикл проверки символа в строке
            if letter in verification_numbers:  # Если введенных данных это цифра
                str_number_card_correct += letter  # Добавляется символ в строку
            else:
                continue  # Пропускает остальные
        if len(str(str_number_card_correct)) == 16:  # Номер состоит из 16 цифр
            # Кодировка номера, которая заменяет среднюю часть
            coder_number_card = (
                f"{str_number_card_correct[0:4]} {str_number_card_correct[4:6]}** **** {str_number_card_correct[-4:]}"
            )

        elif len(str(str_number_card_correct)) == 12:  # Номер состоит из 12 цифр
            # Кодировка номера, которая заменяет среднюю часть
            coder_number_card = f"{str_number_card_correct[0:2]}** **** {str_number_card_correct[-4:]}"
    else:
        coder_number_card = "Введен некорректный номер карты"
    return coder_number_card


def get_mask_account(number_card: Union[int, str]) -> str:
    """Функция на вход номер счета и возвращает последние четыре цифры"""

    str_number_count = str(number_card)  # Преобразование числа в строку

    if number_card is None or not number_card:  # Если в номер карты передается пустой список или ничего не передается
        return "0"
    elif 16 <= len(str(number_card)) <= 24:  # Если количество символов больше 16 и меньше 24 символов с учетом пробела
        str_number_count_corrected = ""
        verification_numbers = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"  # Проверочные числа
        for letter in str_number_count:  # Цикл проверки символа в строке
            if letter in verification_numbers:  # Если введенных данных это цифра
                str_number_count_corrected += letter  # Добавляется символ в строку
            else:
                continue  # Пропускает остальные
        # Кодировка номера, которая выводит последние 4 цифры с кодировкой
        return f"**{str_number_count_corrected[-4:]}"
    else:
        return "Введен некорректный номер счета"

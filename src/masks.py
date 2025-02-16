import os
from typing import Union

from src import decorators
from src.logging import get_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../logs", "mask.log")
logger = get_logger("mask", file_path)


@decorators.log(filename="mylog.txt")  # Декорирование функции
def get_mask_card_number(number_card: Union[int, str]) -> str:
    """Функция принимает на вход номер карты и шифрует его"""

    logger.info(f"Выполняем кодировку номера карты: {number_card}")

    str_number_card = str(number_card)  # Преобразование числа в строку, исключение пробелов
    coder_number_card = ""
    if number_card is None or not number_card:  # Если в номер карты передается пустой список или ничего не передается
        coder_number_card = "0"
        logger.info("Введенный номер карты пустой, кодировка не производится...")
    elif 12 <= len(str(number_card)) <= 20:  # Если количество символов больше 12 и меньше 20 с учетом пробелов
        str_number_card_cor = ""
        verification_numbers = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"  # Проверочные числа

        logger.info("Проверка введенных данных на корректность, когда в строке больше 16 символов ...")
        for letter in str_number_card:  # Цикл проверки символа в строке
            if letter in verification_numbers:  # Если введенных данных это цифра
                str_number_card_cor += letter  # Добавляется символ в строку
            else:
                continue  # Пропускает остальные
        if len(str(str_number_card_cor)) == 16:  # Номер состоит из 16 цифр
            # Кодировка номера, которая заменяет среднюю часть
            coder_number_card = (
                f"{str_number_card_cor[0:4]} {str_number_card_cor[4:6]}** **** {str_number_card_cor[-4:]}"
            )

        elif len(str(str_number_card_cor)) == 12:  # Номер состоит из 12 цифр
            # Кодировка номера, которая заменяет среднюю часть
            coder_number_card = f"{str_number_card_cor[0:2]}** **** {str_number_card_cor[-4:]}"
    else:
        logger.info("Введен некорректный номер карты")
        return "Введен некорректный номер карты"

    logger.info(f"Кодировка номера карты завершена: {coder_number_card}")
    return coder_number_card


@decorators.log(filename="mylog.txt")  # Декорирование функции
def get_mask_account(number_card: Union[int, str]) -> str:
    """Функция на вход номер счета и возвращает последние четыре цифры"""

    logger.info(f"Выполняем кодировку номера счета: {number_card}")

    str_number_count = str(number_card)  # Преобразование числа в строку

    if number_card is None or not number_card:  # Если в номер карты передается пустой список или ничего не передается
        logger.info("Введенный номер счета пустой, кодировка не производится...")
        return "0"
    elif 16 <= len(str(number_card)) <= 24:  # Если количество символов больше 16 и меньше 24 символов с учетом пробела
        str_number_count_corrected = ""
        verification_numbers = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"  # Проверочные числа

        logger.info("Проверка введенных данных на корректность, когда в строке больше 16 символов ...")
        for letter in str_number_count:  # Цикл проверки символа в строке
            if letter in verification_numbers:  # Если введенных данных это цифра
                str_number_count_corrected += letter  # Добавляется символ в строку
            else:
                continue  # Пропускает остальные
        # Кодировка номера, которая выводит последние 4 цифры с кодировкой

        logger.info(f"Кодировка номера счета завершена: {str_number_count_corrected}")
        return f"**{str_number_count_corrected[-4:]}"
    else:
        logger.info("Введен некорректный номер счета")
        return "Введен некорректный номер счета"

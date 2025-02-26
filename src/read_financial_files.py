import os

import pandas as pd

from src.my_logging import get_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../logs", "read_financial_files.log")
logger = get_logger("read_financial_files", file_path)


def csv_reader(filepath: str = "") -> list:
    """Функция чтения CSV файла и возвращает список словарей с данными из файла."""

    try:
        logger.info(f"Чтение файла {filepath}")
        data = pd.read_csv(filepath, sep=";").to_dict("records")
        return data

    except FileNotFoundError:
        logger.error("Файл не найден")
        raise FileNotFoundError("Файл не найден")


def excel_reader(filepath: str = "") -> list:
    """Функция принимает на вход путь к файлу формата .xlsx и возвращает список словарей
    с данными из файла."""

    try:
        logger.info(f"Чтение файла {filepath}")
        data = pd.read_excel(filepath).to_dict("records")
        return data

    except FileNotFoundError:
        logger.error("Файл не найден")
        raise FileNotFoundError("Файл не найден")

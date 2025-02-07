import logging
import os
from logging import Logger


def get_logger(file_name: str, log_file: str) -> Logger:
    """Функция создает логгер и настраивает его для записи логов в указанный файл."""

    os.makedirs("logs", exist_ok=True)  # Проверка наличия папки для логирования
    logger = logging.getLogger(file_name)  # Создание логгера с указанным именем
    logger.setLevel(logging.DEBUG)  # Установка уровня логирования в DEBUG

    file_handler = logging.FileHandler(log_file, mode="w+")  # Создание обработчика логов в виде файла
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")  # Форматирование логов

    file_handler.setFormatter(file_formatter)  # Настройка обработчика логов
    logger.addHandler(file_handler)  # Добавление обработчика логов к логгеру

    return logger

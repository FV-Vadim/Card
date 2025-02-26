import os
from typing import List, Optional

from src.generators import filter_by_currency
from src.my_logging import get_logger
from src.processing import filter_by_state, sort_by_date
from src.read_financial_files import csv_reader, excel_reader
from src.search_operations import search_transactions_dict
from src.utils import get_json_transaction
from src.widget import get_date, mask_account_card

# Определяем корневую директорию и путь к файлу логов
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "./logs", "main.log")
logger = get_logger("main", file_path)


def user_input(user_input_value: str = "", parameters: Optional[List[str]] = None) -> Optional[str]:
    """
    Функция принимает на вход текстовое сообщение и список допустимых вариантов ответа.
    Производит ввод пользователем, пока введенное значение не соответствует одному из допустимых.

    :param user_input_value: Текстовое сообщение для пользователя
    :param parameters: Список допустимых вариантов ответа
    :return: Возвращает введенное пользователем значение
    """

    if parameters is None:
        parameters = []

    while user_input_value not in parameters:
        user_input_value = input("Пользователь: ").strip().upper()  # Приводим ввод к верхнему регистру
        logger.info(f"Получено введенное значение: {user_input_value}")

        if user_input_value in [param.upper() for param in parameters]:  # Приводим параметры к верхнему регистру
            logger.info(f"Данные введены верно: {user_input_value}")
            return user_input_value
        else:
            logger.info(f"Данные введены неверно: {user_input_value}")
            print("Программа: Данные введены неверно. Попробуйте еще раз.")
    return None


def main() -> list:
    """
    Главное меню приложения, которое запрашивает у пользователя необходимый пункт меню.
    После выбора пункта меню, запускается соответствующая функция.

    :return: Список транзакций и тип файла
    """
    file_type = ""

    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print(
        """
    Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла
    """
    )

    command = user_input("", ["1", "2", "3"])  # Список выбора команд пользователя

    if command == "1":
        print("Для обработки выбран JSON - файл")
        file_type = "json"  # Передача типа файла JSON
    elif command == "2":
        print("Для обработки выбран CSV - файл")  # Передача типа файла CSV
        file_type = "csv"
    elif command == "3":
        print("Для обработки выбран XLSX - файл")  # Передача типа файла XLSX
        file_type = "xlsx"

    state = ""
    while state not in ["EXECUTED", "CANCELED", "PENDING"]:  # Если значение state в списке, запускается цикл
        print(
            """Программа: Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )

        state = str(input("Пользователь: ")).upper()  # Ввод значения пользователем
        logger.info(f"Получено введенное значение статуса: {state}")

        if state in ["EXECUTED", "CANCELED", "PENDING"]:  # Если значение есть в списке
            logger.info(f"Введенный статус корректен: {state}")
        else:
            logger.info(f"Введенный статус некорректен: {state}")
            print(f"Программа: Статус операции {state} недоступен.")

    transactions = []
    try:
        if file_type == "json":
            transactions = get_json_transaction("data/operations.json")  # Открытие файла JSON
        elif file_type == "csv":
            transactions = csv_reader("data/transactions.csv")  # Открытие файла CSV
        elif file_type == "xlsx":
            transactions = excel_reader("data/transactions_excel.xlsx")  # Открытие файла EXCEL
    except FileNotFoundError:
        print("Программа: Файл с данными транзакций не найден. Проверьте правильность пути к файлу.")
        logger.error("Файл с данными транзакций не найден.")
    except Exception as e:
        print(f"Программа: Произошла ошибка при чтении файла: {str(e)}")
        logger.error(f"Ошибка при чтении файла: {str(e)}")

    logger.info(f"Фильтрация по статусу: {state}")
    try:
        transactions = filter_by_state(transactions, state)  # Фильтрация транзакций по статусу
        logger.info("Фильтрация завершена")
        print(f'Программа: Операции отфильтрованы по статусу: "{state}"')
    except Exception as e:
        logger.error(f"Ошибка при фильтрации: {str(e)}")

    print("Программа: Отсортировать операции по дате? Да/Нет")
    sorting_by_date = user_input("", ["да", "нет"])

    if sorting_by_date is not None and sorting_by_date.lower() == "да":
        logger.info("Сортировка по дате включена")
        print("Программа: Отсортировать по возрастанию или по убыванию?")

        sorting_parameters = user_input("", ["по возрастанию", "по убыванию"])
        logger.info("Сортировка по возрастанию / по убыванию")

        if sorting_parameters is not None:
            transactions = sort_by_date(list(transactions), sorting_parameters.lower() == "по убыванию")  # Сортировка
            logger.info("Сортировка завершена")
            print(
                "Программа: Операции отсортированы по дате "
                f'{"по убыванию" if sorting_parameters.lower() == "по убыванию" else "по возрастанию"}'
            )

    print("Программа: Выводить только рублевые транзакции? Да/Нет")
    currency_filter = user_input("", ["да", "нет"])  # Выбор нужна ли фильтрация

    if (
        currency_filter is not None and currency_filter.lower() == "да"
    ):  # Если пользователь выбрал 'да', то включается фильтрация
        logger.info("Фильтрация по валюте включена")
        filtered_transactions = filter_by_currency(transactions, "RUB")  # Получаем генератор
        filtered_list = list(filtered_transactions)  # Преобразуем генератор в список
        # print(filtered_list)  # Вывод отфильтрованных транзакций
        if not filtered_list:  # Проверка на пустой список
            print("Нет рублевых транзакций.")
            transactions_list = []  # Убедимся, что список пуст
        else:
            transactions_list = filtered_list  # Используем отфильтрованный список
    else:
        transactions_list = transactions

    print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    keyword_filter = user_input("", ["да", "нет"])  # Выбор фильтрации по слову

    if keyword_filter is not None and keyword_filter.lower() == "да":
        print("Программа: Введите слово для поиска.")
        keyword = input("Пользователь: ")
        logger.info("Фильтрация по ключевым словам включена")

        filtered_transactions_keyword = search_transactions_dict(transactions_list, keyword)  # Фильтрация по слову
        if filtered_transactions_keyword is None or len(list(filtered_transactions_keyword)) == 0:
            print("Нет транзакций с указанным ключевым словом.")
            transactions_list = []  # Убедимся, что список пуст
        else:
            transactions_list = filtered_transactions_keyword
        logger.info("Фильтрация завершена")

    return [transactions_list, file_type]


# Вывод функции
if __name__ == "__main__":
    program_data = main()  # Получаем данные из основной функции
    transactions_list_program = program_data[0]  # Итоговый список операций
    file_type_program = program_data[1]  # Тип файла в котором происходила работа

    if not transactions_list_program:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Программа: Всего банковских операций в выборке: {len(transactions_list_program)}")

    for transaction in transactions_list_program:
        date = transaction.get("date", "Дата неизвестна")
        description = transaction.get("description", "Описание отсутствует")
        print(f"{get_date(date)} {description}")

        if transaction.get("description") == "Открытие вклада":
            to_account = transaction.get("to", "")
            if to_account:
                print(f"{mask_account_card(to_account)}")
            else:
                print("Карта не указана")
        else:
            from_account = transaction.get("from", "")
            to_account = transaction.get("to", "")
            if from_account and to_account:
                print(f"{mask_account_card(from_account)} -> {mask_account_card(to_account)}")
            else:
                print("Номер карты не указан")

        if file_type_program == "json":
            amount = transaction.get("operationAmount", {}).get("amount", "Сумма неизвестна")
            currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", "Валюта неизвестна")
            print(f"{amount} {currency}")
        else:
            amount = transaction.get("amount", "Сумма неизвестна")
            currency_code = transaction.get("currency_code", "Валюта неизвестна")
            print(f"{amount} {currency_code}")

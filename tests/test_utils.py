import json
from unittest.mock import Mock, mock_open, patch

from src import decorators
from src.utils import get_json_transaction, get_transaction_amount


@decorators.log(filename="mylog.txt")
def test_get_json_transactions_file_err() -> None:
    """Функция теста выполняет проверку открытия файла,
    если файла нет, она проверяет срабатывание исключение"""

    assert get_json_transaction("") == []


@decorators.log(filename="mylog.txt")
@patch("builtins.open", mock_open(read_data=None))
def test_get_json_transactions_empty_file() -> None:
    """Функция теста выполняет проверку открытия файла,
    если файл пустой, она проверяет срабатывание исключение"""

    assert get_json_transaction() == []


@patch("builtins.open", new_callable=mock_open)
def test_valid_file(mock_file: Mock, valid_json_data: dict) -> None:

    mock_file.return_value.__enter__.return_value.read.return_value = json.dumps(valid_json_data)
    # Устанавливаем значение, которое будет возвращено при чтении файла

    result = get_json_transaction("operations.json")
    # Вызываем тестируемую функцию с именем файла "operations.json"

    assert result == valid_json_data
    # Сравниваем результат с ожидаемой структурой данных


# Данные для тестирования работы функции get_json_transactions и get_transactions_amount
data: str = """[{
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "RUB",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
    }]"""


@decorators.log(filename="mylog.txt")
# Тест функции get_json_transactions по типу выходного значения
@patch("builtins.open", mock_open(read_data=data))
def test_get_json_transactions_type() -> None:
    assert type(get_json_transaction()) is list


@decorators.log(filename="mylog.txt")
# Тест функции get_json_transactions на соответствие выходного значения
@patch("builtins.open", mock_open(read_data=data))
def test_get_json_transactions_result() -> None:
    assert get_json_transaction()[0]["operationAmount"]["amount"] == "8221.37"


# Тест функции get_transactions_amount на правильность работы в рублях
@patch("builtins.open", mock_open(read_data=data))
def test_get_transaction_amount_rub(transaction: dict) -> None:
    """Тест функции get_transaction_amount для транзакций в рублях."""

    transaction = get_json_transaction()[0]
    assert get_transaction_amount(transaction) == float(8221.37)


# Тест функции get_transactions_amount на конвертацию валют
@patch("requests.request")
def test_get_transaction_amount_usd(mock_currency: Mock, transaction: dict) -> None:
    mock_response = mock_currency.return_value
    mock_response.json.return_value = {"result": 10343.8}
    assert get_transaction_amount(transaction) == float(10343.8)


def test_get_operation_amount_exception_with_mock() -> None:
    # Имитируем ситуацию, когда возникает исключение
    operation = Mock()
    operation.side_effect = KeyError("Custom error")

    # Проверяем возвращаемое значение
    result = get_transaction_amount(operation)
    assert result is None

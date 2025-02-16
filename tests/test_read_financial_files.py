from unittest.mock import Mock, patch

import pandas
import pytest

from src.read_financial_files import csv_reader, excel_reader


@patch("pandas.read_csv")
def test_csv_reader(mock_get: Mock, csv_transaction: list[dict]) -> None:
    mock_get.return_value = pandas.DataFrame(csv_transaction)

    transaction = csv_reader("test.csv")

    assert transaction == csv_transaction

    mock_get.assert_called_once_with("test.csv", sep=";")


@patch("pandas.read_csv")
def test_csv_reader_none(mock_get: Mock) -> None:
    # Настраиваем мок-объект, чтобы он вызывал FileNotFoundError
    mock_get.side_effect = FileNotFoundError("Файл не найден")

    # Проверяем, что функция выбрасывает исключение FileNotFoundError
    with pytest.raises(FileNotFoundError) as exc_info:
        csv_reader("non_existent_file.csv")

    # Проверяем сообщение исключения
    assert str(exc_info.value) == "Файл не найден"


@patch("pandas.read_excel")
def test_excel_reader(mock_get: Mock, excel_transaction: list[dict]) -> None:
    mock_get.return_value = pandas.DataFrame(excel_transaction)

    transaction = excel_reader("test.xlsx")

    assert transaction == excel_transaction

    mock_get.assert_called_once_with("test.xlsx")


@patch("pandas.read_excel")
def test_excel_reader_none(mock_get: Mock) -> None:
    # Настраиваем мок-объект, чтобы он вызывал FileNotFoundError
    mock_get.side_effect = FileNotFoundError("Файл не найден")

    # Проверяем, что функция выбрасывает исключение FileNotFoundError
    with pytest.raises(FileNotFoundError) as exc_info:
        excel_reader("non_existent_file.xlsx")

    # Проверяем сообщение исключения
    assert str(exc_info.value) == "Файл не найден"

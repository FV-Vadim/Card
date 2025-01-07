from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency
from tests.conftest import result_one, result_two


def test_filter_by_currency_fixture(filter_by_currency_verification: list) -> None:
    assert next(filter_by_currency(filter_by_currency_verification, "USD")) == result_one
    assert next(filter_by_currency(filter_by_currency_verification, "RUB")) == result_two


def test_transaction_descriptions_fixture(transaction_descriptions_verification: Any) -> None:
    assert next(transaction_descriptions_verification) == "Перевод организации"
    assert next(transaction_descriptions_verification) == "Перевод со счета на счет"
    assert next(transaction_descriptions_verification) == "Перевод со счета на счет"
    assert next(transaction_descriptions_verification) == "Перевод с карты на карту"
    assert next(transaction_descriptions_verification) == "Перевод организации"


@pytest.mark.parametrize(
    "start_number, stop_number, expected_value",
    [
        (
            10,
            15,
            [
                "0000 0000 0000 0010",
                "0000 0000 0000 0011",
                "0000 0000 0000 0012",
                "0000 0000 0000 0013",
                "0000 0000 0000 0014",
            ],
        ),
        (21001, 21005, ["0000 0000 0002 1001", "0000 0000 0002 1002", "0000 0000 0002 1003", "0000 0000 0002 1004"]),
        (1, "5", ["Ошибка: некорректный ввод"]),
        ("r", 5, ["Ошибка: некорректный ввод"]),
        ([], [], ["Ошибка: некорректный ввод"]),
    ],
)
def test_card_number_generator(start_number: int, stop_number: int, expected_value: list[str]) -> None:
    assert list(card_number_generator(start_number, stop_number)) == expected_value

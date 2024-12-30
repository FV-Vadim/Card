from typing import Union

import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_fixture(verification_card_name: str, card_number_verification: str) -> None:
    assert mask_account_card(verification_card_name, card_number_verification) == "Maestro 1596 83** **** 5199"


@pytest.mark.parametrize(
    "name,number_card, check_hidden_card",
    [
        ("Счет", "64686473678894779589", "Счет **9589"),
        ("Visa Classic", 6831982476737658, "Visa Classic 6831 98** **** 7658"),
        ("MasterCard", "7158300734726758", "Mastercard 7158 30** **** 6758"),
        ("Visa Platinum", 8990922113665229, "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold", "5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет", "6468 6473 6788 9477 9589", "Счет **9589"),
        ("Maestro", "1596 8378 6870 5199", "Maestro 1596 83** **** 5199"),
        ("Maestro", "1596 8378 5199", "Maestro 15** **** 5199"),
        ("", "", "Введите тип и номер карты, счета."),
        (1596837868705199, "Maestro", "Введите сначала тип карты, а после номер"),
    ],
)
def test_mask_account_card(name: str, number_card: Union[int, str], check_hidden_card: str) -> None:
    assert mask_account_card(name, number_card) == check_hidden_card


def test_get_date_fixture(get_date_verification: str) -> None:
    assert get_date(get_date_verification)


@pytest.mark.parametrize(
    "date, check_date",
    [
        ("2023-03-11T02:26:18.671407", "11.03.2023"),
        ("", "Введите дату."),
        ([], "Введите дату."),
        ("2023-03-11", "11.03.2023"),
    ],
)
def test_get_date(date: str, check_date: str) -> None:
    assert get_date(date) == check_date

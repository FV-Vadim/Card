import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_fixture(card_number_verification: str) -> None:
    assert mask_account_card(card_number_verification) == "Maestro 1596 83** **** 5199"


@pytest.mark.parametrize(
    "name_number_card, check_hidden_card",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 646864736788947 9589", "Счет **9589"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ],
)
def test_mask_account_card(name_number_card: str, check_hidden_card: str) -> None:
    assert mask_account_card(name_number_card) == check_hidden_card


def test_get_date_fixture(get_date_verification: str) -> None:
    assert get_date(get_date_verification)


@pytest.mark.parametrize(
    "date, check_date",
    [
        ("2023-03-11T02:26:18.671407", "11.03.2023"),
        ("", ""),
        ("2023-03-11", "11.03.2023"),
    ],
)
def test_get_date(date: str, check_date: str) -> None:
    assert get_date(date) == check_date

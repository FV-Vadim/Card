from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_fixture(card_verification: str) -> None:
    for meaning_card in card_verification:
        if len(str(meaning_card)) > 16:
            assert get_mask_account(meaning_card) == "**4305"
        else:
            assert get_mask_card_number(meaning_card) == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "number_card, hidden_card",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        (7000792289606361, "7000 79** **** 6361"),
        ("7000 7922 8960 6361", "7000 79** **** 6361"),
        ("1234 5678 2200 8790", "1234 56** **** 8790"),
        ("1234 5678 8790", "12** **** 8790"),
        ("1232132121321312321312331", "Введен некорректный номер карты"),
        ("", "0"),
        ([], "0"),
        ({}, "0"),
    ],
)
def test_get_mask_card_number(number_card: Union[int, str], hidden_card: str) -> None:
    assert get_mask_card_number(number_card) == hidden_card


@pytest.mark.parametrize(
    "number_card, hidden_account",
    [
        ("73654108430135874305", "**4305"),
        (73654108430135874305, "**4305"),
        ("7365 4108 4301 3587 4305", "**4305"),
        ("1234 5678 2200 8790 0000", "**0000"),
        ("7365410843013574305", "**4305"),
        ("1232132121321312321312331", "Введен некорректный номер счета"),
        ("", "0"),
        ([], "0"),
        ({}, "0"),
    ],
)
def test_get_mask_account(number_card: Union[int, str], hidden_account: str) -> None:
    assert get_mask_account(number_card) == hidden_account

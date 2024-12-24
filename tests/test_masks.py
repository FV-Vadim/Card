import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number_fixture(card_verification):
    for meaning_card in card_verification:
        assert get_mask_card_number(meaning_card) == "7000 79** **** 6361"


def test_get_mask_account_number_fixture(count_verification):
    for meaning_count in count_verification:
        assert get_mask_account(meaning_count) == "**4305"


@pytest.mark.parametrize(
    "number_card, hidden_card",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        (7000792289606361, "7000 79** **** 6361"),
        ("7000 7922 8960 6361", "7000 79** **** 6361"),
        ("1234 5678 2200 8790", "1234 56** **** 8790"),
        ("", "0"),
        ([], "0"),
        ({}, "0"),
    ],
)
def test_get_mask_card_number(number_card, hidden_card):
    assert get_mask_card_number(number_card) == hidden_card


@pytest.mark.parametrize(
    "number_card, hidden_account",
    [
        ("73654108430135874305", "**4305"),
        (73654108430135874305, "**4305"),
        ("7365 4108 4301 3587 4305", "**4305"),
        ("1234 5678 2200 8790 0000", "**0000"),
        ("", "0"),
        ([], "0"),
        ({}, "0"),
    ],
)
def test_get_mask_account(number_card, hidden_account):
    assert get_mask_account(number_card) == hidden_account

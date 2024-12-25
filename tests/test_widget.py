import pytest

from src.widget import mask_account_card, get_date


@pytest.fixture()
def test_mask_account_card_fixture(card_name_verification):
    assert (
        mask_account_card(
            card_name_verification
        )
        == "Maestro 1596 83** **** 5199"
    )


@pytest.mark.parametrize(
    "name,number_card, check_hidden_card",
    [
        ("Счет", "64686473678894779589", "Счет **9589"),
        ("Visa Classic", 6831982476737658, "Visa Classic 6831 98** **** 7658"),
        ("MasterCard", "7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Platinum", 8990922113665229, "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold", "5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("", "", "Введите тип и номер карты, счета."),
        ("Счет", "6468 6473 6788 9477 9589", "Счет **9589"),
        ("Maestro", "1596 8378 6870 5199", "Maestro 1596 83** **** 5199"),
    ],
)
def test_mask_account_card(name, number_card, check_hidden_card):
    assert mask_account_card(name, number_card) == check_hidden_card


@pytest.fixture
def test_get_date_fixture(get_date_verification):
    assert get_date(get_date_verification)


@pytest.mark.parametrize(
    "date, check_date", [("2023-03-11T02:26:18.671407", "11.03.2023"), ("", "Введите дату."), ([], "Введите дату.")]
)
def test_get_date(date, check_date):
    assert get_date(date) == check_date

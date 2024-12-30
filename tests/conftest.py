import pytest

# Фикстура для test_masks.py


@pytest.fixture
def card_verification() -> list[str | int]:  # Возвращает номера карт, и счетов
    return ["7000792289606361", 7000792289606361, "73654108430135874305", 73654108430135874305]


# Фикстуры для test_widget.py


@pytest.fixture
def verification_card_name() -> str:  # Возвращает названия карты или счета
    return "Maestro"


@pytest.fixture
def card_number_verification() -> str:  # Возвращает номер карты или номер счета
    return "1596837868705199"


@pytest.fixture
def get_date_verification() -> str:  # Возвращает словарь со списками дат
    return "2024-03-11T02:26:18.671407"


# Фикстуры для test_processing.py


@pytest.fixture
def filter_by_state_verification() -> list:  # Возвращает словарь со списками
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

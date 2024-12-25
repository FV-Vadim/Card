import pytest


@pytest.fixture
def card_verification():
    return ["7000792289606361", 7000792289606361, "73654108430135874305", 73654108430135874305]


@pytest.fixture
def card_name_verification():
    return "Maestro" "1596837868705199"

@pytest.fixture
def get_date_verification():
    return ["2024-03-11T02:26:18.671407", "2024-07-11T02:26:18.671407", "2024-03-15T02:26:18.671407"]

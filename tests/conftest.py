import pytest


@pytest.fixture
def card_verification():
    return ['7000792289606361', 7000792289606361, '7000 7922 8960 6361']

@pytest.fixture
def count_verification():
    return ['73654108430135874305', 73654108430135874305, '7365 4108 4301 3587 4305']
from src.search_operations import search_transactions_dict, transaction_category_count


def test_search_by_keyword(filter_by_currency_verification: list) -> None:
    result = search_transactions_dict(filter_by_currency_verification, "Перевод организации")
    assert len(result) == 2
    assert {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    } in result
    assert {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    } in result


def test_empty_query(filter_by_currency_verification: list) -> None:
    result = search_transactions_dict(filter_by_currency_verification, "")
    assert len(result) == 5


def test_count_categories(filter_by_currency_verification: list) -> None:
    categories = ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]
    result = transaction_category_count(filter_by_currency_verification, categories)
    expected = {
        "Перевод организации": 1,
        "Перевод со счета на счет": 1,
        "Перевод с карты на карту": 0,
    }
    assert result == expected


def test_transaction_category_count_with_missing_description() -> None:
    # Тестовые данные: одна транзакция без ключа "description"
    transactions = [
        {"description": "Перевод организации", "amount": "1000"},
        {"amount": "500"},  # Отсутствует описание
        {"description": "Оплата услуг", "amount": "200"},
    ]

    # Категории для поиска
    categories = ["Перевод организации", "Оплата услуг"]

    # Вызов функции
    result = transaction_category_count(transactions, categories)

    # Ожидаемый результат: транзакция без описания пропущена
    expected = {
        "Перевод организации": 0,  # 1 - 1 (вычитание категории)
        "Оплата услуг": 0,  # 1 - 1 (вычитание категории)
    }

    # Проверка результата
    assert result == expected

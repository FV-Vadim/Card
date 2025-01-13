# Обработка информации банка, карт, счетов

## Описание
Разработка данного проекта проходит в рамках курса "Профессия Python-разработчик" от Skypro.

Данный проект обрабатывает информацию, полученную от клиента банка. 
Алгоритм обрабатывает информацию и засекречивает полученную информацию о картах и счетах.

## Цели ученика:
- Научиться программировать на Python
- Изучить основные инструменты Python-разработчика
- Освоить профессию разработчика на Python

## Цели проекта:

### Разработать функционал приложения, который:
- Принимает название и номер карты, или счет и номер счета.
- Маркирует номера карт или счетов.
- Выполняет отбор данных по состоянию (state) и сортирует данные по дате (date) выполнения.

# Установка и запуск проекта
## Для установки и запуска проекта у вас должны быть установлены IDE, Python 3 и GitHub

- Клонируйте репозиторий командой 'git clone https://github.com/FV-Vadim/Card.git'
- Запустите проект в своей IDE
- В корне проекта вам нужно найти модуль main.py
- Запустите файл main.py в вашей IDE
На данном этапе разработки не предусмотрен ввод команд. 
Все функции имеют заданные значения и запускаются автоматически.

Модуль alphabetical.py содержит словарь букв английского языка и кириллицы.

# Команды

## Pip
- `pip install package-name` - Установка пакета
- 'pip install package-name==4.8.2' - Установка пакета версии 4.8.2
- `python3.13.1 -m pip install package-name` - Установка пакета для Python v3.13.1
- `pip uninstall packege-name` - Удаление пакета
- `python -m pip install --upgrade pip` - Обновление pip
- `pip list` - Вывод списка установленных пакетов
- `pip freeze > requirements.txt` - Запись установленных библиотек в файл

## Poetry
- `poetry init` - Инициализировать пакет в существующем проекте
- `poetry shell` - Активировать виртуальное окружение
- `poetry add requests` - Установка библиотек, зависимостей. В пример указан requests.
- `poetry show --tree` - Посмотреть дерево зависимостей
- `poetry add --group dev requests` - Установка группы develop зависимостей. В пример указан requests.

## Poetry add group dev
- `poetry add --group dev mypy` - Установка Mypy
- `poetry add --group dev pytest` - Установка Pytest
- `poetry add --group dev pytest-cov` - Установка Pytest-cov
``poetry run pytest --cov`` - Запуск тестов с оценкой покрытия
``pytest --cov=src --cov-report=html`` - Генерация отчета по покрытию в HTML формате

## Poetry add group lint
- `poetry add --group lint black` - Установка Black
- `poetry add --group lint isort` - Установка Isort
- `poetry add --group lint flake8` - Установка Flake8

## Git

- `git init` - Создать репозиторий
- `git status` - Посмотреть статус репозитория
- `git add 'Название файла'` - Добавить индекс (выбрать файл для коммита)
- `git commit -m 'Краткое описание что, было сделано'` - Файлы из индекса отправить в репозиторий
- `git log` - Список всех выполненных коммитов, отсортированных по дате выполнения
- `git show 'commit_hash'` - Все изменения, сделанные в рамках одного коммита по хешу


# Описание функций
## Функция get_mask_card_number()
Функция принимает на вход номер карты и возвращает ее маску. 
Номер карты замаскирован и отображается в формате ```XXXX XX** **** XXXX``` где X — это цифра номера.
То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами.

### Пример работы функции:
    7000792289606361 - входной аргумент
    7000 79** **** 6361 - выход функции
## Функция get_mask_account()
Функция принимает на вход номер счета и возвращает его маску.
Номер счета замаскирован и отображается в формате ```**XXXX``` где X — это цифра номера.
То есть видны только последние 4 цифры номера, а перед ними — две звездочки.

### Пример работы функции:
    73654108430135874305 - входной аргумент
    **4305 - выход функции
## Функция mask_account_card()
Функция принимает на вход строку, содержащую тип данных (номер, название карты или номерБ название счета).
Возвращает замаскированный номер с названием карты или названием счета

### Пример для карты
    Visa Platinum 7000792289606361 - входной аргумент
    Visa Platinum 7000 79** **** 6361 - выход функции

### Пример для счета
    Счет 73654108430135874305 - входной аргумент
    Счет **4305 - выход функции
## Функция get_date()
Функция принимает на вход строку с датой в формате
```"2024-03-11T02:26:18.671407"```
и возвращает строку с датой в формате
```"ДД.ММ.ГГГГ" ("11.03.2024").```
## Функция filter_by_state()
Функция принимает список словарей и опционально значение для ключа ```state``` (по умолчанию ```'EXECUTED'```).
Функция возвращает новый список словарей, содержащий только те словари, у которых ключ ```state``` соответствует указанному значению.

### Пример работы функции:
    Входные данные
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

    Выход функции со статусом по умолчанию 'EXECUTED'
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    
    Выход функции, если вторым аргументов передано 'CANCELED'
    [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

## Функция sort_by_date
Функция принимает список словарей и сортирует списки по значению ```bool``` для ключа ```date``` (по умолчанию ```True```).
При значении ```True``` сортировка списка производится по убыванию.
### Входные данные
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    
    Выход функции со статусом по умолчанию 'True'
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

При значении ```False``` сортировка списка производится по убыванию.
### Входные данные
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

    Выход функции со статусом по умолчанию 'False'
    [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]

# Тестирование через pytest

## Parametrize

Использование Parametrize включает в себя параметры и значения, которое поступает в функцию и выходит из функции.
При помощи Parametrize мы можем проверить разом несколько вариантов входных данных.

### Без декоратора работать не будет

``@pytest.mark.parametrize`` - Конструкция декоратор

Пример:
```
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
```

Вызов функции:
```
def test_get_mask_card_number(number_card: Union[int, str], hidden_card: str) -> None:
    assert get_mask_card_number(number_card) == hidden_card
```

Результат:
```
test_masks.py::test_get_mask_card_number[7000792289606361-7000 79** **** 6361_0] PASSED [ 10%]
test_masks.py::test_get_mask_card_number[7000792289606361-7000 79** **** 6361_1] PASSED [ 15%]
test_masks.py::test_get_mask_card_number[7000 7922 8960 6361-7000 79** **** 6361] PASSED [ 21%]
test_masks.py::test_get_mask_card_number[1234 5678 2200 8790-1234 56** **** 8790] PASSED [ 26%]
test_masks.py::test_get_mask_card_number[1234 5678 8790-12** **** 8790] PASSED [ 31%]
test_masks.py::test_get_mask_card_number[1232132121321312321312331-\u0412\u0432\u0435\u0434\u0435\u043d \u043d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u043a\u0430\u0440\u0442\u044b] PASSED [ 36%]
test_masks.py::test_get_mask_card_number[-0] PASSED                      [ 42%]
test_masks.py::test_get_mask_card_number[number_card7-0] PASSED          [ 47%]
test_masks.py::test_get_mask_card_number[number_card8-0] PASSED          [ 52%]
test_masks.py::test_get_mask_account[73654108430135874305-**4305_0] PASSED [ 57%]
test_masks.py::test_get_mask_account[73654108430135874305-**4305_1] PASSED [ 63%]
test_masks.py::test_get_mask_account[7365 4108 4301 3587 4305-**4305] PASSED [ 68%]
test_masks.py::test_get_mask_account[1234 5678 2200 8790 0000-**0000] PASSED [ 73%]
test_masks.py::test_get_mask_account[7365410843013574305-**4305] PASSED  [ 78%]
test_masks.py::test_get_mask_account[1232132121321312321312331-\u0412\u0432\u0435\u0434\u0435\u043d \u043d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0441\u0447\u0435\u0442\u0430] PASSED [ 84%]
test_masks.py::test_get_mask_account[-0] PASSED                          [ 89%]
test_masks.py::test_get_mask_account[number_card7-0] PASSED              [ 94%]
test_masks.py::test_get_mask_account[number_card8-0] PASSED              [100%]

============================= 18 passed in 0.11s ==============================
```

## Fixture

Польза фикстур, когда происходит создание функций в разных модулях, выполняющих примерно один и тот же функционал. 
Можно вызвать одну фикстуру в тестовые модули и проверить несколько модулей функций.
В модуле conftests.py создаются фикстуры: ``@pytest.fixture`` - декоратор

### Без декоратора работать не будет
``@pytest.fixture`` - декоратор

Пример:
```
@pytest.fixture
def card_verification() -> list[str | int]:  # Возвращает номера карт, и счетов
    return ["7000792289606361", 7000792289606361, "73654108430135874305", 73654108430135874305]
```

Вызов функции:
```
def test_get_mask_card_number_fixture(card_verification: str) -> None:
    for meaning_card in card_verification:
        if len(str(meaning_card)) > 16:
            assert get_mask_account(meaning_card) == "**4305"
        else:
            assert get_mask_card_number(meaning_card) == "7000 79** **** 6361"
```

Результат:
```
============================= test session starts =============================
collecting ... collected 1 item

test_masks.py::test_get_mask_card_number_fixture PASSED                  [100%]

============================== 1 passed in 0.03s ==============================
```

В других модулях выполнены тесты подобным образом

## Пример работы функции, фильтрующий операции по заданной валюте:

### Входные данные:
```
[
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)
```

### Вывод функции при заданной валюте 'USD':

```
    {"id": 939719570,
      "state": "EXECUTED",
      "date": "2018-06-30T02:08:58.425572",
      "operationAmount": {
          "amount": "9824.07",
          "currency": {
              "name": "USD",
              "code": "USD"
          }
      },
      "description": "Перевод организации",
      "from": "Счет 75106830613657916952",
      "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
    }
```

### Вывод функции при заданной валюте 'RUB':

```
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
    }
```

## Пример работы функции, возвращающей описание операций:

### Входные данные из предыдущего примера

### Выходные данные:
```
Перевод организации
Перевод со счета на счет
Перевод со счета на счет
Перевод с карты на карту
Перевод организации
```

## Пример работы функции - генератора номеров карт:

### Входные данные(первый и последний номера карт, которые необходимо сгенерировать, - 10, 14)

### Выход функции:

```
0000 0000 0000 0010
0000 0000 0000 0011
0000 0000 0000 0012
0000 0000 0000 0013
0000 0000 0000 0014
```

## Используемые декораторы

### @log
Декоратор используется для записи результатов работы функций и отчетов об ошибках их выполнения.
При успешном выполнении функции записывается сообщение:
    
    function_name ok

### Пример логирования без исключений
``` 
get_mask_card_number ok
get_mask_account ok
get_mask_card_number ok
get_mask_account ok
get_mask_card_number ok
get_mask_account ok
get_mask_card_number ok
get_mask_card_number ok
get_mask_card_number ok
get_mask_account ok
filter_by_state ok
sort_by_date ok
```

При получении ошибки выполнения функции записывается сообщение:

    {function_name} error: {error message}, inputs: {function input parameters}

Декоратор принимает на вход необязательный параметр 'filename', который задает имя файла с логами.
При отсутствии 'filename' логи выводятся в консоль.

### Пример логирования в тестах

```
func error: division by zero. Inputs: (1, 0), {}  # Вызванное исключение
func ok  # Успешное логирование
func error: division by zero. Inputs: (1, 0), {}
func ok
```
import pytest
from _pytest.capture import CaptureFixture

from src import decorators


# тест ошибки выполнения функции и записи лога в файл
def test_log_decorator_function_error() -> None:
    @decorators.log(filename="mylog.txt")  # Вызов декоратора
    def func(a: int, b: int) -> float:
        """Простая функция для проверки деления где в знаменателе получается ноль"""

        return a / (a * b)

    with pytest.raises(Exception):  # Проверка на срабатывание исключения
        func(1, 0)
    file = open("mylog.txt", "r")  # Открывание файла mylog.txt для чтения
    line = file.readlines()  # Построчное чтение файла
    file.close()  # Закрытие файла

    # Добавление текста ошибки если исключение сработало в mylog.txt
    assert line[-1] == f"func error: division by zero, inputs: (1, 1), {"{}"}\n"


# тест успешного выполнения функции и записи лога в файл
def test_log_decorator_file_effectively() -> None:
    @decorators.log(filename="mylog.txt")
    def func(a: int, b: int) -> float:
        """Простая функция для проверки деления"""

        return 1 / (a ^ b)

    func(2, 0)
    file = open("mylog.txt", "r")  # Открывание файла mylog.txt для чтения
    line = file.readlines()  # Построчное чтение файла
    file.close()  # Закрытие файла

    # Добавление текста успешного выполнения в mylog.txt
    assert line[-1] == "func ok\n"


# тест ошибки выполнения функции и вывода лога в консоль
def test_log_decorator_console_error(capsys: CaptureFixture[str]) -> None:
    @decorators.log()
    def func(a: int, b: int) -> float:
        """Простая функция для проверки деления где в знаменателе получается ноль"""

        return 1 / (a - b * a)

    with pytest.raises(Exception):
        func(1, 1)
    captured = capsys.readouterr()  # Возвращение кортежа

    # Вывод текста ошибки в консоль
    assert captured.out == f"func error: division by zero, inputs: (1, 1), {"{}"}\n\n"


# тест успешного выполнения функции и вывода лога в консоль
def test_log_decorator_console_effectively(capsys: CaptureFixture[str]) -> None:
    @decorators.log()
    def func(a: int, b: int) -> float:
        """Простая функция для проверки деления"""

        return 1 / (a ^ b)

    func(2, 0)
    captured = capsys.readouterr()  # Возвращение кортежа

    # Вывод текста успешного выполнения в консоль
    assert captured.out == "func ok\n\n"

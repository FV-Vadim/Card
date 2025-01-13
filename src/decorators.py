from collections.abc import Callable


def log(filename: str = "") -> object:
    """Декоратор определяет, куда будут записываться логи (в файл или в консоль)"""

    def my_decorator(func: Callable) -> object:
        def wrapper(*args: str, **kwargs: int) -> object:
            try:
                # Выполнение декорирования функции
                result = func(*args, **kwargs)
            except Exception as error_mistake:
                # Обработка исключений декорируемой функции при ошибочном выполнении внутренней функции
                try:
                    # Открытие файла для записи лога
                    file = open(filename, "a")
                except FileNotFoundError:
                    # Обработка исключений если файл не найден, в этом случае лог выводится в терминал
                    print(f"{func.__name__} error: {error_mistake}. Inputs: {args}, {kwargs}\n")
                else:
                    # Если исключение сработало, лог записывается в файл сбора логирования
                    file.write(f"{func.__name__} error: {error_mistake}. Inputs: {args}, {kwargs}\n")
                    # Закрытие файла
                    file.close()
                # Исключение выбрасываемое при ошибке выполнения декорируемой функции
                raise Exception(f"Function error: {error_mistake}")
            else:
                # Направление ветки при успешном декорировании функции
                try:
                    # Открытие файла для записи лога
                    file = open(filename, "a")
                except FileNotFoundError:
                    # Обработка исключений если файл не найден, в этом случае лог выводится в терминал
                    print(f"{func.__name__} ok\n")
                else:
                    # Если исключение не сработало, лог записывается в файл сбора логирования
                    file.write(f"{func.__name__} ok\n")
                    # Закрытие файла
                    file.close()
                return result  # Вывод успешного результата в лог

        return wrapper  # Возвращение значения функции wrapper

    return my_decorator  # Возвращение значения функции my_decorator

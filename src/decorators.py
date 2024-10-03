import datetime
from functools import wraps


def log(filename: str = ""):
    """Декторар позволяющий логировать начало и конец выполнения функции, а также ее результаты или возникшие ошибки"""

    def write_file(write_filename: str):
        file = open(write_filename, "a")

        def write_inner(string: str):
            file.write(string + "\n")

        yield write_inner

        yield file.close()

    write_func = print
    gen_write_file = write_file(filename)
    if filename != "":
        write_func = next(gen_write_file)

    def log_inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            write_func(
                f"""{datetime.datetime.now().time()}, Вызов функции {func.__name__} - {func.__doc__}, переданные параметры {args}, {kwargs}"""
            )
            try:
                result = func(*args, **kwargs)
                write_func(f"{datetime.datetime.now().time()}, Функция вернула {result}")
                return result
            except Exception as err:
                write_func(f"{datetime.datetime.now().time()}, Ошибка выполнения функции: {err}")
            finally:
                write_func(f"{datetime.datetime.now().time()}, Завершение функции: {func.__name__}")
                next(gen_write_file)
        return wrapper

    return log_inner

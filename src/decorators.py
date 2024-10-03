import datetime
from functools import wraps


def log(filename: str = ""):
    """Декторар позволяющий логировать выполнения функции, ее завершение или возникшие ошибки"""

    def get_file_writer(write_filename: str):
        file = open(write_filename, "a", encoding="utf-8")

        def write_to_file(text):
            file.write(text + "\n")

        return write_to_file

    write_func = print
    if filename != "":
        write_func = get_file_writer(filename)

    def log_inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                write_func(f"{func.__name__} ok")
                return result
            except Exception as err:
                write_func(f"{func.__name__} error: {err}. Inputs: {args}, {kwargs}")
                raise err

        return wrapper

    return log_inner

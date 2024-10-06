import pytest

from src.decorators import log


def test_log_correct(capsys):
    @log()
    def division(x, y: int):
        """Деление"""
        return x / y

    division(2, 1)
    captured = capsys.readouterr()
    assert captured.out == "division ok\n"


def test_log_correct_in_file():
    @log("mylog.txt")
    def division(x, y: int):
        """Деление"""
        return x / y

    assert division(2, 1) == 2


def test_log_incorrect(capsys):
    @log()
    def division(x, y: int):
        """Деление"""
        return x / y

    with pytest.raises(ZeroDivisionError):
        division(2, 0)

    captured = capsys.readouterr()
    assert captured.out == "division error: division by zero. Inputs: (2, 0), {}\n"


def test_log_incorrect_in_file():
    @log("mylog.txt")
    def division(x, y: int):
        """Деление"""
        return x / y

    with pytest.raises(ZeroDivisionError):
        division(2, 0)

from src.decorators import log


def test_log_correct():
    @log()
    def division(x, y: int):
        """Деление"""
        return x / y

    assert division(2, 1) == 2


def test_log_correct_in_file():
    @log("test_log_correct_in_file.txt")
    def division(x, y: int):
        """Деление"""
        return x / y

    assert division(2, 1) == 2

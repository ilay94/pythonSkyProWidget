import pytest

from src.generators import filter_by_currency


def test_filter_by_currency_correct_filter(correct_list_transactions, correct_list_transactions_executed):
    result = list(filter_by_currency(correct_list_transactions, "USD"))
    assert result == correct_list_transactions_executed


@pytest.mark.parametrize(
    "currency, expected",
    [("START", []), ("", []), ([], []), (None, [])],
)
def test_filter_by_currency_different_currency(correct_list_transactions, currency, expected):
    result = list(filter_by_currency(correct_list_transactions, currency))
    assert result == expected


@pytest.mark.parametrize(
    "list_transactions, expected",
    [("", []), ([], []), (None, [])],
)
def test_filter_by_currency_empy_transaction(list_transactions, expected):
    result = list(filter_by_currency(list_transactions, "USD"))
    assert result == expected

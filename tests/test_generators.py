import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


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


def test_filter_by_currency_without_currency(
    list_transactions_without_description_and_currency, list_transactions_executed_without_currency
):
    result = list(filter_by_currency(list_transactions_without_description_and_currency, "USD"))
    assert result == list_transactions_executed_without_currency


def test_transaction_descriptions_correct(correct_list_transactions, correct_description):
    result = list(transaction_descriptions(correct_list_transactions))
    assert result == correct_description


@pytest.mark.parametrize(
    "list_transactions, expected",
    [("", []), ([], []), (None, [])],
)
def test_transaction_descriptions_empy_transaction(list_transactions, expected):
    result = list(transaction_descriptions(list_transactions))
    assert result == expected


def test_transaction_descriptions_without_currency(
    list_transactions_without_description_and_currency, description_without_description
):
    result = list(transaction_descriptions(list_transactions_without_description_and_currency))
    assert result == description_without_description


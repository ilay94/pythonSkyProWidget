import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


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


def test_card_number_generator():
    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"


def test_card_number_generator_secont_parth():
    generator = card_number_generator(121111, 121113)
    assert next(generator) == "0000 0000 0012 1111"
    assert next(generator) == "0000 0000 0012 1112"
    assert next(generator) == "0000 0000 0012 1113"


def test_card_number_generator_third_parth():
    generator = card_number_generator(1211211111, 1211211113)
    assert next(generator) == "0000 0012 1121 1111"
    assert next(generator) == "0000 0012 1121 1112"
    assert next(generator) == "0000 0012 1121 1113"


def test_card_number_generator_full_number():
    generator = card_number_generator(1121111211111111, 1121111211111113)
    assert next(generator) == "1121 1112 1111 1111"
    assert next(generator) == "1121 1112 1111 1112"
    assert next(generator) == "1121 1112 1111 1113"


@pytest.mark.parametrize(
    "start, finish, expected",
    [(2, 1, []), (1, 1, ["0000 0000 0000 0001"]), (1, None, ["0000 0000 0000 0001"]), (None, 1, [])],
)
def test_card_number_generator_start_finish_empty_test(start, finish, expected):
    generator = list(card_number_generator(start, finish))
    assert generator == expected

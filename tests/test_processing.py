import pytest

from src.processing import filter_by_state, sort_by_date, filter_by_currency, get_count_process_by_descriptions


def test_filter_by_state_correct_executed(correct_list_process, correct_list_process_state_executed):
    assert filter_by_state(correct_list_process) == correct_list_process_state_executed


def test_filter_by_state_correct_canceled(correct_list_process, correct_list_process_state_canceled):
    assert filter_by_state(correct_list_process, "CANCELED") == correct_list_process_state_canceled


def test_filter_by_state_list_without_state(list_process_without_state):
    assert filter_by_state(list_process_without_state) == []


def test_filter_by_state_list_without_state_canceled(list_process_without_state):
    assert filter_by_state(list_process_without_state, "CANCELED") == []


@pytest.mark.parametrize(
    "state, expected",
    [("START", []), ("", []), ([], []), (None, [])],
)
def test_filter_by_state_different_state(correct_list_process, state, expected):
    assert filter_by_state(correct_list_process, state) == expected


def test_sort_by_date_correct(correct_list_process, sorted_reverse_list_process):
    assert sort_by_date(correct_list_process) == sorted_reverse_list_process


def test_sort_by_date_correct_not_reverse(correct_list_process, sorted_list_process):
    assert sort_by_date(correct_list_process, False) == sorted_list_process


def test_sort_by_date_incorrect_date(incorrect_date_list_process):
    assert sort_by_date(incorrect_date_list_process) == []


def test_sort_by_date_without_date(list_process_without_date):
    assert sort_by_date(list_process_without_date) == []


def test_sort_by_date_equal_date(list_process_equal_date, sorted_list_process_equal_date):
    assert sort_by_date(list_process_equal_date) == sorted_list_process_equal_date


def test_filter_by_currency_correct(correct_list_transactions, correct_list_process_rub):
    assert filter_by_currency(correct_list_transactions) == correct_list_process_rub


@pytest.mark.parametrize(
    "currency, expected",
    [("START", []), ("", []), ([], []), (None, [])],
)
def test_filter_by_currency_different_currency(correct_list_transactions, currency, expected):
    assert filter_by_currency(correct_list_transactions, currency) == expected


def test_get_count_process_by_descriptions_correct(correct_list_transactions, correct_list_transactions_count):
    assert get_count_process_by_descriptions(correct_list_transactions) == correct_list_transactions_count


@pytest.mark.parametrize(
    "descriptions, expected",
    [
        (["Перевод организации"], {"Перевод организации": 2}),
        (["бубугага"], {}),
        ([], {"Перевод организации": 2, "Перевод с карты на карту": 1, "Перевод со счета на счет": 2}),
        (None, {"Перевод организации": 2, "Перевод с карты на карту": 1, "Перевод со счета на счет": 2}),
    ],
)
def test_get_count_process_by_descriptions_different_descriptions(correct_list_transactions, descriptions, expected):
    assert get_count_process_by_descriptions(correct_list_transactions, descriptions) == expected

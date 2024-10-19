import pytest
from unittest.mock import patch

from src.utils import read_json_from_file, get_amount_rub


def test_read_json_from_file_correct(first_correct_list_operations):
    result = read_json_from_file("tests/data/operations_correct.json")
    assert result[0] == first_correct_list_operations


@pytest.mark.parametrize(
    "file_patch, result",
    [
        ("tests/data/operations_incorrect_not_list.json", []),
        ("adasdad", []),
        ([], []),
        (None, []),
    ],
)
def test_read_json_from_file_incorrect_file(file_patch, result):
    assert read_json_from_file(file_patch) == result


def test_get_amount_rub_correct_from_rub(first_correct_list_operations):
    assert get_amount_rub(first_correct_list_operations) == 31957.58


@patch("requests.get")
def test_get_amount_rub_correct_from_usd(
    mock_convert_to_RUB, operation_correct, api_key
):
    mock_convert_to_RUB.return_value.status_code = 200
    mock_convert_to_RUB.return_value.text = '{"result": 1000.0}'
    assert get_amount_rub(operation_correct) == 1000.00
    mock_convert_to_RUB.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=10",
        headers={"apikey": api_key},
        data={},
    )

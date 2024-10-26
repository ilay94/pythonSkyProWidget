import os
from unittest.mock import patch

import pandas as pd
import pytest

from src.read_file import get_process_from_csv, get_process_from_excel


def test_get_process_from_csv_correct(correct_list_single_operations):
    result = get_process_from_csv(os.path.join(os.path.dirname(__file__), "data/transactions_correct.csv"))
    assert result[0] == correct_list_single_operations


def test_get_process_from_excel(correct_list_single_operations):
    result = get_process_from_excel(os.path.join(os.path.dirname(__file__), "data/transactions_excel_correct.xlsx"))
    assert result[0] == correct_list_single_operations


@pytest.mark.parametrize(
    "frame, result",
    [
        (
            {
                "id": [650703],
                "state": ["EXECUTED"],
                "date": ["2023-09-05T11:30:32Z"],
                "amount": [16210.1],
                "currency_name": ["Sol"],
                "currency_code": [None],
                "from": ["Счет 58803664561298323391"],
                "to": [None],
                "description": ["Перевод организации"],
            },
            [
                {
                    "date": "2023-09-05T11:30:32Z",
                    "description": "Перевод организации",
                    "from": "Счет 58803664561298323391",
                    "id": 650703,
                    "operationAmount": {"amount": 16210.1, "currency": {"code": None, "name": "Sol"}},
                    "state": "EXECUTED",
                    "to": None,
                }
            ],
        ),
        (
            {
                "id": [650703],
                "state": ["EXECUTED"],
                "date": ["2023-09-05T11:30:32Z"],
                "amount": ["asdadsa"],
                "currency_name": ["Sol"],
                "to": ["Счет 39745660563456619397"],
                "description": ["Перевод организации"],
            },
            [],
        ),
        (
            {
                "id": [650703],
                "state": ["EXECUTED"],
                "date": ["2023-09-05T11:30:32Z"],
                "currency_name": ["Sol"],
                "currency_code": ["PEN"],
                "from": ["Счет 58803664561298323391"],
                "description": ["Перевод организации"],
            },
            [],
        ),
    ],
)
@patch("pandas.read_csv")
def test_get_process_from_csv_incorrect(mock_read_incorrect, frame, result):
    mock_read_incorrect.return_value = pd.DataFrame(frame)
    process = get_process_from_csv(os.path.join(os.path.dirname(__file__), "data/transactions_correct.csv"))
    assert process == result
    mock_read_incorrect.assert_called_once_with(
        os.path.join(os.path.dirname(__file__), "data/transactions_correct.csv"), sep=";", header=0
    )


@pytest.mark.parametrize(
    "file_patch, result",
    [
        ("adasdad", []),
        ([], []),
        (None, []),
    ],
)
def test_get_process_from_csv_incorrect_file_patch(file_patch, result):
    assert get_process_from_csv(file_patch) == result


@pytest.mark.parametrize(
    "frame, result",
    [
        (
            {
                "id": [650703],
                "state": ["EXECUTED"],
                "date": ["2023-09-05T11:30:32Z"],
                "amount": [16210.1],
                "currency_name": ["Sol"],
                "currency_code": [None],
                "from": ["Счет 58803664561298323391"],
                "to": [None],
                "description": ["Перевод организации"],
            },
            [
                {
                    "date": "2023-09-05T11:30:32Z",
                    "description": "Перевод организации",
                    "from": "Счет 58803664561298323391",
                    "id": 650703,
                    "operationAmount": {"amount": 16210.1, "currency": {"code": None, "name": "Sol"}},
                    "state": "EXECUTED",
                    "to": None,
                }
            ],
        ),
        (
            {
                "id": [650703],
                "state": ["EXECUTED"],
                "date": ["2023-09-05T11:30:32Z"],
                "amount": ["asdadsa"],
                "currency_name": ["Sol"],
                "to": ["Счет 39745660563456619397"],
                "description": ["Перевод организации"],
            },
            [],
        ),
        (
            {
                "id": [650703],
                "state": ["EXECUTED"],
                "date": ["2023-09-05T11:30:32Z"],
                "currency_name": ["Sol"],
                "currency_code": ["PEN"],
                "from": ["Счет 58803664561298323391"],
                "description": ["Перевод организации"],
            },
            [],
        ),
    ],
)
@patch("pandas.read_excel")
def test_get_get_process_from_excel_incorrect(mock_read_incorrect, frame, result):
    mock_read_incorrect.return_value = pd.DataFrame(frame)
    process = get_process_from_excel(os.path.join(os.path.dirname(__file__), "data/transactions_excel_correct.csv"))
    assert process == result
    mock_read_incorrect.assert_called_once_with(
        os.path.join(os.path.dirname(__file__), "data/transactions_excel_correct.csv"), header=0
    )


@pytest.mark.parametrize(
    "file_patch, result",
    [
        ("adasdad", []),
        ([], []),
        (None, []),
    ],
)
def test_get_process_from_excel_incorrect_file_patch(file_patch, result):
    assert get_process_from_excel(file_patch) == result

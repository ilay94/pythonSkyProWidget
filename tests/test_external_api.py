import pytest
from unittest.mock import patch

from src.external_api import convert_to_RUB


@patch("requests.get")
def test_convert_to_RUB_correct(mock_convert_to_RUB, api_key):
    mock_convert_to_RUB.return_value.status_code = 200
    mock_convert_to_RUB.return_value.text = '{"result": 1000.0}'
    assert convert_to_RUB("10", "USD") == 1000.00
    mock_convert_to_RUB.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=10",
        headers={"apikey": api_key},
        data={},
    )


@pytest.mark.parametrize(
    "amount, code, result",
    [
        ("asdf", "USD", None),
        ([], "USD", None),
        ("None", "USD", None),
        ("100", "usd", None),
        ("100", "HELLO", None),
        ("100", "", None),
        ("100", [], None),
        ("100", None, None),
    ],
)
@patch("requests.get")
def test_convert_to_RUB_incorrect_param(
    mock_convert_to_RUB, amount, code, result, api_key
):
    mock_convert_to_RUB.return_value.status_code = 200
    mock_convert_to_RUB.return_value.text = '{"result": 1000.0}'
    assert convert_to_RUB(amount, code) == result


@pytest.mark.parametrize(
    "status_code",
    [100, 300, 400, 500],
)
@patch("requests.get")
def test_convert_to_RUB_incorrect_status_code(
    mock_convert_to_RUB, status_code, api_key, capsys
):
    mock_convert_to_RUB.return_value.status_code = status_code
    mock_convert_to_RUB.return_value.reason = status_code

    convert_to_RUB("10", "USD")
    captured = capsys.readouterr()
    assert captured.out == f"Запрос не был успешным. Возможная причина: {status_code}\n"
    mock_convert_to_RUB.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=10",
        headers={"apikey": api_key},
        data={},
    )

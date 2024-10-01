import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_account_card_masking(account_card, expected):
    # Проверка маскировки номеров карт и счетов
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize(
    "account_card, expected",
    [
        (" 1596837868705199", "Некорректный номер"),
        (" 64686473678894779589", "Некорректный номер"),
        ("MasterCard 71583007347267", "Некорректный номер карты"),
        ("Счет 353830334744478955", "Некорректный номер счета"),
        ("Visa Classic", "Некорректный номер карты"),
        ("8990922113665229", "Некорректный номер"),
        ("Visa Gold", "Некорректный номер карты"),
        ("Счет", "Некорректный номер счета"),
        ("", "Некорректный номер"),
        ([], "Некорректный номер"),
        (None, "Некорректный номер"),
    ],
)
def test_mask_account_card_account_card_incorrect(account_card, expected):
    # Проверка корректности номеров карт и счетов
    assert mask_account_card(account_card) == expected


def test_get_date(date_and_time):
    # Проверка получения даты из времени
    assert get_date(date_and_time) == "11.03.2024"


@pytest.mark.parametrize(
    "date_and_time, expected",
    [
        ("2024-13-11T02:26:18.671407", "Некорректная дата"),
        ("2024-12-32T02:26:18.671407", "Некорректная дата"),
        ("2024-02-32T02:26:18.671407", "Некорректная дата"),
        ("2023-02-29T02:26:18.671407", "Некорректная дата"),
        ("2024-LZ-15T02:26:18.671407", "Некорректная дата"),
        ("2024-13-11T02:26:1", "Некорректная дата"),
        ("2024-13-11T02:26:11118.671407", "Некорректная дата"),
        ("11-12-2024T02:26:18.671407", "Некорректная дата"),
        ("11-lZ-2024T02:26:18.671407", "Некорректная дата"),
        ("", "Некорректная дата"),
        ([], "Некорректная дата"),
        (None, "Некорректная дата"),
    ],
)
def test_get_date_date_incorrect(date_and_time, expected):
    # Проверка корректности даты и времени
    assert get_date(date_and_time) == expected

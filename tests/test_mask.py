import pytest

from src.mask import get_mask_account, get_mask_card_number


def test_get_mask_card_number_card_number_mask(unmask_card_number):
    # Проверяем маскировку номера карты
    assert get_mask_card_number(unmask_card_number) == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "number_card, expected",
    [
        ("700079228960", "Некорректный номер карты"),
        ("70007922896063617922", "Некорректный номер карты"),
        ("7000792FA9606361", "Некорректный номер карты"),
        ("asdvdfsbsdfgdkghuregn", "Некорректный номер карты"),
        (7000792289606361, "Некорректный номер карты"),
        ("", "Некорректный номер карты"),
        ([], "Некорректный номер карты"),
        (None, "Некорректный номер карты"),
    ],
)
def test_get_mask_card_number_card_number_incorrect(number_card, expected):
    # Проверка случаев некорректных номеров карты
    assert get_mask_card_number(number_card) == expected


def test_get_mask_account_account_mask(unmask_account):
    # Проверка маскировки номера счета
    assert get_mask_account(unmask_account) == "**4305"


@pytest.mark.parametrize(
    "number_card, expected",
    [
        ("7365410843013587", "Некорректный номер счета"),
        ("736541084301358743054305", "Некорректный номер счета"),
        ("7365{EQA430135874305", "Некорректный номер счета"),
        ("asdvdfsbsdfgdkghuregn", "Некорректный номер счета"),
        (73654108430135874305, "Некорректный номер счета"),
        ("", "Некорректный номер счета"),
        ([], "Некорректный номер счета"),
        (None, "Некорректный номер счета"),
    ],
)
def test_get_mask_card_number_card_number_incorrect(number_card, expected):
    # Проверка случаев некорректных номеров счетов
    assert get_mask_account(number_card) == expected

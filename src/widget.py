from src.mask import get_mask_account, get_mask_card_number
from datetime import datetime


def mask_account_card(account_card: str) -> str:
    """ "Функция маскировки номера карты или счета"""
    if type(account_card) is not str:
        return "Некорректный номер"
    account_card_split = account_card.rsplit(" ", 1)
    if account_card_split[0] == "" or account_card.isdigit():
        return "Некорректный номер"
    if account_card_split[0] != "Счет":
        mask_card = get_mask_card_number(account_card_split[-1])
        if mask_card == "Некорректный номер карты":
            return mask_card
        else:
            return f"{account_card_split[0]} {mask_card}"
    else:
        mask_account = get_mask_account(account_card_split[-1])
        if mask_account == "Некорректный номер счета":
            return mask_account
        else:
            return f"{account_card_split[0]} {mask_account}"


def get_date(date_time: str) -> str:
    """ "Функция форматирования даты к ДД.ММ.ГГГГ"""
    if type(date_time) is not str:
        return "Некорректная дата"
    try:
        if date_time.endswith("Z"):
            date_object = datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S")
        else:
            date_object = datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S.%f")
        formatted_date = date_object.strftime("%d.%m.%Y")
    except:
        return "Некорректная дата"

    return formatted_date

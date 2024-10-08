from src.mask import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """ "Функци маскировки номера карты или счета"""
    account_card_split = account_card.rsplit(" ", 1)
    if account_card_split[0] in ["Visa Platinum", "Maestro"]:
        mask_card = get_mask_card_number(account_card_split[1])
        return f"{account_card_split[0]} {mask_card}"
    elif account_card_split[0] == "Счет":
        mask_account = get_mask_account(account_card_split[1])
        return f"{account_card_split[0]} {mask_account}"


def get_date(date_time: str) -> str:
    """ "Функция форматирования даты к ДД.ММ.ГГГГ"""
    date = date_time[:10].split("-")
    return f"{date[2]}.{date[1]}.{date[0]}"

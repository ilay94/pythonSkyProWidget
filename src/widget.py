from src.mask import get_mask_account, get_mask_card_number


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
    if type(date_time) is not str or len(date_time) not in [19, 26]:
        return "Некорректная дата"
    date = date_time[:10].split("-")
    if not (len(date[2]) == 2 and len(date[1]) == 2 and len(date[0]) == 4 and "".join(date).isdigit()):
        return "Некорректная дата"
    count_date_in_mount = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    int_year = int(date[0])
    int_month = int(date[1])
    int_day = int(date[2])
    leap_year_mount_2 = 0
    if int_year % 4 == 0 and int_month == 2:
        leap_year_mount_2 = 1
    if not (1 <= int_month <= 12 and 1 <= int_day <= (count_date_in_mount[int_month - 1] + leap_year_mount_2)):
        return "Некорректная дата"
    return f"{date[2]}.{date[1]}.{date[0]}"

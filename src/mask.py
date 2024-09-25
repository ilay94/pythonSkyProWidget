def get_mask_card_number(card_number: str) -> str:
    """ "Функцию маскировки номера банковской карты в виде XXXX XX** **** XXXX"""
    if type(card_number) is str and card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return "Некорректный номер карты"


def get_mask_account(card_number: str) -> str:
    """ "Функцию маскировки номера банковского счета в виде **XXXX"""
    if type(card_number) is str and card_number.isdigit() and len(card_number) == 20:
        return f"**{card_number[-4:]}"
    else:
        return "Некорректный номер счета"

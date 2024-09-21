def get_mask_card_number(card_number: str) -> str:
    """ "Функцию маскировки номера банковской карты в виде XXXX XX** **** XXXX"""

    return  f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(card_number: str) -> str:
    """ "Функцию маскировки номера банковского счета в виде **XXXX"""
    return f"**{card_number[-4:]}"

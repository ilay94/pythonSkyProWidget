# Настройка логера
import logging

logger = logging.getLogger("mask_log")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/mask_log.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """ "Функцию маскировки номера банковской карты в виде XXXX XX** **** XXXX"""
    logger.debug(f"Маскировка строки: {card_number}")
    if type(card_number) is str and card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        logger.error("Некорректный номер карты")
        return "Некорректный номер карты"


def get_mask_account(card_number: str) -> str:
    """ "Функцию маскировки номера банковского счета в виде **XXXX"""
    logger.debug(f"Маскировка строки: {card_number}")
    if type(card_number) is str and card_number.isdigit() and len(card_number) == 20:
        return f"**{card_number[-4:]}"
    else:
        logger.error("Некорректный номер счета")
        return "Некорректный номер счета"

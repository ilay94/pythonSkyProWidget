import json
import logging

from src.external_api import convert_to_RUB

# Настройка логера
logger = logging.getLogger("utils_log")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils_log.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json_from_file(filepatch: str) -> list:
    """Функицмя чтения json файла, учитываем только списки"""
    try:
        logger.debug(f"Чтение файла {filepatch}")
        with open(filepatch, encoding="utf-8") as f:
            operations = json.load(f)
            if isinstance(operations, list):
                logger.debug(f"Чтение файла {filepatch} завершено успешно")
                return operations
            else:
                logger.debug(f"Файл {filepatch} не содержит список операций")
                return []
    except Exception as e:
        logger.error("В процессе чтения файла возникла ошибка:", exc_info=e)
        return []


def get_amount_rub(operation: dict) -> float:
    """Функция получения суммы проведенной операции в рублях"""
    logger.debug(f"Получения суммы из операции: {operation}")
    try:
        if operation["operationAmount"]["currency"]["code"] != "RUB":
            logger.debug(
                f"Конвертация {operation["operationAmount"]["amount"]}"
                + f"{operation["operationAmount"]["currency"]["code"]}"
            )
            return convert_to_RUB(
                operation["operationAmount"]["amount"],
                operation["operationAmount"]["currency"]["code"],
            )
        else:
            return float(operation["operationAmount"]["amount"])
    except Exception as e:
        logger.error("В получения суммы операции возникла ошибка:", exc_info=e)

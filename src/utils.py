import json

from src.external_api import convert_to_RUB


def read_json_from_file(filepatch: str) -> list:
    """Функицмя чтения json файла, учитываем только списки"""
    try:
        with open(filepatch, encoding="utf-8") as f:
            operations = json.load(f)
            if type(operations) == list:
                return operations
            else:
                return []
    except Exception as e:
        return []


def get_amount_rub(operation: dict) -> float:
    """Функция получения суммы проведенной операции в рублях"""
    if operation["operationAmount"]["currency"]["code"] != "RUB":
        return convert_to_RUB(
            operation["operationAmount"]["amount"],
            operation["operationAmount"]["currency"]["code"],
        )
    else:
        return float(operation["operationAmount"]["amount"])

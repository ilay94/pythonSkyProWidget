def filter_by_currency(transaction: list, currency: str) -> iter:
    """Создает итератор возвращающий только операции по указаной валюте"""

    def get_currency(proces):
        if (
            "operationAmount" in proces
            and "currency" in proces["operationAmount"]
            and "code" in proces["operationAmount"]["currency"]
        ):
            return proces["operationAmount"]["currency"]["code"] == currency
        else:
            return False

    if type(transaction) is not list:
        return iter([])
    return filter(get_currency, transaction)


def transaction_descriptions(transaction: list):
    """Создает генератор возвращающий описание каждой операции по очереди"""
    pass


def card_number_generator(start: int, finish: int):
    """Генерирует последовательность номеров карт"""
    pass

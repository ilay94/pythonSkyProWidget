def filter_by_currency(transactions: list, currency: str) -> iter:
    """Создает итератор возвращающий только операции по указаной валюте"""

    def get_currency(transaction):
        if (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and "code" in transaction["operationAmount"]["currency"]
        ):
            return transaction["operationAmount"]["currency"]["code"] == currency
        else:
            return False

    if type(transactions) is not list:
        return iter([])
    return filter(get_currency, transactions)


def transaction_descriptions(transactions: list):
    """Создает генератор возвращающий описание каждой операции по очереди"""
    if type(transactions) is not list:
        return iter([])

    def get_description(transaction):
        if "description" in transaction and type(transaction["description"]) is str:
            return transaction["description"]
        else:
            return ""

    return [get_description(transaction) for transaction in transactions]


def card_number_generator(start: int, finish: int):
    """Генерирует последовательность номеров карт"""
    pass

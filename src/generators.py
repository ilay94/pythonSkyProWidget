def filter_by_currency(transactions: list, currency: str) -> iter:
    """Создает итератор возвращающий только операции по указанной валюте"""

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


def transaction_descriptions(transactions: list) -> iter:
    """Создает генератор возвращающий описание каждой операции по очереди"""
    if type(transactions) is not list:
        return iter([])

    def get_description(transaction):
        if "description" in transaction and type(transaction["description"]) is str:
            return transaction["description"]
        else:
            return ""

    return [get_description(transaction) for transaction in transactions]


def card_number_generator(start: int, finish: int) -> iter:
    """Генерирует последовательность номеров карт"""

    if type(start) is not int:
        return
    if type(finish) is not int:
        finish = start
    while start <= finish:
        path_1 = start % 10000
        part_2 = (start // 10000) % 10000
        part_3 = (start // 100000000) % 10000
        part_4 = start // 1000000000000
        yield f"{part_4:04d} {part_3:04d} {part_2:04d} {path_1:04d}"
        start += 1

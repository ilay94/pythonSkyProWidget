def filter_by_state(process: list, state: str = "EXECUTED") -> list:
    """ "Функция для фильтрации списка операций по статусу выполнения"""
    return list(filter(lambda proces: proces["state"] == state, process))


def sort_by_date(process: list, order_reverse: bool = True) -> list:
    """ " Функция для сортировки списка операций по дате исполнения"""
    return sorted(process, key=lambda proces: proces["date"], reverse=order_reverse)

def filter_by_state(process: list, state: str = "EXECUTED") -> list:
    """ "Функция для фильтрации списка операций по статусу выполнения"""

    def get_state(proces):
        if "state" in proces:
            return proces["state"] == state
        else:
            return False

    return list(filter(get_state, process))


def sort_by_date(process: list, order_reverse: bool = True) -> list:
    """ " Функция для сортировки списка операций по дате исполнения"""

    def get_date(proces) -> tuple[str, int]:
        if "date" in proces:
            return proces["date"], proces["id"]
        else:
            return "", proces["id"]

    for proces in process:
        date_proces = get_date(proces)[0]
        if not date_proces.replace("-", "").replace(":", "").replace(".", "").replace("T", "").isdigit():
            return []

    return sorted(process, key=get_date, reverse=order_reverse)

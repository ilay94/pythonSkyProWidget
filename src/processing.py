def filter_by_state(process: list, state: str = "EXECUTED") -> list:
    """ "Фильтрует список операций по статусу выполнения"""
    return list(filter(lambda proces: proces["state"] == state, process))

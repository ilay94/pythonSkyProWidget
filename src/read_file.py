import pandas as pd


def get_process_from_csv(filepatch: str) -> list:
    """Функицмя чтения csv файла, и получения списка операций"""
    try:
        csv_frame = pd.read_csv(filepatch, sep=";", header=0)
        return dataFrame_to_process(csv_frame)
    except Exception as e:
        return []


def get_process_from_excel(filepatch: str) -> list:
    """Функицмя чтения excel файла, и получения списка операций"""
    try:
        excel_frame = pd.read_excel(filepatch, header=0)
        return dataFrame_to_process(excel_frame)
    except Exception as e:
        return []


def dataFrame_to_process(dataFrame) -> list:
    """Функицмя преобразования DataFrame в список операций"""
    required_columns = set(
        ["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"]
    )
    if set(dataFrame.columns).issuperset(required_columns):
        return [
            {
                "id": value.id,
                "state": value.state,
                "date": value.date,
                "operationAmount": {
                    "amount": value.amount,
                    "currency": {"name": value.currency_name, "code": value.currency_code},
                },
                "description": value.description,
                "from": value[7],
                "to": value.to,
            }
            for value in dataFrame.itertuples()
        ]
    else:
        raise Exception(f"Отсутствуют колонки {required_columns.difference(set(dataFrame.columns))}")

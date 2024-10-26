import pandas as pd


def get_process_from_csv(filepatch: str) -> list:
    """Функицмя чтения csv файла, учитываем только списки"""
    try:
        csv_frame = pd.read_csv(filepatch, sep=";", header=0)
        result = []
        for value in csv_frame.itertuples():
            result.append({
                "id": value.id,
                "state": value.state,
                "date": value.date,
                "operationAmount": {
                  "amount": value.amount,
                  "currency": {
                    "name": value.currency_name,
                    "code": value.currency_code
                  }
                },
                "description": value.description,
                "from": value[7],
                "to": value.to
              })
        return result
    except Exception as e:
        return []

def get_process_from_excel(filepatch: str) -> list:
    """Функицмя чтения excel файла, учитываем только списки"""
    try:
        excel_frame = pd.read_excel(filepatch, header=0)
        result = []
        for value in excel_frame.itertuples():
            result.append({
                "id": value.id,
                "state": value.state,
                "date": value.date,
                "operationAmount": {
                  "amount": value.amount,
                  "currency": {
                    "name": value.currency_name,
                    "code": value.currency_code
                  }
                },
                "description": value.description,
                "from": value[7],
                "to": value.to
              })
        return result
    except Exception as e:
        return []
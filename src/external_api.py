import json
import os
from dotenv import load_dotenv
import requests

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значения переменной API_KEY из .env-файла
api_key = os.getenv("API_KEY")


def convert_to_RUB(amount: str, code: str) -> float:
    """Функция конвертации суммы проведенной операции в рубли"""

    if type(amount) is str and amount.isdigit() and code in ["USD", "EUR"]:


        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"

        headers = {"apikey": api_key}

        response = requests.get(url, headers=headers, data={})

        status_code = response.status_code
        if 199 < status_code < 300:
            result = json.loads(response.text)
            return float(result["result"])
        else:
            print(f"Запрос не был успешным. Возможная причина: {response.reason}")

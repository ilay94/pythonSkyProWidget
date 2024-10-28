from src.processing import filter_by_description, filter_by_state, sort_by_date
from src.read_file import get_process_from_csv, get_process_from_excel
from src.utils import read_json_from_file
from src.widget import get_date, mask_account_card
def main():
    print(
        """Привет! Добро пожаловать в программу работы 
    с банковскими транзакциями. """
    )

    operations = []
    while True:
        print(
            """Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
        )
        choice = input()
        if choice in ["1", "2", "2"]:
            match choice:
                case "1":
                    operations = read_json_from_file("data/operations.json")
                case "2":
                    print("Для обработки выбран CSV-файл.")
                    operations = get_process_from_csv("data/transactions.csv")
                case "3":
                    print("Для обработки выбран XLSX-файл.")
                    operations = get_process_from_excel("data/transactions_excel.xlsx")
            break
        else:
            print("Выбран неверный формат файла")

    filtered_processing = []

    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию. 
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )
        state = input().upper()
        if state in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Операции отфильтрованы по статусу "{state}".')
            filtered_processing = filter_by_state(operations, state)
            break
        else:
            print(f'Статус операции "{state}" недоступен')

    while True:
        print("Отсортировать операции по дате? Да/Нет")
        sort_date = input().upper()
        if sort_date == "ДА":
            print("По возрастанию или по убыванию? по возрастанию/по убыванию ")
            order = input().lower()
            match order:
                case "по возрастанию":
                    filtered_processing = sort_by_date(filtered_processing)
                    break
                case "по убыванию":
                    filtered_processing = sort_by_date(filtered_processing, False)
                    break
                case _:
                    print(f"Выбрано неверное направление сортировки {order}, сортировка не произведенна")
        elif sort_date == "НЕТ":
            break

    print("Выводить только рублевые транзакции? Да/Нет: ")
    rub_transaction = input().upper()
    if rub_transaction == "ДА":
        filtered_processing = [t for t in filtered_processing if t["currency"] == "RUB"]


    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ")
    filter_desc = input().upper()
    if filter_desc == "ДА":
        word = input("Введите слово для фильтрации: ")
        filtered_processing = filter_by_description(filtered_processing, word)

    print("Распечатываю итоговый список транзакций...")
    if len(filtered_processing) < 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_processing)}")
        for proces in filtered_processing:
            print(f"{get_date(proces["date"])} {proces["description"]}")
            if "from" in proces and "to" in proces:
                print(f"{mask_account_card(proces["from"])} -> {mask_account_card(proces["to"])}")
            elif "from" in proces:
                print(f"{mask_account_card(proces["from"])}")
            elif "to" in proces:
                print(f"{mask_account_card(proces["to"])}")

            print(f"Сумма: {proces["operationAmount"]["amount"]} {proces["operationAmount"]["currency"]["name"]}")
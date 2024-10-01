# Учебный проект банковский виджет

## Описание:

Проект банковский виджет - это приложение на Python для выведения информации о свершенных операциях с картами и счетами.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/ilay94/pythonSkyProWidget.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Тестирование:
Для запуска тестирование воспользуйтесь командой:
#### при активированном виртуальном окружении
```
pytest --cov
```
#### через poetry
```
poetry run pytest --cov
```
#### генерировать отчет о покрытии в HTML-формате, где src — пакет c модулями, которые тестируем
```
pytest --cov=src --cov-report=html
```
## Использование:

Сейчас предоставлен набор функций для обработки входных данных и представления их в нужном виде.

### Модуль mask предоставляет следующий набор функций:
```def get_mask_card_number(card_number: str) -> str:```
Функция маскировки номера банковской карты в виде XXXX XX** **** XXXX

```def get_mask_account(card_number: str) -> str:```
Функция маскировки номера банковского счета в виде **XXXX

### Модуль widget предоставляет следующий набор функций:
```def mask_account_card(account_card: str) -> str:```
Функция маскировки номера карты или счета

```def get_date(date_time: str) -> str:```
Функция форматирования даты к ДД.ММ.ГГГГ

### Модуль processing предоставляет следующий набор функций:
```def filter_by_state(process: list, state: str = "EXECUTED") -> list:```
Функция для фильтрации списка операций по статусу выполнения

```def sort_by_date(process: list, order_reverse: bool = True) -> list:```
Функция для сортировки списка операций по дате исполнения

### Модуль generators предоставляет следующий набор функций:

```filter_by_currency(transactions: list, currency: str) -> iter:```
Создает итератор возвращающий только операции по указанной валюте

```def card_number_generator(start: int, finish: int) -> iter:```
Генерирует последовательность номеров карт

```def transaction_descriptions(transactions: list) -> iter:```
Создает генератор возвращающий описание каждой операции по очереди


## Документация:

Описание доступных функций представлена в виде Docstrings 

## Лицензия:

Этот проект лицензирован по [лицензии MIT](https://choosealicense.com/licenses/mit/).

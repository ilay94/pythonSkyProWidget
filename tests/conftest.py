import pytest


@pytest.fixture
def unmask_card_number():
    return "7000792289606361"


@pytest.fixture
def unmask_account():
    return "73654108430135874305"


@pytest.fixture
def date_and_time():
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def correct_list_process():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def correct_list_process_state_executed():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def correct_list_process_state_canceled():
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_process_without_state():
    return [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sorted_reverse_list_process():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sorted_list_process():
    return [
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
    ]


@pytest.fixture
def incorrect_date_list_process():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "20asdasdadasdasdas29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_process_without_date():
    return [
        {"id": 41428829, "state": "EXECUTED"},
        {"id": 939719570, "state": "EXECUTED"},
        {"id": 594226727, "state": "CANCELED"},
        {"id": 615064591, "state": "CANCELED"},
    ]


@pytest.fixture
def list_process_equal_date():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sorted_list_process_equal_date():
    return [
        {"date": "2019-07-03T18:35:29.512364", "id": 939719570, "state": "EXECUTED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
    ]

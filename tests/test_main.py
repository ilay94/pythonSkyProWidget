import pytest
from unittest.mock import patch

from main import main

@patch('builtins.input', side_effect=['1', 'EXECUTED', 'нет', 'нет', 'нет'])
def test_main(mock_user_input, capsys):
    main()
    captured = capsys.readouterr()
    assert "Распечатываю итоговый список транзакций..." in captured.out


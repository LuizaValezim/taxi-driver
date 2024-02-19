import os
import pytest
from main import main

@pytest.mark.parametrize("file_path, expected_actions", [
    ("./tests/map1.txt", ['go_down', 'go_down', 'go_down', 'go_right', 'go_right', 'go_right', 'go_right', 'go_up', 'go_up', 'go_up', 'go_right', 'pick_up_passenger', 'go_down', 'go_down', 'go_down', 'go_down', 'go_left', 'go_left', 'go_left', 'go_left', 'go_left', 'leave_passenger']),
    ("./tests/map2.txt", ['pick_up_passenger', 'go_down', 'go_left', 'go_left', 'go_left', 'go_left', 'go_left', 'leave_passenger']),
    ("./tests/map3.txt", ['go_down', 'go_down', 'go_right', 'go_right', 'go_down', 'go_right', 'go_right', 'go_right', 'go_right', 'go_up', 'go_up', 'go_up', 'go_left', 'go_left', 'pick_up_passenger', 'go_down', 'go_right', 'go_right', 'go_down', 'go_down', 'go_left', 'go_left', 'go_left', 'go_left', 'go_up', 'go_left', 'go_left', 'go_down', 'go_down', 'leave_passenger']),
    ("./tests/map4.txt", ['go_down', 'go_left', 'go_left', 'go_down', 'go_down', 'go_down', 'go_down', 'go_down', 'pick_up_passenger', 'go_up', 'go_up', 'go_up', 'go_up', 'go_up', 'go_right', 'go_right', 'go_down', 'go_down', 'go_down', 'go_down', 'go_down', 'leave_passenger']),
    ("./tests/map5.txt", ['go_up', 'go_up', 'go_up', 'go_up', 'go_right', 'go_right', 'go_down', 'go_down', 'go_down', 'go_down', 'go_down', 'go_right', 'go_right', 'pick_up_passenger', 'go_up', 'go_up', 'go_up', 'go_up', 'go_up', 'go_right', 'go_right', 'go_down', 'go_down', 'go_down', 'go_down', 'go_down', 'leave_passenger'])  
])

def test_taxi(file_path, expected_actions, capsys):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    map_path = os.path.join(current_dir, file_path)

    main(map_path)

    captured = capsys.readouterr()
    output = captured.out.strip().split('\n')

    if expected_actions:
        assert output[-1] == str(expected_actions)
    else:
        assert output[-1] == "Não foi possível encontrar uma solução."
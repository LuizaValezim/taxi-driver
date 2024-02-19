import sys
from collections import deque

ACTIONS = ['go_down', 'go_up', 'go_right', 'go_left', 'pick_up_passenger', 'leave_passenger']

MOVE_DELTAS = {
    'go_down': (1, 0),
    'go_up': (-1, 0),
    'go_right': (0, 1),
    'go_left': (0, -1),
    'pick_up_passenger': (0, 0),
    'leave_passenger': (0, 0)
}

def read_map(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]

def is_valid_move(map, position):
    return 0 <= position[0] < len(map) and 0 <= position[1] < len(map[0]) and map[position[0]][position[1]] != 'B'

def bfs(map, start, goal):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        current_position, actions = queue.popleft()

        if current_position == goal:
            return actions

        for action in ACTIONS:
            new_position = tuple(current_position[i] + MOVE_DELTAS[action][i] for i in range(2))

            if is_valid_move(map, new_position) and new_position not in visited:
                if action == 'pick_up_passenger' and current_position != find_position(map, 'P'):
                    continue
                if action == 'leave_passenger' and current_position != find_position(map, 'G'):
                    continue
                if action in ['go_down', 'go_up', 'go_right', 'go_left']:
                    if action == 'go_down' and map[current_position[0]+1][current_position[1]] == 'B':
                        continue
                    if action == 'go_up' and map[current_position[0]-1][current_position[1]] == 'B':
                        continue
                    if action == 'go_right' and map[current_position[0]][current_position[1]+1] == 'B':
                        continue
                    if action == 'go_left' and map[current_position[0]][current_position[1]-1] == 'B':
                        continue
                queue.append((new_position, actions + [action]))
                visited.add(new_position)

    return None

def find_position(map, char):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == char:
                return (i, j)
    return None

def main(file_path):
    map = read_map(file_path)

    start = find_position(map, 'T')

    if find_position(map, 'P') != None:
        passenger_start = find_position(map, 'P')
        passenger_goal = find_position(map, 'G')

        actions_to_passenger = bfs(map, start, passenger_start)
        actions_to_goal = bfs(map, passenger_start, passenger_goal)

        if actions_to_goal:
            actions = actions_to_passenger + ['pick_up_passenger'] + actions_to_goal
            actions.append('leave_passenger')  
        else:
            actions = actions_to_passenger  

        if actions:
            print(actions)
        else:
            print("Não foi possível encontrar uma solução.")
    
    else:
        passenger_goal = find_position(map, 'G')
        actions_to_goal = bfs(map, start, passenger_goal)

        actions = ['pick_up_passenger'] + actions_to_goal
        actions.append('leave_passenger')  

        if actions:
            print(actions)
        else:
            print("Não foi possível encontrar uma solução.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python nome_do_arquivo.py <caminho_do_arquivo>")
        sys.exit(1)
    file_path = sys.argv[1]
    main(file_path)
def import_and_process_data():
    with open("day_06/input.txt", "r") as file:
        lines = file.read().split("\n")
    return [list(item) for item in lines]


def get_initial_guard_poss(input_map):
    for x_idx, row in enumerate(input_map):
        for y_idx, char in enumerate(row):
            if char == "^":
                return x_idx, y_idx, "up"


def move(row, col, direction):
    if direction == "right":
        return move_right(row, col)
    elif direction == "left":
        return move_left(row, col)
    elif direction == "up":
        return move_up(row, col)
    elif direction == "down":
        return move_down(row, col)
    else:
        raise ValueError(f"Direction provided not available: {direction}")


def move_up(row, col):
    return row - 1, col


def move_down(row, col):
    return row + 1, col


def move_left(row, col):
    return row, col - 1


def move_right(row, col):
    return row, col + 1


def check_if_wall_in_front(input_map, row, col, direction):
    if direction == "right":
        return input_map[row][col + 1] == "#"

    elif direction == "left":
        return input_map[row][col - 1] == "#"

    elif direction == "up":
        return input_map[row - 1][col] == "#"

    elif direction == "down":
        return input_map[row + 1][col] == "#"

    else:
        raise ValueError(f"Direction provided not available: {direction}")


def guard_step(input_map, row, col, direction):
    try:
        wall_in_front = check_if_wall_in_front(input_map, row, col, direction)
    except IndexError:
        wall_in_front = False
    if wall_in_front:
        if direction == "right":
            return row, col, "down"

        elif direction == "down":
            return row, col, "left"

        elif direction == "left":
            return row, col, "up"

        elif direction == "up":
            return row, col, "right"
    return *move(row, col, direction), direction


def check_if_guard_still_here(input_map, row, col):
    return not (
        row < 0
        or col < 0
        or row > (len(input_map[0]) - 1)
        or col > (len(input_map) - 1)
    )


def add_wall(input_map, row, col):
    input_map[row][col] = "#"
    return input_map


def remove_wall(input_map, row, col):
    input_map[row][col] = "."
    return input_map


def run_guard_walk(input_map, row, col, direction):
    initial_state = (row, col, direction)
    visited_states = set()
    visited_states.add(initial_state)
    guard_still_here = True
    while guard_still_here:
        row, col, direction = guard_step(input_map, row, col, direction)
        if (row, col, direction) in visited_states:
            return True
        visited_states.add((row, col, direction))
        guard_still_here = check_if_guard_still_here(input_map, row, col)
    return False


def find_loops(input_map, row, col, direction):
    count = 0
    for i in range(len(input_map)):
        for j in range(len(input_map[i])):
            if input_map[i][j] == ".":
                input_map = add_wall(input_map, i, j)
                count += run_guard_walk(input_map, row, col, direction)
                input_map = remove_wall(input_map, i, j)
            print(f"Testing ROW: {i}, COL {j}. Loops found: {count}")
    return count


if __name__ == "__main__":
    input_map = import_and_process_data()[:-1]
    row, col, direction = get_initial_guard_poss(input_map)
    result = find_loops(input_map, row, col, direction)
    print(f"Solution: {result}")

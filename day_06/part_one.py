def import_and_process_data():
    with open("day_06/input.txt", "r") as file:
        file = file.read().split("\n")
        return file

def get_initial_guard_poss(input_map):
    for x_idx, row in enumerate(input_map):
        for y_idx, char in enumerate(row):
            if char == "^":
                return x_idx, y_idx, "up"

def guard_movement(input_map, row, col, direction):
    # Guard goes to RIGHT
    if direction == "right":
        if input_map[row][col+1] == "#":
            return row, col, "down"
        else:
            return row, col+1, direction

    # Guard goes DOWN
    elif direction == "down":
        if input_map[row+1][col] == "#":
            return row, col, "left"
        else:
            return row+1, col, direction

    # Guard goes LEFT
    elif direction == "left":
        if input_map[row][col-1] == "#":
            return row, col, "up"
        else:
            return row, col-1, direction

    # Guard goes UP
    elif direction == "up":
        if input_map[row-1][col] == "#":
            return row, col, "right"
        else:
            return row-1, col, direction

if __name__ == "__main__":
    input_map = import_and_process_data()[:-1]
    row, col, direction = get_initial_guard_poss(input_map)
    all_directions = []
    guard_still_here = True
    while guard_still_here:
        try:
            coord = (row, col)
            if coord not in all_directions:
                all_directions.append(coord)
            row, col, direction = guard_movement(input_map, row, col, direction)
            if row < 0 or col < 0:
                guard_still_here = False
        except IndexError:
            guard_still_here = False
    print(f"Solution: {len(set(all_directions))}")
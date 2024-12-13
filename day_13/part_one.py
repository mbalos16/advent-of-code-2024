def import_and_process_data():
    with open("day_13/input.txt", "r") as file:
        lines = file.readlines()
        machines = []
        new_machine = []
        for elem in lines:
            if elem != "\n":
                new_machine.append(elem.rstrip())
            else:
                machines.append(new_machine)
                new_machine = []
    return machines


def get_machine_coords(machine):
    x_a = machine[0][12:14]
    y_a = machine[0][18:]

    x_b = machine[1][12:14]
    y_b = machine[1][18:]

    prize = machine[2][9:].split(",")
    x_prize = prize[0]
    y_prize = prize[1][3:]
    return int(x_a), int(y_a), int(x_b), int(y_b), int(x_prize), int(y_prize)


def get_buttons_coords(x_a, y_a, x_b, y_b, x_prize, y_prize):
    coords_a = [[0, 0]]
    coords_b = [[x_prize, y_prize]]
    for i in range(100):
        coords_a.append([coords_a[-1][0] + x_a, coords_a[-1][1] + y_a])
        coords_b.append([coords_b[-1][0] - x_b, coords_b[-1][1] - y_b])
    return coords_a, coords_b


def get_tokens(coords_a, coords_b, x_prize, y_prize):
    # Check if buttons arribe at opposite destination
    a_arrived = False
    b_arrived = False
    if [x_prize, y_prize] in coords_a:
        a_arrived = True
        steps_a = coords_a.index([z_prize, y_prize])
    if [0, 0] in coords_b:
        b_arrived = True
        steps_b = coords_b.index([0, 0])

    # Check intersection
    intersection = False
    for idx_loc, location in enumerate(coords_a):
        if location in coords_b:
            intersection = True
            tokens_a = idx_loc
            tokens_b = coords_b.index(location)

    if a_arrived and b_arrived:
        tokens_a = steps_a * 3
        tokens_b = steps_b * 1
        return min(tokens_a, tokens_b)
    elif a_arrived:
        return steps_a * 3
    elif b_arrived:
        return steps_b * 1
    elif intersection:
        return tokens_a * 3 + tokens_b * 1
    return 0


if __name__ == "__main__":
    input_data = import_and_process_data()
    tokens_count = 0
    for machine in range(len(input_data)):
        x_a, y_a, x_b, y_b, x_prize, y_prize = get_machine_coords(input_data[machine])
        coords_a, coords_b = get_buttons_coords(x_a, y_a, x_b, y_b, x_prize, y_prize)
        tokens_count += get_tokens(coords_a, coords_b, x_prize, y_prize)
    print(tokens_count)

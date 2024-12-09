def import_and_process_data():
    with open("day_08/input.txt", "r") as file:
        lines = file.readlines()
    lines = [x.strip() for x in lines]
    return lines


def process_data(input_data):
    input_data_new = []
    for row in input_data:
        input_data_new.append(list(row))
    return input_data_new


def get_antenas_types_and_coord(input_data):
    antenas_coords = {}
    for idx_row, row in enumerate(input_data):
        for idx_char, char in enumerate(row):
            if char != ".":
                if char in antenas_coords:
                    antenas_coords[char].append((idx_row, idx_char))
                else:
                    antenas_coords[char] = []
                    antenas_coords[char].append((idx_row, idx_char))
    return antenas_coords


def find_antinode(coord_one, coord_two):
    return (
        coord_two[0] + coord_two[0] - coord_one[0],
        coord_two[1] + coord_two[1] - coord_one[1],
    )


def create_pairs_of_antenas(antenas_pos):
    antenas_coords = []
    for i in antenas_pos:
        for j in antenas_pos:
            if i != j:
                antenas_coords.append([i, j])
    return antenas_coords


def get_all_antinodes(pairs_of_coords):
    antinodes = set()
    for elem in pairs_of_coords:
        antinode_one = find_antinode(elem[0], elem[1])
        antinode_two = find_antinode(elem[1], elem[0])
        antinodes.add(antinode_one)
        antinodes.add(antinode_two)
    return antinodes


def is_coord_in_map(coord, input_map):
    if coord[0] < len(input_map) and coord[0] >= 0:
        if coord[1] < len(input_map[0]) and coord[1] >= 0:
            return True
    return False


if __name__ == "__main__":
    input_data = import_and_process_data()
    input_data = process_data(input_data)
    antenas_coords = get_antenas_types_and_coord(input_data)

    pairs_of_coords = []
    for antena_type, coordinate in antenas_coords.items():
        pairs_of_coords += create_pairs_of_antenas(coordinate)

    antinodes = get_all_antinodes(pairs_of_coords)

    result = 0
    for antinode in antinodes:
        result += is_coord_in_map(antinode, input_map=input_data)
    print(f"Solution: {result}")

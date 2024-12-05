import math

import numpy as np


def import_and_process_data():
    with open("day_04/input.txt", "r") as file:
        file = file.readlines()
        new_file = []
        for row in file:
            new_file.append(list(row.replace("\n", "")))
        return new_file


def count_characters(input_data):
    count = 0
    for row in input_data:
        row = "".join(row)
        for i in range(len(row)):
            if row[i:].startswith("XMAS"):
                count += 1
    return count


def horizontal_flip(input_data):
    new_data = []
    for row in input_data:
        new_data.append(row[::-1])
    return new_data


def vertical_flip(input_data):
    return np.transpose(input_data)


def get_all_diagonals(input_data):
    new_data = []
    for i in range(-len(input_data), len(input_data)):
        new_data.append(np.linalg.diagonal(input_data, offset=i))
        new_data.append(np.linalg.diagonal(input_data, offset=i)[::-1])
    return new_data


if __name__ == "__main__":
    input_data = import_and_process_data()
    count = count_characters(input_data)

    # Transform the data horrizontally
    horizontal = horizontal_flip(input_data)
    count += count_characters(horizontal)

    # Transform the data vertically
    vertical = vertical_flip(input_data)
    count += count_characters(vertical)

    # Transform the horizontal vertically
    v = vertical_flip(input_data)
    h = horizontal_flip(v)
    count += count_characters(h)

    # Check the diagonal
    diagonal = get_all_diagonals(input_data)
    count += count_characters(diagonal)

    # Check the flipped diagonal
    diagonal = get_all_diagonals(horizontal)
    count += count_characters(diagonal)

    print(f"Solution: {count}")

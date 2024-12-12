import math


def import_and_process_data():
    with open("day_11/input.txt", "r") as file:
        content = file.read()
    return content.split(" ")


def split_stone_in_two(stone):
    stone_len = math.floor(len(stone) / 2)
    new_elem_one = stone[:stone_len]
    new_elem_two = stone[stone_len:]
    return str(int(new_elem_one)), str(int(new_elem_two))


def multiply_stone(stone):
    return str(int(stone) * 2024)


def blink_once(input_data):
    new_input_data = []
    for i in range(len(input_data)):
        if input_data[i] == "0":
            new_input_data.append("1")
        elif len(input_data[i]) % 2 == 0:
            new_elem_one, new_elem_two = split_stone_in_two(input_data[i])
            new_input_data.append(new_elem_one)
            new_input_data.append(new_elem_two)
        else:
            new_input_data.append(multiply_stone(input_data[i]))

    return new_input_data


if __name__ == "__main__":
    input_data = import_and_process_data()
    iterations = 0
    while iterations < 25:
        input_data = blink_once(input_data)
        iterations += 1
    print(f"Solution: {len(input_data)}")

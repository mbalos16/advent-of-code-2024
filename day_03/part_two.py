import re


def import_and_process_data():
    with open("day_03/input.txt", "r") as file:
        return file.read()


def create_new_input(input_data):
    allow_save = True
    new_input = ""
    i = 0
    while i < len(input_data):
        if input_data[i:].startswith("do()"):
            allow_save = True
        elif input_data[i:].startswith("don't()"):
            allow_save = False
        if allow_save == True:
            new_input += input_data[i]
        i += 1
    return new_input


def multiply_numbers(input_data):
    count = 0
    re_pattern = re.compile("mul\((\d+),(\d+)\)")
    for num1, num2 in re.findall(re_pattern, input_data):
        count += int(num1) * int(num2)
    return count


if __name__ == "__main__":
    input_data = import_and_process_data()
    input_data = create_new_input(input_data)
    result = multiply_numbers(input_data)
    print(f"Solution: {result}")

import itertools


def import_and_process_data():
    with open("day_07/input.txt", "r") as file:
        lines = file.readlines()
    lines = [x.strip() for x in lines]
    return lines


def process_data(inpt_data):
    list_elements = [item.split(": ") for item in input_data]
    processed_data = []
    for element in list_elements:
        new_elem = [int(element[0]), [int(item) for item in element[1].split(" ")]]
        processed_data.append(new_elem)
    return processed_data


def check_longest_operation(input_data):
    longest_opp = 0
    for elem in input_data:
        if len(elem[1]) > longest_opp:
            longest_opp = len(elem[1])
    return 2 ** (longest_opp - 1)


def calculate(list_of_elem, operations):
    result = 0
    for idx, elem in enumerate(list_of_elem):
        if idx == 0:
            result = elem
        else:
            op = operations[idx - 1]
            if op == "+":
                result += elem
            elif op == "*":
                result *= elem
    return result


def check_all_possible_combinations(goal, list_of_elem):
    candidate_operations = list(itertools.product(["+", "*"], repeat=len(elem[1]) - 1))
    for operations in candidate_operations:
        result = calculate(list_of_elem, operations)
        if result == goal:
            return True
    return False


if __name__ == "__main__":
    input_data = import_and_process_data()
    data = process_data(input_data)
    longest_operation = check_longest_operation(data)
    print(f"Longest operation: {longest_operation}")

    # Get all lists:
    result = 0
    for elem in data:
        if check_all_possible_combinations(elem[0], elem[1]) == True:
            result += elem[0]
    print(f"Solution: {result}")

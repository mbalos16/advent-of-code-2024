def import_and_process_data():
    with open("input.txt", "r") as file:
        return file.read().split()


def generate_sorted_left_right_lists(input_numbers: str) -> list:
    left_list = []
    right_list = []

    for i in range(0, len(input_list), 2):
        left_list.append(int(input_list[i]))
        right_list.append(int(input_list[i + 1]))
    return sorted(left_list), sorted(right_list)


def calculate_distance(left, right) -> int:
    count = 0
    for i in range(len(left)):
        left_elem = left[i]
        right_elem = right[i]

        # Calculate the total distance
        if left_elem > right_elem:
            count += left_elem - right_elem
        elif right_elem > left_elem:
            count += right_elem - left_elem
    return count


if __name__ == "__main__":
    input_list = import_and_process_data()
    left, right = generate_sorted_left_right_lists(input_numbers=input_list)
    result = calculate_distance(left, right)
    print(f"Solution: {result}")

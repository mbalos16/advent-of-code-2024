def import_and_process_data():
    with open("input.txt", "r") as file:
        return file.read().split()


def generate_left_right_lists(input_list: str) -> list:
    left_list = []
    right_list = []

    for i in range(0, len(input_list), 2):
        left_list.append(int(input_list[i]))
        right_list.append(int(input_list[i + 1]))

    return left_list, right_list


def calculate_similarity(left, right):
    similarity_count = 0
    for elem in left:
        similarity_count += elem * right.count(elem)
    return similarity_count


if __name__ == "__main__":
    input_list = import_and_process_data()
    left, right = generate_left_right_lists(input_list=input_list)
    similarity_count = calculate_similarity(left, right)
    print(f"Solution: {similarity_count}")

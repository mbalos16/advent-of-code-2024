import math


def import_and_process_data():
    with open("day_05/input.txt", "r") as file:
        return file.read()


def process_data(input_data):
    input_data = input_data.split("\n\n")
    # Condition
    conditions = [item.split("|") for item in input_data[0].split("\n")]

    # Sequences
    sequences = [item.split("\n") for item in input_data[1].split("\n")]
    final_sequence = []
    for sequence in sequences:
        for page in sequence:
            final_sequence.append(page.split(","))
    return conditions, final_sequence


def valid_sequence(sequence, rule):
    page = rule[0]
    if page in sequence:
        if rule[1] in sequence[: sequence.index(page)]:
            return False
    return True


def find_valid_invalid_sequences(sequences, conditions):
    # Find all valid and non_valid
    valid_sequences = []
    non_valid_sequences = []
    for sequence in sequences:
        valid_sequence_count = 0
        for rule in conditions:
            if valid_sequence(sequence, rule) == True:
                valid_sequence_count += 1
        if valid_sequence_count == len((conditions)):
            valid_sequences.append(sequence)
        else:
            for i in range(len(sequence)):
                new_sequence = sequence[i:] + sequence[:i]
            non_valid_sequences.append(sequence)
    return valid_sequences, non_valid_sequences


def get_middle_page(valid_sequences):
    result = 0
    for sequence in valid_sequences:
        if len(sequence) > 1:
            idx = math.floor(len(sequence) / 2)
            result += int(sequence[idx])
    return result


if __name__ == "__main__":
    input_data = import_and_process_data()
    conditions, sequences = process_data(input_data=input_data)
    valid_sequences, invalid_sequences = find_valid_invalid_sequences(
        sequences=sequences, conditions=conditions
    )
    result = get_middle_page(valid_sequences)

    print(f"Solution: {result}")

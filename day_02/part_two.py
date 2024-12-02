def import_and_process_data():
    with open("day_02/input.txt", "r") as file:
        return file.read()


def process_data(data):
    return [item.split() for item in data.split("\n")]


def is_safe(report):
    # Register the number of strictly increassing / strictly decreassing numbers in a report
    report_count = {
        "strictly_increassing": 0,
        "strictly_decreassing": 0,
    }
    last_level = 0
    # Iterate over all the levels
    for idx, levels in enumerate(report):
        levels = int(levels)
        if idx == 0:
            last_level = levels
        else:
            # Check stricktly increassing
            if levels > last_level and levels - last_level in [1, 2, 3]:
                report_count["strictly_increassing"] += 1

            # Chreck strictly decreasing
            elif levels < last_level and last_level - levels in [1, 2, 3]:
                report_count["strictly_decreassing"] += 1

            # Asign actual level as the last level for the next round
            last_level = levels

        if (
            report_count["strictly_increassing"] == len(report) - 1
            or report_count["strictly_decreassing"] == len(report) - 1
        ):
            return True
    return False


def one_error(report):
    count = 0
    for i in range(len(report)):
        new_report = report[:i] + report[i + 1 :]
        if is_safe(new_report):
            count += 1
        if count == 1:
            return True
    return False


def check_strictly_conditions(data):
    safe_reports = 0
    for report in data:
        if is_safe(report) or one_error(report):
            safe_reports += 1
    return safe_reports


if __name__ == "__main__":
    input_data = import_and_process_data()
    process_data = process_data(input_data)

    result = check_strictly_conditions(process_data)
    print(f"Solution: {result}")

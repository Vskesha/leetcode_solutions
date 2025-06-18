from pathlib import Path

BLOCKED_TASKS = {
    0,
}


def get_first_missing_task(number_from: int = 1) -> int:
    curr_path = Path(__file__).parent.absolute()

    files_set = set()

    for item in curr_path.iterdir():
        if (
            item.is_file()
            and item.suffix == ".py"
            and item.name.startswith("p")
            and len(item.name) >= 8
            and item.name[1:5].isdigit()
            and item.name[5] == "_"
        ):
            try:
                task_number = int(item.name[1:5])
                files_set.add(task_number)
            except ValueError:
                pass

    files_set.update(BLOCKED_TASKS)
    for i in range(number_from, 10000):
        if i not in files_set:
            return i

    return 10000


if __name__ == "__main__":
    fmt = get_first_missing_task()
    print(f"The first missing task number is: {fmt}")

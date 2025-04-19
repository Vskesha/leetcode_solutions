from pathlib import Path


def get_first_missing_task(number_from=1):
    p = Path(__file__).parent.absolute()

    files_set = set()

    for f in p.iterdir():
        if (
                f.is_file()
                and f.suffix == '.py'
                and f.name.startswith('p')
                and len(f.name) >= 8
                and f.name[1:5].isdigit()
                and f.name[5] == '_'
        ):
            try:
                task_number = int(f.name[1:5])
                files_set.add(task_number)
            except ValueError:
                pass

    for i in range(number_from, 10000):
        if i not in files_set:
            return i

    return 10000


if __name__ == '__main__':
    fmt = get_first_missing_task()
    print(f'The first missing task number is: {fmt}')

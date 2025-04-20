from pathlib import Path
from typing import List


def get_tasks_without_tests(path_to_folder: str | Path) -> List[str]:
    p = Path(path_to_folder)

    files = []

    for f in p.iterdir():
        msg = f'Processing {f.name}'
        print(msg, end='', flush=True)

        if (
            f.is_file()
            and f.suffix == '.py'
            and f.name.startswith('p')
            and len(f.name) >= 8
            and f.name[1:5].isdigit()
            and f.name[5] == '_'
        ):
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
                if 'TestCase' not in content:
                    files.append(f.name)
        print('\r' + ' ' * len(msg) + '\r', end='', flush=True)

    files.sort()
    return files


if __name__ == '__main__':
    current_dir = Path(__file__).parent.absolute()
    files = get_tasks_without_tests(current_dir)
    for file in files:
        print(file)
    print(f'Found {len(files)} tasks without tests.')

from pathlib import Path
from typing import List


def get_tasks_without_tests(path_to_folder: str | Path) -> List[str]:
    curr_path = Path(path_to_folder)

    files = []

    for item in curr_path.iterdir():
        msg = f"Processing {item.name}"
        print(msg, end="", flush=True)

        if (
            item.is_file()
            and item.suffix == ".py"
            and item.name.startswith("p")
            and len(item.name) >= 8
            and item.name[1:5].isdigit()
            and item.name[5] == "_"
        ):
            with open(item, "r", encoding="utf-8") as file:
                content = file.read()
                if "TestCase" not in content:
                    files.append(item.name)
        print("\r" + " " * len(msg) + "\r", end="", flush=True)

    files.sort()
    return files


if __name__ == "__main__":
    current_dir = Path(__file__).parent.absolute()
    files = get_tasks_without_tests(current_dir)
    for curr_file in files:
        print(curr_file)
    print(f"Found {len(files)} tasks without tests.")

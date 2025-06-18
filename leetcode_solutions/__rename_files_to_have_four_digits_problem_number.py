from pathlib import Path


def rename_not_four_digit() -> None:
    current_folder = Path(__file__).parent

    for item in current_folder.iterdir():
        if item.is_file() and item.name.startswith("p"):
            name = item.name
            i = name.index("_")
            if i == 5:
                continue
            print(name, end="  -->  ")
            new_name = "p" + "0" * (5 - i) + name[1:]
            print(new_name)
            item.rename(new_name)


if __name__ == "__main__":
    rename_not_four_digit()

from pathlib import Path


def main() -> None:
    number_of_right_named = 0
    number_of_other_files = 0

    curr_path = Path(__file__).parent.absolute()

    for item in curr_path.iterdir():
        name = item.name
        if item.is_file() and name.endswith(".py"):
            if name.startswith("p") and name[1].isdigit():
                number_of_right_named += 1
            elif name[0] != "_":
                number_of_other_files += 1

    print(f"Number of right named solutions: {number_of_right_named}")
    print(f"Number of other files: {number_of_other_files}")


if __name__ == "__main__":
    main()

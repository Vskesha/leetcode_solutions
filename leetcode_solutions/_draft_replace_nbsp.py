from pathlib import Path


def replace_nbsp_in_file(file_path):
    path = Path(file_path)
    if not path.is_file():
        print(f"File not found: {file_path}")
        return

    # Read content
    text = path.read_text(encoding="utf-8")

    # Replace non-breaking spaces
    text = text.replace("\xa0", " ").replace("&nbsp;", " ")

    # Write back the modified content
    path.write_text(text, encoding="utf-8")
    print(f"Replaced non-breaking spaces in: {file_path}")


if __name__ == "__main__":
    replace_nbsp_in_file("_draft.py")

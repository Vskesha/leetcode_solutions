import re


def main() -> None:
    inp = input("Type title of the problem: ")

    filename = re.sub(
        r"[^a-zA-Z0-9]+",
        "_",
        inp.lower().strip().replace("'", "")
    ) + ".py"

    if filename[0].isdigit():
        i = filename.index("_")
        filename = "p" + "0" * (4 - i) + filename

    test_class_template = """import unittest

from leetcode_solutions._test_meta import TestMeta



class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            # "cls_init_args": [],
            # "cls_init_kwargs": dict(),
            "class_methods": ["class_method"] * n,
            # "args": [[], ],
            "kwargs": [
                dict(),
            ],
            "expected": [],
            # "assert_methods": ["assertMethod"] * n,
        },
    ]


if __name__ == "__main__":
    unittest.main()
"""

    with open(filename, "x") as file:
        file.write(test_class_template)


    print(f"Created file: {filename}")


if __name__ == "__main__":
    main()

"""
Example of test class using "TestMeta":

import unittest

from leetcode_solutions._test_meta import TestMeta


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            # "cls_init_args": [],
            # "cls_init_kwargs": dict(),
            "class_methods": ["class_method"] * n,
            # "args": [[], ],
            "kwargs": [
                dict(),
            ],
            "expected": [],
            # "assert_methods": ["assertMethod"] * n,
        },
    ]


if __name__ == "__main__":
    unittest.main()

"""

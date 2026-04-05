import unittest

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        mat = []
        le = len(encodedText)
        lr = le // rows + rows - 1

        for i in range(rows):
            ss = encodedText[i::rows]
            mat.append(" " * i + ss + " " * (lr - i - len(ss)))

        return "".join(mat)


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["decodeCiphertext"] * 3,
            "kwargs": [
                dict(encodedText="ch   ie   pr", rows=3),
                dict(),
                dict(),
            ],
            "expected": [],
            # "assert_methods": ["assertMethod"] * n,
        },
    ]


if __name__ == "__main__":
    unittest.main()

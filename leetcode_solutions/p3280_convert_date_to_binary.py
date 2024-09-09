import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join(f"{int(k):b}" for k in date.split("-"))


class Solution2:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join(bin(int(k))[2:] for k in date.split("-"))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["convertDateToBinary"] * 2,
            "kwargs": [
                dict(date="2080-02-29"),
                dict(date="1900-01-01"),
            ],
            "expected": ["100000100000-10-11101", "11101101100-1-1"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

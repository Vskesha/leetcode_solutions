import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def checkRecord(self, s: str) -> bool:
        return "LLL" not in s and s.count("A") < 2


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["checkRecord"] * 2,
            "kwargs": [
                dict(s="PPALLP"),
                dict(s="PPALLL"),
            ],
            "expected": [True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return not sum(derived) % 2


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["doesValidArrayExist"] * 3,
            "kwargs": [
                dict(derived=[1, 1, 0]),
                dict(derived=[1, 1]),
                dict(derived=[1, 0]),
            ],
            "expected": [True, True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

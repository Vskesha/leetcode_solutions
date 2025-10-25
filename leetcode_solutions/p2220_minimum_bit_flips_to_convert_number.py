import unittest
from itertools import zip_longest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return sum(
            a != b
            for a, b in zip_longest(
                bin(start)[:1:-1], bin(goal)[:1:-1], fillvalue="0"
            )
        )


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minBitFlips"] * 2,
            "kwargs": [
                dict(start=10, goal=7),
                dict(start=3, goal=4),
            ],
            "expected": [3, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()

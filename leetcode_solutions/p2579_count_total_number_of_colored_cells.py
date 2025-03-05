import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * n * (n - 1) + 1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["coloredCells"] * 3,
            "kwargs": [
                dict(n=1),
                dict(n=2),
                dict(n=3),
            ],
            "expected": [1, 5, 13],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def sumZero(self, n: int) -> List[int]:
        return list(range(1, n)) + [-(n * (n - 1) // 2)]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["sumZero"] * 3,
            "kwargs": [
                dict(n=5),
                dict(n=3),
                dict(n=1),
            ],
            "expected": [[-7, -1, 1, 3, 4], [-1, 0, 1], [0]],
            "assert_methods": ["assertSumZero"] * 3,
        },
    ]

    def assertSumZero(self, actual: list[int], expected: list[int]):
        self.assertEqual(len(actual), len(expected))
        self.assertEqual(sum(expected), 0)
        self.assertEqual(sum(actual), 0)


if __name__ == "__main__":
    unittest.main()

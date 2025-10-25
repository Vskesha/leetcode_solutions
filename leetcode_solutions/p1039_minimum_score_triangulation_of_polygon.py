import unittest
from functools import cache
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        @cache
        def dfs(left: int, right: int) -> int:
            return min(
                (
                    values[left] * values[right] * values[k]
                    + dfs(left, k)
                    + dfs(k, right)
                    for k in range(left + 1, right)
                ),
                default=0,
            )

        return dfs(0, len(values) - 1)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minScoreTriangulation"] * 3,
            "kwargs": [
                dict(values=[1, 2, 3]),
                dict(values=[3, 7, 4, 5]),
                dict(values=[1, 3, 1, 4, 1, 5]),
            ],
            "expected": [6, 144, 13],
        },
    ]


if __name__ == "__main__":
    unittest.main()

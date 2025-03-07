import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        rep = 0
        seen = set()
        for row in grid:
            for val in row:
                if val in seen:
                    rep = val
                else:
                    seen.add(val)

        n = pow(len(grid), 2)
        mis = n * (n + 1) // 2 - sum(seen)

        return [rep, mis]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findMissingAndRepeatedValues"] * 2,
            "kwargs": [
                dict(grid = [[1,3],[2,2]]),
                dict(grid = [[9,1,7],[8,9,2],[3,4,6]]),
            ],
            "expected": [
                [2, 4],
                [9, 5],
            ],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

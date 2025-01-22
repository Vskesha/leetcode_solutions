import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        if n == 1:
            return 0

        acc1, acc2 = sum(grid[0]), 0
        for i in range(n):
            acc1 -= grid[0][i]
            if acc1 <= acc2:
                curr = max(acc1, acc2)
                prev = max(acc1 + grid[0][i], acc2 - grid[1][i - 1])
                return min(curr, prev)
            acc2 += grid[1][i]


class Solution2:
    def gridGame(self, grid: List[List[int]]) -> int:
        ans = acc1 = sum(grid[0])
        acc2 = 0
        for a, b in zip(*grid):
            acc1 -= a
            ans = min(ans, max(acc1, acc2))
            acc2 += b
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["gridGame"] * 3,
            "kwargs": [
                dict(grid=[[2, 5, 4], [1, 5, 1]]),
                dict(grid=[[3, 3, 1], [8, 5, 2]]),
                dict(grid=[[1, 3, 1, 15], [1, 3, 3, 1]]),
            ],
            "expected": [4, 4, 7],
        },
    ]


if __name__ == "__main__":
    unittest.main()

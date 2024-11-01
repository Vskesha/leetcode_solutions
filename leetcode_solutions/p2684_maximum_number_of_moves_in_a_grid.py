import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pcol = set(range(m))

        for j in range(1, n):
            col = set()
            for i in pcol:
                if i and grid[i][j - 1] < grid[i - 1][j]:
                    col.add(i - 1)
                if grid[i][j - 1] < grid[i][j]:
                    col.add(i)
                if i < m - 1 and grid[i][j - 1] < grid[i + 1][j]:
                    col.add(i + 1)
            if not col:
                return j - 1
            pcol = col

        return n - 1

class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxMoves"] * 2,
            "kwargs": [
                dict(grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]),
                dict(grid = [[3,2,4],[2,1,9],[1,1,7]]),
            ],
            "expected": [3, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

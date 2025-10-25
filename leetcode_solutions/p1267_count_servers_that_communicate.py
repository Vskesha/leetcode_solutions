import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [sum(row) for row in grid]
        cols = [sum(col) for col in zip(*grid)]

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (rows[i] > 1 or cols[j] > 1):
                    ans += 1
        return ans


class Solution2:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols = [0] * m, [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                if rows[i] == 2:
                    break
        for j in range(n):
            for i in range(m):
                cols[j] += grid[i][j]
                if cols[j] == 2:
                    break
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (rows[i] == 2 or cols[j] == 2):
                    ans += 1
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countServers"] * 3,
            "kwargs": [
                dict(grid=[[1, 0], [0, 1]]),
                dict(grid=[[1, 0], [1, 1]]),
                dict(
                    grid=[
                        [1, 1, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1],
                    ]
                ),
            ],
            "expected": [0, 3, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[0] * n for _ in range(m)]
        for r, c in guards:
            grid[r][c] = 2
        for r, c in walls:
            grid[r][c] = 3
        for r, c in guards:
            for i in range(r - 1, -1, -1):
                if grid[i][c] > 1:
                    break
                grid[i][c] = 1
            for i in range(r + 1, m):
                if grid[i][c] > 1:
                    break
                grid[i][c] = 1
            for j in range(c - 1, -1, -1):
                if grid[r][j] > 1:
                    break
                grid[r][j] = 1
            for j in range(c + 1, n):
                if grid[r][j] > 1:
                    break
                grid[r][j] = 1

        cnt = 0
        for row in grid:
            for val in row:
                if val == 0:
                    cnt += 1

        return cnt


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countUnguarded"] * 2,
            "kwargs": [
                dict(
                    m=4,
                    n=6,
                    guards=[[0, 0], [1, 1], [2, 3]],
                    walls=[[0, 1], [2, 2], [1, 4]],
                ),
                dict(m=3, n=3, guards=[[1, 1]], walls=[[0, 1], [1, 0], [2, 1], [1, 2]]),
            ],
            "expected": [7, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()

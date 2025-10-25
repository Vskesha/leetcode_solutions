import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j, pi, pj, time) -> bool:
            critic = False
            grid[i][j] = time
            for ni, nj in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
                if (
                    ni < 0
                    or nj < 0
                    or ni >= m
                    or nj >= n
                    or grid[ni][nj] == 0
                    or (ni == pi and nj == pj)
                ):
                    continue
                if grid[ni][nj] == 1:
                    if dfs(ni, nj, i, j, time + 1):
                        critic = True
                    if grid[ni][nj] > time:
                        critic = True
                    if grid[ni][nj] == time and pi != -1:
                        critic = True
                grid[i][j] = min(grid[i][j], grid[ni][nj])
            return critic

        cells = sum(sum(row) for row in grid)
        if cells < 2:
            return cells

        islands_explored = 0
        has_critical = False

        for r in range(m):
            for c in range(n):
                if grid[r][c] != 1:
                    continue
                if islands_explored:
                    return 0
                has_critical = dfs(r, c, -1, -1, 2)
                islands_explored += 1

        return 2 - int(has_critical and cells != 2)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minDays"] * 6,
            "kwargs": [
                dict(grid=[[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]),
                dict(grid=[[1, 1]]),
                dict(
                    grid=[
                        [1, 1, 0, 1, 1],
                        [1, 1, 1, 1, 1],
                        [1, 1, 0, 1, 1],
                        [1, 1, 0, 1, 1],
                    ]
                ),
                dict(grid=[[1, 0, 1, 0]]),
                dict(
                    grid=[
                        [1, 1, 0, 1, 1],
                        [1, 1, 1, 1, 1],
                        [1, 1, 0, 1, 1],
                        [1, 1, 1, 1, 1],
                    ]
                ),
                dict(grid=[[0, 1, 1], [1, 1, 1], [1, 1, 0]]),
            ],
            "expected": [2, 2, 1, 0, 2, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

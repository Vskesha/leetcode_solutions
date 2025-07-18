import unittest
from collections import deque
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def bfs(i, j):
            if not grid[i][j]:
                return
            grid[i][j] = 0
            que = deque([(i, j)])
            while que:
                i, j = que.popleft()
                for ni, nj in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj]:
                        grid[ni][nj] = 0
                        que.append((ni, nj))

        for i in range(m):
            bfs(i, 0)
            bfs(i, n - 1)

        for j in range(n):
            bfs(0, j)
            bfs(m - 1, j)

        return sum(sum(row) for row in grid)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["numEnclaves"] * 2,
            "kwargs": [
                dict(grid=[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]),
                dict(grid=[[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]),
            ],
            "expected": [3, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

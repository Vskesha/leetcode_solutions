import unittest
from collections import deque
from typing import List

from _test_meta import TestMeta


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 0
            res = grid[i][j]
            grid[i][j] = 0
            for ni, nj in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
                res += dfs(ni, nj)
            return res

        return max(dfs(i, j) for i in range(m) for j in range(n))


class Solution2:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    bfs = deque([(r, c)])
                    res = 0
                    while bfs:
                        cr, cc = bfs.popleft()
                        res += grid[cr][cc]
                        grid[cr][cc] = 0
                        for nr, nc in (
                            (cr, cc + 1),
                            (cr + 1, cc),
                            (cr, cc - 1),
                            (cr - 1, cc),
                        ):
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc]:
                                bfs.append((nr, nc))
                    ans = max(ans, res)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findMaxFish"] * 2,
            "kwargs": [
                dict(
                    grid=[
                        [0, 2, 1, 0],
                        [4, 0, 0, 3],
                        [1, 0, 0, 4],
                        [0, 3, 2, 0],
                    ]
                ),
                dict(
                    grid=[
                        [1, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 1],
                    ]
                ),
            ],
            "expected": [7, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

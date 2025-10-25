import unittest
from collections import deque
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = [[0] * n for _ in range(n)]
        if all(v for row in grid for v in row):
            return n * n

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs = deque()
                    bfs.append((i, j))
                    grid[i][j] = 2
                    coast = set()
                    size = 0
                    while bfs:
                        ci, cj = bfs.popleft()
                        for ni, nj in (
                            (ci, cj + 1),
                            (ci + 1, cj),
                            (ci, cj - 1),
                            (ci - 1, cj),
                        ):
                            if 0 <= ni < n and 0 <= nj < n:
                                if grid[ni][nj] == 1:
                                    grid[ni][nj] = 2
                                    bfs.append((ni, nj))
                                elif grid[ni][nj] == 0:
                                    coast.add((ni, nj))
                        size += 1
                    for ci, cj in coast:
                        res[ci][cj] += size

        return max(max(row) for row in res) + 1


class Solution2:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ii = 2
        sizes = {}
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs = deque()
                    bfs.append((i, j))
                    grid[i][j] = ii
                    size = 0
                    while bfs:
                        ci, cj = bfs.popleft()
                        for di, dj in dirs:
                            ni, nj = ci + di, cj + dj
                            if (
                                0 <= ni < n
                                and 0 <= nj < n
                                and grid[ni][nj] == 1
                            ):
                                grid[ni][nj] = ii
                                bfs.append((ni, nj))
                        size += 1
                    sizes[ii] = size
                    ii += 1

        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    continue
                neibs = set()
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj]:
                        neibs.add(grid[ni][nj])
                res = sum(sizes[ii] for ii in neibs) + 1
                ans = max(ans, res)

        return ans or n * n


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["largestIsland"] * 3,
            "kwargs": [
                dict(grid=[[1, 0], [0, 1]]),
                dict(grid=[[1, 1], [1, 0]]),
                dict(grid=[[1, 1], [1, 1]]),
            ],
            "expected": [3, 4, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()

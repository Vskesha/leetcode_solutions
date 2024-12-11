import unittest
from collections import deque
from heapq import heappop, heappush
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        obs = [[-1] * n for _ in range(m)]
        obs[0][0] = grid[0][0]
        bfs = deque([(grid[0][0], 0, 0)])

        while bfs:
            ob, i, j = bfs.popleft()
            if i == m - 1 and j == n - 1:
                return ob
            for ni, nj in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                if 0 <= ni < m and 0 <= nj < n:
                    if obs[ni][nj] == -1:
                        if grid[ni][nj]:
                            bfs.append((ob + 1, ni, nj))
                        else:
                            bfs.appendleft((ob, ni, nj))
                        obs[ni][nj] = ob + grid[ni][nj]

        return obs[-1][-1]


class Solution2:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        visited = [[inf] * n for _ in range(m)]
        visited[0][0] = grid[0][0]
        while heap:
            obs, i, j = heappop(heap)
            if i == m - 1 and j == n - 1:
                return obs
            for ni, nj in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                if 0 <= ni < m and 0 <= nj < n:
                    nobs = obs + grid[ni][nj]
                    if nobs < visited[ni][nj]:
                        visited[ni][nj] = nobs
                        heappush(heap, (nobs, ni, nj))
        return -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimumObstacles"] * 2,
            "kwargs": [
                dict(grid=[[0, 1, 1], [1, 1, 0], [1, 1, 0]]),
                dict(grid=[[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]),
            ],
            "expected": [2, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

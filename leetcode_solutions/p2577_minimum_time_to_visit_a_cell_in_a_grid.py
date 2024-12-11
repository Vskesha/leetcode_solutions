import unittest
from heapq import heappop, heappush
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][0] < grid[0][1] - 1 and grid[0][0] < grid[1][0] - 1:
            return -1
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        heap = [(0, 0, 0)]
        while heap:
            t, i, j = heappop(heap)
            if i == m - 1 and j == n - 1:
                return t
            t += 1
            for ni, nj in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                if 0 <= ni < m and 0 <= nj < n:
                    if not visited[ni][nj]:
                        visited[ni][nj] = True
                        if grid[ni][nj] > t:
                            d = (grid[ni][nj] - t) % 2
                            heappush(heap, (grid[ni][nj] + d, ni, nj))
                        else:
                            heappush(heap, (t, ni, nj))

        return -1


class Solution2:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][0] < grid[0][1] - 1 and grid[0][0] < grid[1][0] - 1:
            return -1
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        heap = [(0, 0, 0)]
        while heap:
            t, i, j = heappop(heap)
            if i == m - 1 and j == n - 1:
                return t
            t += 1
            for ni, nj in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                if 0 <= ni < m and 0 <= nj < n:
                    if not visited[ni][nj]:
                        grid[ni][nj] += (grid[ni][nj] & 1) ^ ((ni + nj) & 1)
                        visited[ni][nj] = True
                        heappush(heap, (max(grid[ni][nj], t), ni, nj))
        return -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimumTime"] * 2,
            "kwargs": [
                dict(grid=[[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]),
                dict(grid=[[0, 2, 4], [3, 2, 1], [1, 0, 4]]),
            ],
            "expected": [7, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

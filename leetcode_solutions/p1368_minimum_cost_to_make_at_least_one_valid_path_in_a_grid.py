import unittest
from collections import deque
from heapq import heappop, heappush
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
        dp = [[m + n] * n for _ in range(m)]
        dp[0][0] = 0
        queue = deque([(0, 0)])

        while queue:
            i, j = queue.popleft()
            if i == m - 1 and j == n - 1:
                return dp[i][j]
            ch = dp[i][j]
            dr = grid[i][j]
            di, dj = dirs[dr]
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and dp[ni][nj] > ch:
                dp[ni][nj] = ch
                queue.appendleft((ni, nj))
            ch += 1
            for ndr in range(dr + 1, dr + 4):
                ndr = (ndr - 1) % 4 + 1
                di, dj = dirs[ndr]
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and dp[ni][nj] > ch:
                    dp[ni][nj] = ch
                    queue.append((ni, nj))

        return dp[-1][-1]


class Solution2:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        dp = [[m + n] * n for _ in range(m)]
        dp[0][0] = 0
        queue = deque()
        queue.append((0, 0))

        while queue:
            i, j = queue.popleft()
            if i == m - 1 and j == n - 1:
                return dp[i][j]
            dr = grid[i][j]
            for ndr in range(dr, dr + 4):
                ndr = (ndr - 1) % 4 + 1
                di, dj = dirs[ndr]
                ni, nj = i + di, j + dj
                ch = dp[i][j] + (ndr != dr)
                if 0 <= ni < m and 0 <= nj < n and dp[ni][nj] > ch:
                    dp[ni][nj] = ch
                    if dr == ndr:
                        queue.appendleft((ni, nj))
                    else:
                        queue.append((ni, nj))

        return dp[-1][-1]


class Solution3:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        dp = [[m + n] * n for _ in range(m)]
        dp[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            _, i, j = heappop(heap)
            if i == m - 1 and j == n - 1:
                return dp[i][j]
            dr = grid[i][j]
            for ndr in range(dr, dr + 4):
                ndr = (ndr - 1) % 4 + 1
                di, dj = dirs[ndr]
                ni, nj = i + di, j + dj
                ch = dp[i][j] + (ndr != dr)
                if 0 <= ni < m and 0 <= nj < n and dp[ni][nj] > ch:
                    dp[ni][nj] = ch
                    heappush(heap, (ch, ni, nj))

        return dp[-1][-1]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minCost"] * 3,
            "kwargs": [
                dict(
                    grid=[
                        [1, 1, 1, 1],
                        [2, 2, 2, 2],
                        [1, 1, 1, 1],
                        [2, 2, 2, 2],
                    ]
                ),
                dict(grid=[[1, 1, 3], [3, 2, 2], [1, 1, 4]]),
                dict(grid=[[1, 2], [4, 3]]),
            ],
            "expected": [3, 0, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

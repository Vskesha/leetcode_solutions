import unittest
from heapq import heappop, heappush
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        heap = [(0, 0, 0, 1)]
        visited = [[False] * n for _ in range(m)]
        while heap:
            t, i, j, dt = heappop(heap)
            if i == m - 1 and j == n - 1:
                return t
            ndt = 3 - dt
            for ni, nj in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                if 0 <= ni < m and 0 <= nj < n:
                    if not visited[ni][nj]:
                        visited[ni][nj] = True
                        ct = max(t, moveTime[ni][nj]) + dt
                        heappush(heap, (ct, ni, nj, ndt))
        return -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minTimeToReach"] * 3,
            "kwargs": [
                dict(moveTime=[[0, 4], [4, 4]]),
                dict(moveTime=[[0, 0, 0, 0], [0, 0, 0, 0]]),
                dict(moveTime=[[0, 1], [1, 2]]),
            ],
            "expected": [7, 6, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()

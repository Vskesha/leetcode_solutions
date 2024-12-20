import unittest
from heapq import heappop, heappush
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        heap = [(0, 0, 0)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        while heap:
            t, i, j = heappop(heap)
            if i == m - 1 and j == n - 1:
                return t
            for ni, nj in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                if 0 <= ni < m and 0 <= nj < n:
                    if not visited[ni][nj]:
                        visited[ni][nj] = True
                        nt = max(t, moveTime[ni][nj]) + 1
                        heappush(heap, (nt, ni, nj))

        return -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minTimeToReach"] * 3,
            "kwargs": [
                dict(moveTime=[[0, 4], [4, 4]]),
                dict(moveTime=[[0, 0, 0], [0, 0, 0]]),
                dict(moveTime=[[0, 1], [1, 2]]),
            ],
            "expected": [6, 3, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()

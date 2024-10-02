import unittest
from heapq import heappop, heappush
from itertools import pairwise
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dij = [[inf] * n for _ in range(m)]
        dij[0][0] = grid[0][0]
        heap = [(grid[0][0], 0, 0)]
        dirs = (0, 1, 0, -1, 0)

        while heap:
            d, i, j = heappop(heap)
            if d == health:
                return False
            if i == m - 1 and j == n - 1:
                return True
            for di, dj in pairwise(dirs):
                di, dj = di + i, dj + j
                if 0 <= di < m and 0 <= dj < n:
                    nd = d + grid[di][dj]
                    if nd < dij[di][dj]:
                        dij[di][dj] = nd
                        heappush(heap, (nd, di, dj))

        return False


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findSafeWalk"] * 3,
            "kwargs": [
                dict(
                    grid=[[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], health=1
                ),
                dict(
                    grid=[
                        [0, 1, 1, 0, 0, 0],
                        [1, 0, 1, 0, 0, 0],
                        [0, 1, 1, 1, 0, 1],
                        [0, 0, 1, 0, 1, 0],
                    ],
                    health=3,
                ),
                dict(grid=[[1, 1, 1], [1, 0, 1], [1, 1, 1]], health=5),
            ],
            "expected": [True, False, True],
        },
    ]


if __name__ == "__main__":
    unittest.main()

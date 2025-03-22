import unittest
from heapq import heappop, heappush
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]
        heap = []
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    height[i][j] = 0
                    heappush(heap, (0, i, j))

        while heap:
            h, i, j = heappop(heap)
            h += 1
            for ni, nj in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
                if 0 <= ni < m and 0 <= nj < n and height[ni][nj] == -1:
                    height[ni][nj] = h
                    heappush(heap, (h, ni, nj))

        return height

class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["highestPeak"] * 2,
            "kwargs": [
                dict(isWater = [[0,1],[0,0]]),
                dict(isWater = [[0,0,1],[1,0,0],[0,0,0]]),
            ],
            "expected": [[[1,0],[2,1]],
                         [[1,1,0],[0,1,1],[1,2,2]]],
            "assert_methods": ["assertHighestPeak"] * 2,
        },
    ]

    def assertHighestPeak(self, expected: List[List[int]], actual: List[List[int]]):
        me, ne = len(expected), len(expected[0])
        ma, na = len(actual), len(actual[0])

        self.assertEqual(me, ma)
        self.assertEqual(ne, na)

        maxe = max(expected[i][j] for i in range(me) for j in range(ne))
        maxa = max(actual[i][j] for i in range(ma) for j in range(na))
        self.assertEqual(maxe, maxa)

        for i in range(1, me):
            self.assertLessEqual(abs(expected[i][0] - expected[i - 1][0]), 1)
            self.assertLessEqual(abs(actual[i][0] - actual[i - 1][0]), 1)

        for j in range(1, ne):
            self.assertLessEqual(abs(expected[0][j] - expected[0][j - 1]), 1)
            self.assertLessEqual(abs(actual[0][j] - actual[0][j - 1]), 1)

        for i in range(1, me):
            for j in range(1, ne):
                self.assertLessEqual(abs(expected[i][j] - expected[i][j - 1]), 1)
                self.assertLessEqual(abs(expected[i][j] - expected[i - 1][j]), 1)
                self.assertLessEqual(abs(actual[i][j] - actual[i][j - 1]), 1)
                self.assertLessEqual(abs(actual[i][j] - actual[i - 1][j]), 1)


if __name__ == "__main__":
    unittest.main()

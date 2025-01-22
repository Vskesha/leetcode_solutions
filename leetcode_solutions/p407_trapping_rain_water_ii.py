import unittest
from heapq import heappush, heappop
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        ans = 0

        for i in range(m):
            heappush(heap, (heightMap[i][0], i, 0))
            heappush(heap, (heightMap[i][n - 1], i, n - 1))
            visited[i][0] = True
            visited[i][n - 1] = True
        for j in range(1, n - 1):
            heappush(heap, (heightMap[0][j], 0, j))
            heappush(heap, (heightMap[m - 1][j], m - 1, j))
            visited[0][j] = True
            visited[m - 1][j] = True

        while heap:
            h, i, j = heappop(heap)
            for ni, nj in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
                if 0 <= ni < m and 0 <= nj < n:
                    if not visited[ni][nj]:
                        visited[ni][nj] = True
                        nh = heightMap[ni][nj]
                        if nh < h:
                            ans += h - nh
                            heappush(heap, (h, ni, nj))
                        else:
                            heappush(heap, (nh, ni, nj))

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["trapRainWater"] * 2,
            "kwargs": [
                dict(
                    heightMap=[
                        [1, 4, 3, 1, 3, 2],
                        [3, 2, 1, 3, 2, 4],
                        [2, 3, 3, 2, 3, 1],
                    ]
                ),
                dict(
                    heightMap=[
                        [3, 3, 3, 3, 3],
                        [3, 2, 2, 2, 3],
                        [3, 2, 1, 2, 3],
                        [3, 2, 2, 2, 3],
                        [3, 3, 3, 3, 3],
                    ]
                ),
            ],
            "expected": [4, 10],
        },
    ]


if __name__ == "__main__":
    unittest.main()

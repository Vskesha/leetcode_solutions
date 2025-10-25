import unittest
from collections import deque
from itertools import pairwise
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = (-1, 0, 1, 0, -1)

        def find_cells(bfs, ocean):
            while bfs:
                i, j = bfs.popleft()
                for di, dj in pairwise(directions):
                    ni, nj = i + di, j + dj
                    if (
                        0 <= ni < m
                        and 0 <= nj < n
                        and not ocean[ni][nj]
                        and heights[ni][nj] >= heights[i][j]
                    ):
                        ocean[ni][nj] = 1
                        bfs.append((ni, nj))

        bfs = deque()
        pacific = [[0] * n for _ in range(m)]
        for i in range(0, m):
            pacific[i][0] = 1
            bfs.append((i, 0))
        for j in range(1, n):
            pacific[0][j] = 1
            bfs.append((0, j))
        find_cells(bfs, pacific)

        atlantic = [[0] * n for _ in range(m)]
        for i in range(0, m):
            atlantic[i][n - 1] = 1
            bfs.append((i, n - 1))
        for j in range(0, n - 1):
            atlantic[m - 1][j] = 1
            bfs.append((m - 1, j))
        find_cells(bfs, atlantic)

        result = []
        for i in range(m):
            for j in range(n):
                if atlantic[i][j] and pacific[i][j]:
                    result.append([i, j])

        return result


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["pacificAtlantic"] * 4,
            "kwargs": [
                dict(heights=[[2, 1], [1, 2]]),
                dict(
                    heights=[
                        [1, 2, 2, 3, 5],
                        [3, 2, 3, 4, 4],
                        [2, 4, 5, 3, 1],
                        [6, 7, 1, 4, 5],
                        [5, 1, 1, 2, 4],
                    ]
                ),
                dict(heights=[[1]]),
                dict(heights=[[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
            ],
            "expected": [
                [[0, 0], [0, 1], [1, 0], [1, 1]],
                [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
                [[0, 0]],
                [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],
            ],
            "assert_methods": ["assertNestedListEqual"] * 4,
        },
    ]

    def assertNestedListEqual(self, actual, expected):
        self.assertEqual(len(actual), len(expected))
        for lst1, lst2 in zip(actual, expected):
            self.assertListEqual(lst1, lst2)


if __name__ == "__main__":
    unittest.main()

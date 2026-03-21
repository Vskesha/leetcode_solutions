import unittest
from itertools import pairwise
from math import inf
from typing import List

from sortedcontainers import SortedList

from leetcode_solutions._test_meta import TestMeta


# fmt: off
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        return [[min((b - a for a, b in pairwise(sorted(set(grid[ii][jj] for ii in range(i, i + k) for jj in range(j, j + k))))), default=0) for j in range(len(grid[0]) - k + 1)] for i in range(len(grid) - k + 1)]  # noqa: E501
# fmt: on


class Solution2:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = []

        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                values = set(
                    grid[ii][jj]
                    for ii in range(i, i + k)
                    for jj in range(j, j + k)
                )
                row.append(
                    min(
                        (b - a for a, b in pairwise(sorted(values))), default=0
                    )
                )
            ans.append(row)

        return ans


class Solution3:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        if k == 1:
            return [[0] * n for _ in range(m)]

        smv = SortedList(
            grid[i][j] for i in range(k - 1) for j in range(k - 1)
        )
        ans = []

        for i in range(m - k + 1):
            row = []
            smv.update(grid[i + k - 1][jj] for jj in range(k - 1))
            csmv = smv.copy()
            for j in range(n - k + 1):
                csmv.update(grid[ii][j + k - 1] for ii in range(i, i + k))
                prev = csmv[0]
                min_diff = inf
                for val in csmv:
                    if val != prev and (diff := val - prev) < min_diff:
                        min_diff = diff
                    prev = val
                if min_diff == inf:
                    min_diff = 0
                row.append(min_diff)
                for ii in range(i, i + k):
                    csmv.remove(grid[ii][j])
            for jj in range(k - 1):
                smv.remove(grid[i][jj])
            ans.append(row)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minAbsDiff"] * 3,
            "kwargs": [
                dict(grid=[[1, 8], [3, -2]], k=2),
                dict(grid=[[3, -1]], k=1),
                dict(grid=[[1, -2, 3], [2, 3, 5]], k=2),
            ],
            "expected": [[[2]], [[0, 0]], [[1, 2]]],
            "assert_methods": ["assertMatrixEqual"] * 3,
        },
    ]

    def assertMatrixEqual(
        self, actual: List[List[int]], expected: List[List[int]]
    ):
        self.assertEqual(len(actual), len(expected))
        for a, b in zip(actual, expected):
            self.assertListEqual(a, b)


if __name__ == "__main__":
    unittest.main()

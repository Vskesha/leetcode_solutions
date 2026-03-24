import unittest
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        m, n = len(grid), len(grid[0])

        ans = [[0] * n for _ in range(m)]
        ps = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                ans[i][j] = ps
                ps = ps * grid[i][j] % mod

        ps = 1
        for i in range(m):
            for j in range(n):
                ans[i][j] = ans[i][j] * ps % mod
                ps = ps * grid[i][j] % mod

        return ans


class Solution2:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        mod = 12345

        pref = [[0] * n for _ in range(m)]
        ps = 1
        for i in range(m):
            for j in range(n):
                pref[i][j] = ps
                ps = (ps * grid[i][j]) % mod

        suff = [[0] * n for _ in range(m)]
        ps = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                suff[i][j] = ps
                ps = (ps * grid[i][j]) % mod

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = pref[i][j] * suff[i][j] % mod

        return ans


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["constructProductMatrix"] * 2,
            "kwargs": [
                dict(grid=[[1, 2], [3, 4]]),
                dict(grid=[[12345], [2], [1]]),
            ],
            "expected": [[[24, 12], [8, 6]], [[2], [0], [0]]],
            "assert_methods": ["assertMatrixEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

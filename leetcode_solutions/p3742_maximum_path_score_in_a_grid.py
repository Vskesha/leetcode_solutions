import unittest
from functools import cache
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        dp = [dict() for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(m):
            for j in range(n):
                for at, sc in dp[j - 1].items():
                    dp[j][at] = max(dp[j].get(at, -1), sc)
                if grid[i][j]:
                    dp[j] = {
                        cost + 1: score + grid[i][j]
                        for cost, score in dp[j].items()
                        if cost < k
                    }

        ans = max(dp[n - 1].values(), default=-1)
        return ans


class Solution2:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dp(i, j, at):
            if i < 0 or j < 0 or at < 0:
                return -1

            if i == 0 and j == 0:
                if bool(grid[0][0]) > at:
                    return -1
                return grid[0][0]

            res_top = dp(i - 1, j, at - bool(grid[i][j]))
            res_lft = dp(i, j - 1, at - bool(grid[i][j]))

            res = max(res_top, res_lft)
            return res + grid[i][j] if res > -1 else -1

        ans = dp(m - 1, n - 1, k)
        return ans


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxPathScore"] * 3,
            "kwargs": [
                dict(grid=[[0, 2, 2], [1, 1, 1], [0, 0, 2]], k=3),
                dict(grid=[[0, 1], [2, 0]], k=1),
                dict(grid=[[0, 1], [1, 2]], k=1),
            ],
            "expected": [5, 2, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

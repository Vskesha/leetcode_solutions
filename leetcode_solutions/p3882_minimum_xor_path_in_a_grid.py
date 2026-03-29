import unittest

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = []
        prev = 0

        for val in grid[0]:
            prev ^= val
            dp.append({prev})

        for i in range(1, m):
            ndp = [{grid[i][0] ^ num for num in dp[0]}]
            for j in range(1, n):
                ndp.append({grid[i][j] ^ num for num in (dp[j] | ndp[-1])})
            dp = ndp
        return min(dp[-1])


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minCost"] * 3,
            "kwargs": [
                dict(grid=[[1, 2], [3, 4]]),
                dict(grid=[[6, 7], [5, 8]]),
                dict(grid=[[2, 7, 5]]),
            ],
            "expected": [6, 9, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

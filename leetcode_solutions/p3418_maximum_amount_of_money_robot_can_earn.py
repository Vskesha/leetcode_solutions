import unittest
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        dp = [[-inf] * 3 for _ in range(n + 1)]
        dp[0] = [0, -inf, -inf]

        for i in range(m):
            ndp = [[-inf] * 3 for _ in range(n + 1)]
            for j in range(n):
                for k in range(3):
                    ndp[j][k] = max(ndp[j - 1][k], dp[j][k]) + coins[i][j]
                if coins[i][j] < 0:
                    for k in range(1, 3):
                        ndp[j][k] = max(
                            ndp[j][k], ndp[j - 1][k - 1], dp[j][k - 1]
                        )
            dp = ndp

        return max(dp[n - 1])


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumAmount"] * 2,
            "kwargs": [
                dict(coins=[[0, 1, -1], [1, -2, 3], [2, -3, 4]]),
                dict(coins=[[10, 10, 10], [10, 10, 10]]),
            ],
            "expected": [8, 40],
        },
    ]


if __name__ == "__main__":
    unittest.main()

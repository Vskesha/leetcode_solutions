import unittest

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7

        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        for i in range(zero + 1):
            for j in range(one + 1):
                for lastBit in range(2):
                    if i == 0:
                        if lastBit == 0 or j > limit:
                            dp[i][j][lastBit] = 0
                        else:
                            dp[i][j][lastBit] = 1
                    elif j == 0:
                        if lastBit == 1 or i > limit:
                            dp[i][j][lastBit] = 0
                        else:
                            dp[i][j][lastBit] = 1
                    elif lastBit == 0:
                        dp[i][j][lastBit] = dp[i - 1][j][0] + dp[i - 1][j][1]
                        if i > limit:
                            dp[i][j][lastBit] -= dp[i - limit - 1][j][1]
                    else:
                        dp[i][j][lastBit] = dp[i][j - 1][0] + dp[i][j - 1][1]
                        if j > limit:
                            dp[i][j][lastBit] -= dp[i][j - limit - 1][0]
                    dp[i][j][lastBit] %= mod
        return (dp[-1][-1][0] + dp[-1][-1][1]) % mod


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["numberOfStableArrays"] * 3,
            "kwargs": [
                dict(zero=1, one=1, limit=2),
                dict(zero=1, one=2, limit=1),
                dict(zero=3, one=3, limit=2),
            ],
            "expected": [2, 1, 14],
        },
    ]


if __name__ == "__main__":
    unittest.main()

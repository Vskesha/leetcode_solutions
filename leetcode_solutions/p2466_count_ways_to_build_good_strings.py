import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1

        for i in range(high + 1):
            if i >= zero:
                dp[i] = dp[i - zero]
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % mod

        ans = 0
        for i in range(low, high + 1):
            ans = (ans + dp[i]) % mod

        return ans


class Solution1:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        if one < zero:
            one, zero = zero, one
        for ln in range(zero, one):
            dp[ln] = dp[ln - zero]
        for ln in range(one, low):
            dp[ln] = (dp[ln - zero] + dp[ln - one]) % mod
        ans = 0
        for ln in range(low, high + 1):
            dp[ln] = (dp[ln - zero] + dp[ln - one]) % mod
            ans = (ans + dp[ln]) % mod
        return ans


class Solution2:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        for e in range(1, high + 1):
            if e >= zero:
                dp[e] += dp[e - zero]
            if e >= one:
                dp[e] += dp[e - one]
            dp[e] %= mod

        return sum(dp[low:]) % mod

class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countGoodStrings"] * 2,
            "kwargs": [
                dict(low = 3, high = 3, zero = 1, one = 1),
                dict(low = 2, high = 3, zero = 1, one = 2),
            ],
            "expected": [8, 5],
        },
    ]


if __name__ == "__main__":
    unittest.main()

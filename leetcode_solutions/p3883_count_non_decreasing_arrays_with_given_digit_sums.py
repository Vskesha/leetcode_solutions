import unittest
from functools import cache

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    mod = 10**9 + 7
    dsum = [0] * 5001
    for num in range(5001):
        dsum[num] = dsum[num // 10] + num % 10

    def countArrays(self, digitSum: list[int]) -> int:
        n = len(digitSum)

        dp = [1] * 5002

        for i in range(n - 1, -1, -1):
            ndp = [0] * 5002
            for num in range(5000, -1, -1):
                if self.dsum[num] == digitSum[i]:
                    ndp[num] = (ndp[num + 1] + dp[num]) % self.mod
                else:
                    ndp[num] = ndp[num + 1]
            dp = ndp

        return dp[0]


# TLE
class Solution3:
    def countArrays(self, digitSum: list[int]) -> int:
        mod = 10**9 + 7
        n = len(digitSum)
        dsum = [0] * 5001

        for num in range(5001):
            dsum[num] = dsum[num // 10] + num % 10

        @cache
        def dp(idx, num):
            if idx == n:
                return 1
            if num > 5000:
                return 0

            res = 0
            if dsum[num] == digitSum[idx]:
                res = (res + dp(idx + 1, num)) % mod

            res = (res + dp(idx, num + 1)) % mod

            return res

        return dp(0, 0)


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countArrays"] * 3,
            "kwargs": [
                dict(digitSum=[25, 1]),
                dict(digitSum=[1]),
                dict(digitSum=[2, 49, 23]),
            ],
            "expected": [6, 4, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

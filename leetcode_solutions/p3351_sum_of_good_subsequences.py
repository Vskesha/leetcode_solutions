import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        mxn = max(nums) + 2
        cnts = [0] * mxn
        sums = [0] * mxn

        for n in nums:
            ncnt = cnts[n - 1] + cnts[n + 1] + 1
            sums[n] = (sums[n] + sums[n - 1] + sums[n + 1] + ncnt * n) % mod
            cnts[n] = (cnts[n] + ncnt) % mod

        return sum(sums) % mod


class Solution2:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        dp = {}
        ans = 0

        for n in nums:
            lc, ls = dp.get(n - 1, (0, 0))
            bc, bs = dp.get(n + 1, (0, 0))
            nc, ns = dp.get(n, (0, 0))
            cc = lc + bc + 1
            cs = ls + bs + cc * n
            ans = (ans + cs) % mod
            dp[n] = (nc + cc, ns + cs)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["sumOfGoodSubsequences"] * 2,
            "kwargs": [
                dict(nums=[1, 2, 1]),
                dict(nums=[3, 4, 5]),
            ],
            "expected": [14, 40],
        },
    ]


if __name__ == "__main__":
    unittest.main()

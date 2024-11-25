import unittest
from functools import cache
from math import gcd
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        ln = len(nums)

        @cache
        def dp(i, g1, g2):
            if i >= ln:
                return int(g1 == g2 and g1 != 0)
            n = nums[i]
            ans = dp(i + 1, g1, g2)
            ans = (ans + dp(i + 1, gcd(g1, n) if g1 else n, g2)) % mod
            ans = (ans + dp(i + 1, g1, gcd(g2, n) if g2 else n)) % mod
            return ans

        return dp(0, 0, 0)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["subsequencePairCount"] * 3,
            "kwargs": [
                dict(nums=[1, 2, 3, 4]),
                dict(nums=[10, 20, 30]),
                dict(nums=[1, 1, 1, 1]),
            ],
            "expected": [10, 2, 50],
        },
    ]


if __name__ == "__main__":
    unittest.main()

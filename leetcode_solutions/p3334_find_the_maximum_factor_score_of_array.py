import unittest
from itertools import accumulate
from math import gcd, lcm
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        pref_gcd = list(accumulate(nums, gcd))
        pref_lcm = list(accumulate(nums, lcm))
        suff_gcd = list(accumulate(reversed(nums), gcd))
        suff_lcm = list(accumulate(reversed(nums), lcm))
        ln = len(nums)
        ans = pref_gcd[-1] * pref_lcm[-1]
        if ln == 1:
            return ans

        ans = max(ans, pref_gcd[-2] * pref_lcm[-2])
        ans = max(ans, suff_gcd[-2] * suff_lcm[-2])
        for i in range(ln - 2):
            cgcd = gcd(pref_gcd[i], suff_gcd[-i - 3])
            clcm = lcm(pref_lcm[i], suff_lcm[-i - 3])
            ans = max(ans, cgcd * clcm)

        return ans


class Solution2:
    def maxScore(self, nums: List[int]) -> int:
        ans = gcd(*nums) * lcm(*nums)
        for i in range(len(nums)):
            wn = [nums[j] for j in range(len(nums)) if j != i]
            ans = max(ans, gcd(*wn) * lcm(*wn))
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxScore"] * 5,
            "kwargs": [
                dict(nums=[6, 20, 1, 18]),
                dict(nums=[12, 1, 16]),
                dict(nums=[2, 4, 8, 16]),
                dict(nums=[1, 2, 3, 4, 5]),
                dict(nums=[3]),
            ],
            "expected": [360, 192, 64, 60, 9],
        },
    ]


if __name__ == "__main__":
    unittest.main()

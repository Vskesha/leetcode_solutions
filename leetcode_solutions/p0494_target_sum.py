import unittest
from collections import defaultdict
from functools import cache
from itertools import accumulate
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        left = list(accumulate(nums[::-1], initial=0))[::-1]
        dp = defaultdict(int)
        dp[0] = 1

        for n, lft in zip(nums, left):
            ndp = defaultdict(int)
            for sm, cnt in dp.items():
                if sm <= target + lft:
                    ndp[sm + n] += cnt
                if sm >= target - lft:
                    ndp[sm - n] += cnt
            dp = ndp

        return dp[target]


class Solution1:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @cache
        def dp(i, s):
            if s > target + left[i] or s < target - left[i]:
                return 0
            if i == ln:
                return int(s == target)
            res1 = dp(i + 1, s - nums[i])
            res2 = dp(i + 1, s + nums[i])
            res = res1 + res2
            return res

        left = list(accumulate(nums[::-1], initial=0))[::-1]
        ln = len(nums)
        ans = dp(0, 0)
        return ans


class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for n in nums:
            ndp = defaultdict(int)
            for sm, cnt in dp.items():
                ndp[sm + n] += cnt
                ndp[sm - n] += cnt
            dp = ndp

        return dp[target]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findTargetSumWays"] * 2,
            "kwargs": [
                dict(nums=[1, 1, 1, 1, 1], target=3),
                dict(nums=[1], target=1),
            ],
            "expected": [5, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

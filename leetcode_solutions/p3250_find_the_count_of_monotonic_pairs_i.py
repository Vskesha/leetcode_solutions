import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        dp = [1] * (nums[0] + 1)

        for i in range(1, n):
            ndp = [0] * (nums[i] + 1)
            diff = max(0, nums[i] - nums[i - 1])
            for inc in range(diff, nums[i] + 1):
                ndp[inc] = sum(dp[: (inc - diff + 1)]) % mod
            dp = ndp

        return sum(dp) % mod


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countOfPairs"] * 2,
            "kwargs": [
                dict(nums=[2, 3, 2]),
                dict(nums=[5, 5, 5, 5]),
            ],
            "expected": [4, 126],
        },
    ]


if __name__ == "__main__":
    unittest.main()

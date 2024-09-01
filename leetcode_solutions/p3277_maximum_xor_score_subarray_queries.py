import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maximumSubarrayXor(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        ln = len(nums)
        dp = [[0] * ln for _ in range(ln)]
        mx = [[0] * ln for _ in range(ln)]
        for i in range(ln):
            dp[i][i] = mx[i][i] = nums[i]

        for d in range(1, ln):
            for i, j in zip(range(ln), range(d, ln)):
                dp[i][j] = dp[i + 1][j] ^ dp[i][j - 1]
                mx[i][j] = max(dp[i][j], mx[i + 1][j], mx[i][j - 1])

        return [mx[i][j] for i, j in queries]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumSubarrayXor"] * 2,
            "kwargs": [
                dict(nums=[2, 8, 4, 32, 16, 1], queries=[[0, 2], [1, 4], [0, 5]]),
                dict(
                    nums=[0, 7, 3, 2, 8, 5, 1],
                    queries=[[0, 3], [1, 5], [2, 4], [2, 6], [5, 6]],
                ),
            ],
            "expected": [[12, 60, 60], [7, 14, 11, 14, 5]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

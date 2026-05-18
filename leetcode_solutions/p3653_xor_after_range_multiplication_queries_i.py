import unittest
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    MOD = 10**9 + 7

    def xorAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> int:
        for left, right, k, v in queries:
            for i in range(left, right + 1, k):
                nums[i] = (nums[i] * v) % self.MOD

        res = 0
        for x in nums:
            res ^= x

        return res


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["xorAfterQueries"] * 2,
            "kwargs": [
                dict(nums=[1, 1, 1], queries=[[0, 2, 1, 4]]),
                dict(
                    nums=[2, 3, 1, 5, 4], queries=[[1, 4, 2, 3], [0, 2, 1, 2]]
                ),
            ],
            "expected": [4, 31],
        },
    ]


if __name__ == "__main__":
    unittest.main()

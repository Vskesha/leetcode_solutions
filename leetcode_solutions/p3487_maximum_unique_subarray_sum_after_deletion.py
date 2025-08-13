import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if all(n < 0 for n in nums):
            return max(nums)
        return sum(set(n for n in nums if n >= 0))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxSum"] * 3,
            "kwargs": [
                dict(nums=[1, 2, 3, 4, 5]),
                dict(nums=[1, 1, 0, 1, 1]),
                dict(nums=[1, 2, -1, -2, 1, 0, -1]),
            ],
            "expected": [15, 1, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()

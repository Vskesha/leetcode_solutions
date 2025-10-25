import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        return sum(
            (nums[i - 2] + nums[i]) * 2 == nums[i - 1]
            for i in range(2, len(nums))
        )


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countSubarrays"] * 2,
            "kwargs": [
                dict(nums=[1, 2, 1, 4, 1]),
                dict(nums=[1, 1, 1]),
            ],
            "expected": [1, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

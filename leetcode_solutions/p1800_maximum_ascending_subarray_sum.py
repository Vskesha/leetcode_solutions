import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = asc_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                asc_sum += nums[i]
            else:
                ans = max(ans, asc_sum)
                asc_sum = nums[i]
        ans = max(ans, asc_sum)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxAscendingSum"] * 3,
            "kwargs": [
                dict(nums=[10, 20, 30, 5, 10, 50]),
                dict(nums=[10, 20, 30, 40, 50]),
                dict(nums=[12, 17, 15, 13, 10, 11, 12]),
            ],
            "expected": [65, 150, 33],
        },
    ]


if __name__ == "__main__":
    unittest.main()

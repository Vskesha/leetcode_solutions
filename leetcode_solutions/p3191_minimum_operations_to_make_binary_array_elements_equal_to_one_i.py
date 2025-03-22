import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                ans += 1
        if nums[-1] == 0 or nums[-2] == 0:
            return -1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minOperations"] * 2,
            "kwargs": [
                dict(nums=[0, 1, 1, 1, 0, 0]),
                dict(nums=[0, 1, 1, 1]),
            ],
            "expected": [3, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

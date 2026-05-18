import unittest
from bisect import bisect_left
from itertools import accumulate
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        maxes = list(accumulate(nums, max))
        # mins = list(reversed(accumulate(reversed(nums), min)))
        mins = nums.copy()
        for i in range(len(nums) - 2, -1, -1):
            mins[i] = min(mins[i], nums[i + 1])

        for i, n in enumerate(nums):
            idx = bisect_left(mins, n)
            nums[i] = maxes[max(i, idx - 1)]

        return nums


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxValue"] * 2,
            "kwargs": [
                dict(nums=[2, 1, 3]),
                dict(nums=[2, 3, 1]),
            ],
            "expected": [[2, 2, 3], [3, 3, 3]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

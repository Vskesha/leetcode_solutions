import unittest
from bisect import bisect_left, bisect_right
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        i = bisect_left(nums, 0)
        j = bisect_right(nums, 0)
        return max(i, len(nums) - j)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumCount"] * 3,
            "kwargs": [
                dict(nums=[-2, -1, -1, 1, 2, 3]),
                dict(nums=[-3, -2, -1, 0, 0, 1, 2]),
                dict(nums=[5, 20, 66, 1314]),
            ],
            "expected": [3, 3, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()

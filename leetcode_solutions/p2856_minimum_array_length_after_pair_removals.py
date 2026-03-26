import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        return max(len(nums) % 2, max(Counter(nums).values()) * 2 - len(nums))


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minLengthAfterRemovals"] * 4,
            "kwargs": [
                dict(nums=[1, 2, 3, 4]),
                dict(nums=[1, 1, 2, 2, 3, 3]),
                dict(nums=[1000000000, 1000000000]),
                dict(nums=[2, 3, 4, 4, 4]),
            ],
            "expected": [0, 0, 2, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

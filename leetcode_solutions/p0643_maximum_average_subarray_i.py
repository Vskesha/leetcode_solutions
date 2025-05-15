import unittest
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wsum, mwsum = 0, -inf

        for i in range(k - 1):
            wsum += nums[i]

        for j, i in zip(range(len(nums)), range(k - 1, len(nums))):
            wsum += nums[i]
            if wsum > mwsum:
                mwsum = wsum
            wsum -= nums[j]

        return mwsum / k


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findMaxAverage"] * 2,
            "kwargs": [
                dict(nums = [1,12,-5,-6,50,3], k = 4),
                dict(nums = [5], k = 1),
            ],
            "expected": [12.75000, 5.00000],
            "assert_methods": ["assertAlmostEqualFivePlaces"] * 2,
        },
    ]

    def assertAlmostEqualFivePlaces(self, expected, actual):
        self.assertAlmostEqual(expected, actual, places=5)


if __name__ == "__main__":
    unittest.main()

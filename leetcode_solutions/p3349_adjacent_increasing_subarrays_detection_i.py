import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        ln = len(nums)
        inc = [1] * ln

        for i in range(ln - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc[i] = inc[i + 1] + 1

        for i in range(ln - k * 2 + 1):
            if inc[i] >= k and inc[i + k] >= k:
                return True

        return False


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["hasIncreasingSubarrays"] * 2,
            "kwargs": [
                dict(nums=[2, 5, 7, 8, 9, 2, 3, 4, 3, 1], k=3),
                dict(nums=[1, 2, 3, 4, 4, 4, 4, 5, 6, 7], k=5),
            ],
            "expected": [True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

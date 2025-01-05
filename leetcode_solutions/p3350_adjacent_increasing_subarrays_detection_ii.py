import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ln = len(nums)
        inc = [1] * ln

        for i in range(ln - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc[i] = inc[i + 1] + 1

        def exist2adj(k):
            for i in range(ln - k * 2 + 1):
                if inc[i] >= k and inc[i + k] >= k:
                    return True

            return False

        l, r = 1, ln // 2
        while l < r:
            m = (l + r + 1) // 2
            if exist2adj(m):
                l = m
            else:
                r = m - 1

        return r


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxIncreasingSubarrays"] * 2,
            "kwargs": [
                dict(nums=[2, 5, 7, 8, 9, 2, 3, 4, 3, 1]),
                dict(nums=[1, 2, 3, 4, 4, 4, 4, 5, 6, 7]),
            ],
            "expected": [3, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()

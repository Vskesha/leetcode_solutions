import unittest
from typing import List

from sortedcontainers import SortedList

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        sl = SortedList()
        j = 0
        ans = 0

        for i, n in enumerate(nums):
            sl.add(n)
            while sl[-1] - sl[0] > 2:
                sl.remove(nums[j])
                j += 1
            ans += i - j + 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["continuousSubarrays"] * 2,
            "kwargs": [
                dict(nums=[5, 4, 2, 4]),
                dict(nums=[1, 2, 3]),
            ],
            "expected": [8, 6],
        },
    ]


if __name__ == "__main__":
    unittest.main()

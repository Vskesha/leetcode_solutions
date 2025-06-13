import unittest
from itertools import pairwise
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        mn = mx = nums[0] - nums[-1]
        for d in (a - b for a, b in pairwise(nums)):
            if d < mn:
                mn = d
            elif d > mx:
                mx = d
        return max(mx, -mn)


class Solution2:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = max(abs(a - b) for a, b in pairwise(nums))
        return max(ans, abs(nums[0] - nums[-1]))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxAdjacentDistance"] * 2,
            "kwargs": [
                dict(nums=[1, 2, 4]),
                dict(nums=[-5, -10, -5]),
            ],
            "expected": [3, 5],
        },
    ]


if __name__ == "__main__":
    unittest.main()

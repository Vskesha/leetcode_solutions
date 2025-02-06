import unittest
from itertools import pairwise
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = inc = dec = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                inc = 1
                dec += 1
            else:
                inc = dec = 1
            ans = max(ans, inc, dec)

        return ans


class Solution2:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = inc = dec = 1
        for a, b in pairwise(nums):
            if b > a:
                inc += 1
                dec = 1
            elif b < a:
                inc = 1
                dec += 1
            else:
                inc = dec = 1
            ans = max(ans, inc, dec)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["longestMonotonicSubarray"] * 3,
            "kwargs": [
                dict(nums=[1, 4, 3, 3, 2]),
                dict(nums=[3, 3, 3, 3]),
                dict(nums=[3, 2, 1]),
            ],
            "expected": [2, 1, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()

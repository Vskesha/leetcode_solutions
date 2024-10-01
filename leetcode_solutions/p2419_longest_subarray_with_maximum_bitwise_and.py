import unittest
from itertools import groupby
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mv = max(nums)
        return max(len(list(gr)) for k, gr in groupby(nums) if k == mv)


class Solution2:
    def longestSubarray(self, nums: List[int]) -> int:
        mv, ans = max(nums), 0
        for k, gr in groupby(nums):
            if k == mv:
                ans = max(ans, len(list(gr)))
        return ans


class Solution3:
    def longestSubarray(self, nums: List[int]) -> int:
        mv, ans = 0, 0
        for k, gr in groupby(nums):
            if k > mv:
                mv = k
                ans = len(list(gr))
            elif k == mv:
                ans = max(ans, len(list(gr)))
        return ans


class Solution4:
    def longestSubarray(self, nums: List[int]) -> int:
        mv = max(nums)
        ans = cl = 0

        for n in nums:
            if n == mv:
                cl += 1
                ans = max(ans, cl)
            else:
                cl = 0
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["longestSubarray"] * 2,
            "kwargs": [
                dict(nums=[1, 2, 3, 3, 2, 2]),
                dict(nums=[1, 2, 3, 4]),
            ],
            "expected": [2, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        mx = ans = 0
        for n in nums:
            ans += mx
            mx = max(mx, n)
        return ans


class Solution2:
    def findMaximumScore(self, nums: List[int]) -> int:
        mi = 0
        cm = nums[0]
        ans = 0

        for i, n in enumerate(nums):
            if n > cm:
                ans += cm * (i - mi)
                cm = n
                mi = i
        ans += cm * (len(nums) - 1 - mi)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findMaximumScore"] * 2,
            "kwargs": [
                dict(nums=[1, 3, 1, 5]),
                dict(nums=[4, 3, 1, 3, 2]),
            ],
            "expected": [7, 16],
        },
    ]


if __name__ == "__main__":
    unittest.main()

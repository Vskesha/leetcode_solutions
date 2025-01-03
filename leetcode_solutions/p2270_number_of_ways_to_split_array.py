import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sn = (sum(nums) + 1) // 2
        cs = ans = 0

        for i in range(len(nums) - 1):
            cs += nums[i]
            ans += cs >= sn

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["waysToSplitArray"] * 2,
            "kwargs": [
                dict(nums=[10, 4, -8, 7]),
                dict(nums=[2, 3, 1, 0]),
            ],
            "expected": [2, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()

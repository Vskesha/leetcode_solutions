import unittest
from itertools import groupby
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        for key, group in groupby(nums):
            if key == 0:
                lgr = len(list(group))
                ans += lgr * (lgr + 1) // 2
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["zeroFilledSubarray"] * 3,
            "kwargs": [
                dict(nums = [1,3,0,0,2,0,0,4]),
                dict(nums = [0,0,0,2,0,0]),
                dict(nums = [2,10,2019]),
            ],
            "expected": [6, 9, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

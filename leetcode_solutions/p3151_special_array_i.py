import unittest
from itertools import pairwise
from typing import List

from leetcode_solutions._test_meta import TestMeta

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        pr = (nums[0] - 1) % 2
        for i, n in enumerate(nums):
            cr = n % 2
            if cr == pr:
                return False
            pr = cr
        return True


class Solution2:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all(a % 2 != b % 2 for a, b in pairwise(nums))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["isArraySpecial"] * 3,
            "kwargs": [
                dict(nums=[1]),
                dict(nums=[2, 1, 4]),
                dict(nums=[4, 3, 1, 6]),
            ],
            "expected": [True, True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

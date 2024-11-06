import unittest
from itertools import groupby
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        pmax = 0
        for k, gr in groupby(nums, key=lambda x: x.bit_count()):
            gr = list(gr)
            if min(gr) < pmax:
                return False
            pmax = max(gr)
        return True


class Solution2:
    def canSortArray(self, nums: List[int]) -> bool:
        pmax, cmax = 0, nums[0]
        pcnt = nums[0].bit_count()

        for n in nums:
            if n.bit_count() != pcnt:
                pcnt = n.bit_count()
                pmax = cmax
            if n < pmax:
                return False
            cmax = max(cmax, n)

        return True


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["canSortArray"] * 3,
            "kwargs": [
                dict(nums=[8, 4, 2, 30, 15]),
                dict(nums=[1, 2, 3, 4, 5]),
                dict(nums=[3, 16, 8, 4, 2]),
            ],
            "expected": [True, True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

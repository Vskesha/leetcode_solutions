import operator
import unittest
from functools import reduce
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mn = (1 << maximumBit) - 1
        xr = 0
        ans = []

        for n in nums:
            xr ^= n
            ans.append(mn ^ xr)

        return ans[::-1]


class Solution2:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xr = reduce(operator.xor, nums)
        mn = (1 << maximumBit) - 1
        ans = []

        for n in reversed(nums):
            ans.append(mn ^ xr)
            xr ^= n

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["getMaximumXor"] * 3,
            "kwargs": [
                dict(nums=[0, 1, 1, 3], maximumBit=2),
                dict(nums=[2, 3, 4, 7], maximumBit=3),
                dict(nums=[0, 1, 2, 2, 5, 7], maximumBit=3),
            ],
            "expected": [[0, 3, 2, 3], [5, 2, 6, 5], [4, 3, 6, 4, 6, 7]],
            "assert_methods": ["assertListEqual"] * 3,
        },
    ]


if __name__ == "__main__":
    unittest.main()

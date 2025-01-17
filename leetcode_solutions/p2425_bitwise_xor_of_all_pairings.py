import operator
import unittest
from functools import reduce
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        if len(nums1) % 2:
            for n in nums2:
                ans ^= n
        if len(nums2) % 2:
            for n in nums1:
                ans ^= n
        return ans


class Solution2:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        if len(nums1) % 2:
            ans ^= reduce(operator.xor, nums2)
        if len(nums2) % 2:
            ans ^= reduce(operator.xor, nums1)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["xorAllNums"] * 2,
            "kwargs": [
                dict(nums1=[2, 1, 3], nums2=[10, 2, 5, 0]),
                dict(nums1=[1, 2], nums2=[3, 4]),
            ],
            "expected": [13, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

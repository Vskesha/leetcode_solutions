import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zc1, zc2 = nums1.count(0), nums2.count(0)
        sm1, sm2 = sum(nums1) + zc1, sum(nums2) + zc2
        if (zc1 or sm2 <= sm1) and (zc2 or sm1 <= sm2):
            return max(sm1, sm2)
        return -1


class Solution2:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zc1 = nums1.count(0)
        zc2 = nums2.count(0)
        sm1 = sum(nums1)
        sm2 = sum(nums2)

        if zc1 and zc2:
            return max(sm1 + zc1, sm2 + zc2)
        if zc1:
            return sm2 if sm1 + zc1 <= sm2 else -1
        if zc2:
            return sm1 if sm2 + zc2 <= sm1 else -1
        return sm1 if sm1 == sm2 else -1


class Solution3:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        if 0 in nums1:
            if 0 in nums2:
                return max(
                    sum(nums1) + nums1.count(0), sum(nums2) + nums2.count(0)
                )
            sm2 = sum(nums2)
            if sum(nums1) + nums1.count(0) <= sm2:
                return sm2
            return -1

        if 0 in nums2:
            sm1 = sum(nums1)
            if sum(nums2) + nums2.count(0) <= sm1:
                return sm1
            return -1

        sm1 = sum(nums1)
        if sum(nums2) == sm1:
            return sm1
        return -1


class Solution4:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sm1 = sm2 = zc1 = zc2 = 0

        for n in nums1:
            if n:
                sm1 += n
            else:
                zc1 += 1
        sm1 += zc1

        for n in nums2:
            if n:
                sm2 += n
            else:
                zc2 += 1
        sm2 += zc2

        if zc1 and zc2:
            return max(sm1, sm2)
        if zc1:
            return sm2 if sm1 <= sm2 else -1
        if zc2:
            return sm1 if sm2 <= sm1 else -1
        return sm1 if sm1 == sm2 else -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            # "cls_init_args": [],
            # "cls_init_kwargs": dict(),
            "class_methods": ["minSum"] * 2,
            # "args": [[], ],
            "kwargs": [
                dict(nums1=[3, 2, 0, 1, 0], nums2=[6, 5, 0]),
                dict(nums1=[2, 0, 2, 0], nums2=[1, 4]),
            ],
            "expected": [12, -1],
            # "assert_methods": ["assertMethod"] * n,
        },
    ]


if __name__ == "__main__":
    unittest.main()

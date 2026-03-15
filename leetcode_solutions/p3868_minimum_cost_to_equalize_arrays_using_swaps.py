import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        cnt = cnt1 + cnt2

        ans = 0
        for n, c in cnt.items():
            if c % 2:
                return -1
            ans += abs(c // 2 - cnt1[n])

        return ans // 2


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minCost"] * 3,
            "kwargs": [
                dict(nums1=[10, 20], nums2=[20, 10]),
                dict(nums1=[10, 10], nums2=[20, 20]),
                dict(nums1=[10, 20], nums2=[30, 40]),
            ],
            "expected": [0, 1, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

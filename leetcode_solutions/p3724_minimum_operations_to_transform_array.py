import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        ans = sum(abs(num1 - num2) for num1, num2 in zip(nums1, nums2)) + 1
        print(ans)
        last = nums2[-1]
        min_diff = abs(last - nums1[0])

        for num1, num2 in zip(nums1, nums2):
            if num1 > num2:
                num1, num2 = num2, num1
            if num1 <= last <= num2:
                return ans
            min_diff = min(min_diff, abs(num1 - last), abs(num2 - last))

        return ans + min_diff


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minOperations"] * 3,
            "kwargs": [
                dict(nums1=[2, 8], nums2=[1, 7, 3]),
                dict(nums1=[1, 3, 6], nums2=[2, 4, 5, 3]),
                dict(nums1=[2], nums2=[3, 4]),
            ],
            "expected": [4, 4, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()

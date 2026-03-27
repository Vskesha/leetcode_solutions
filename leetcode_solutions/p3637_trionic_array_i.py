import unittest
from itertools import pairwise
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        ln = len(nums)
        i = j = 1

        if any(a == b for a, b in pairwise(nums)):
            return False

        while i < ln and nums[i] > nums[i - 1]:
            i += 1
        if i == j:
            return False

        j = i
        while i < ln and nums[i] < nums[i - 1]:
            i += 1
        if i == j:
            return False

        if i >= ln:
            return False

        return all(nums[j] > nums[j - 1] for j in range(i, ln))


class Solution2:
    def isTrionic(self, nums: List[int]) -> bool:
        if nums[0] >= nums[1]:
            return False

        ext = 0
        for i in range(2, len(nums)):
            if nums[i] == nums[i - 1]:
                return False
            if (nums[i] - nums[i - 1]) * (nums[i - 1] - nums[i - 2]) < 0:
                if ext == 2:
                    return False
                ext += 1

        return ext == 2


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["isTrionic"] * 2,
            "kwargs": [
                dict(nums=[1, 3, 5, 4, 2, 6]),
                dict(nums=[2, 1, 3]),
            ],
            "expected": [True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

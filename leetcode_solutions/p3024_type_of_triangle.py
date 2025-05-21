import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        p = sum(nums)
        if any(a * 2 >= p for a in nums):
            return "none"
        ln = len(set(nums))
        if ln == 1:
            return "equilateral"
        elif ln == 2:
            return "isosceles"
        else:
            return "scalene"


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["triangleType"] * 2,
            "kwargs": [
                dict(nums=[3, 3, 3]),
                dict(nums=[3, 4, 5]),
            ],
            "expected": ["equilateral", "scalene"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

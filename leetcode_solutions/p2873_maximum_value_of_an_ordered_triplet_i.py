import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        max_difference = 0
        max_val = 0

        for n in nums:
            res = max(res, max_difference * n)
            max_difference = max(max_difference, max_val - n)
            max_val = max(max_val, n)
        return res


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumTripletValue"] * 3,
            "kwargs": [
                dict(nums=[12, 6, 1, 2, 7]),
                dict(nums=[1, 10, 3, 4, 19]),
                dict(nums=[1, 2, 3]),
            ],
            "expected": [77, 133, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

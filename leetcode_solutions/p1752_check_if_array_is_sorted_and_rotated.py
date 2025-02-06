import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def check(self, nums: List[int]) -> bool:
        seen = False
        for i in range(len(nums)):
            if nums[i] < nums[i - 1]:
                if seen:
                    return False
                seen = True
        return True


class Solution2:
    def check(self, nums: List[int]) -> bool:
        return sum(nums[i] < nums[i - 1] for i in range(len(nums))) < 2


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["check"] * 3,
            "kwargs": [
                dict(nums=[3, 4, 5, 1, 2]),
                dict(nums=[2, 1, 3, 4]),
                dict(nums=[1, 2, 3]),
            ],
            "expected": [True, False, True],
        },
    ]


if __name__ == "__main__":
    unittest.main()

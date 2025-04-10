import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        mn = min(nums)
        if mn < k:
            return - 1
        return len(set(nums)) - (k == mn)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minOperations"] * 3,
            "kwargs": [
                dict(nums=[5, 2, 5, 4, 5], k=2),
                dict(nums=[2, 1, 2], k=2),
                dict(nums=[9, 7, 5, 3], k=1),
            ],
            "expected": [2, -1, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()

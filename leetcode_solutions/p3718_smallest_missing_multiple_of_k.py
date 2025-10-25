import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        ln = len(nums) + 1
        nums = set(nums)
        for num in range(k, k * ln + 1, k):
            if num not in nums:
                return num
        return -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["missingMultiple"] * 2,
            "kwargs": [
                dict(nums=[8, 2, 3, 4, 6], k=2),
                dict(nums=[1, 4, 7, 10, 15], k=5),
            ],
            "expected": [10, 5],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                return i // 3 + 1
            seen.add(nums[i])
        return 0


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimumOperations"] * 3,
            "kwargs": [
                dict(nums=[1, 2, 3, 4, 2, 3, 3, 5, 7]),
                dict(nums=[4, 5, 6, 4, 4]),
                dict(nums=[6, 7, 8, 9]),
            ],
            "expected": [2, 2, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

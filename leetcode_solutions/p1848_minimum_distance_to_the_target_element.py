import unittest
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        return min(abs(i - start) for i, n in enumerate(nums) if n == target)


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["getMinDistance"] * 3,
            "kwargs": [
                dict(nums=[1, 2, 3, 4, 5], target=5, start=3),
                dict(nums=[1], target=1, start=0),
                dict(nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], target=1, start=0),
            ],
            "expected": [1, 0, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

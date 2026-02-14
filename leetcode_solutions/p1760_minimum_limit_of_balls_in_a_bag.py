import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            ops = sum((n - 1) // mid for n in nums)
            if ops > maxOperations:
                left = mid + 1
            else:
                right = mid

        return right


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimumSize"] * 2,
            "kwargs": [
                dict(nums=[9], maxOperations=2),
                dict(nums=[2, 4, 8, 2], maxOperations=4),
            ],
            "expected": [3, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()

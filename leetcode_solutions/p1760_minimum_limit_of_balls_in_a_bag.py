import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            m = (l + r) // 2
            ops = sum((n - 1) // m for n in nums)
            if ops > maxOperations:
                l = m + 1
            else:
                r = m

        return r


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

import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(map(int, str(n))) for n in nums)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minElement"] * 3,
            "kwargs": [
                dict(nums=[10, 12, 13, 14]),
                dict(nums=[1, 2, 3, 4]),
                dict(nums=[999, 19, 199]),
            ],
            "expected": [1, 1, 10],
        },
    ]


if __name__ == "__main__":
    unittest.main()

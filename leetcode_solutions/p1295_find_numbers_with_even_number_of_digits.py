import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(str(n)) % 2 == 0 for n in nums)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findNumbers"] * 2,
            "kwargs": [
                dict(nums=[12, 345, 2, 6, 7896]),
                dict(nums=[555, 901, 482, 1771]),
            ],
            "expected": [2, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        unique = set(n for n, c in cnt.items() if c == 1 and n % 2 == 0)
        for n in nums:
            if n in unique:
                return n
        return -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["firstUniqueEven"] * 2,
            "kwargs": [
                dict(nums=[3, 4, 2, 5, 4, 6]),
                dict(nums=[4, 4]),
            ],
            "expected": [2, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

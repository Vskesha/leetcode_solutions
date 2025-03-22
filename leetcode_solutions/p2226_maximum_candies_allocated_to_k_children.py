import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        sc = sum(candies)
        if sc < k:
            return 0
        l, r = 1, sc // k
        while l < r:
            m = (l + r + 1) // 2
            if sum(c // m for c in candies) < k:
                r = m - 1
            else:
                l = m
        return r


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumCandies"] * 2,
            "kwargs": [
                dict(candies = [5,8,6], k = 3),
                dict(candies = [2,5], k = 11),
            ],
            "expected": [5, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

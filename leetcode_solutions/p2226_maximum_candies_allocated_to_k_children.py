import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        sc = sum(candies)
        if sc < k:
            return 0
        left, right = 1, sc // k
        while left < right:
            mid = (left + right + 1) // 2
            if sum(c // mid for c in candies) < k:
                right = mid - 1
            else:
                left = mid
        return right


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumCandies"] * 2,
            "kwargs": [
                dict(candies=[5, 8, 6], k=3),
                dict(candies=[2, 5], k=11),
            ],
            "expected": [5, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

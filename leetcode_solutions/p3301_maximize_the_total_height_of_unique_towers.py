import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)

        for i in range(1, len(maximumHeight)):
            if maximumHeight[i] >= maximumHeight[i - 1]:
                maximumHeight[i] = maximumHeight[i - 1] - 1

        return sum(maximumHeight) if maximumHeight[-1] > 0 else -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumTotalSum"] * 3,
            "kwargs": [
                dict(maximumHeight=[2, 3, 4, 3]),
                dict(maximumHeight=[15, 10]),
                dict(maximumHeight=[2, 2, 1]),
            ],
            "expected": [10, 25, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

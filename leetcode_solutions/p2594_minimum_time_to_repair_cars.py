import unittest
from math import ceil, floor, sqrt
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        l, r = 0, max(ranks) * pow(ceil(cars / len(ranks)), 2)
        while l < r:
            m = (l + r) // 2
            if cars <= sum(floor(sqrt(m / r)) for r in ranks):
                r = m
            else:
                l = m + 1
        return r


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["repairCars"] * 3,
            "kwargs": [
                dict(ranks=[4, 2, 3, 1], cars=10),
                dict(ranks=[5, 1, 8], cars=6),
                dict(ranks=[2, 2, 3, 3, 1, 3, 3, 1, 3], cars=32),
            ],
            "expected": [16, 16, 32],
        },
    ]


if __name__ == "__main__":
    unittest.main()

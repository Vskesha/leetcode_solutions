import unittest
from itertools import accumulate
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        max_acc = min_acc = 0
        for acc in accumulate(differences):
            if acc > max_acc:
                max_acc = acc
            elif acc < min_acc:
                min_acc = acc
        return max(0, upper - lower - max_acc + min_acc + 1)


class Solution2:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        acc = list(accumulate(differences, initial=0))
        diff = upper - lower - max(acc) + min(acc) + 1
        return diff if diff > 0 else 0


class Solution3:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        return max(0, upper - lower - max(accumulate(differences, initial=0)) + min(
            accumulate(differences, initial=0)) + 1)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["numberOfArrays"] * 3,
            "kwargs": [
                dict(differences=[1, -3, 4], lower=1, upper=6),
                dict(differences=[3, -4, 5, 1, -2], lower=-4, upper=5),
                dict(differences=[4, -7, 2], lower=3, upper=6),
            ],
            "expected": [2, 4, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

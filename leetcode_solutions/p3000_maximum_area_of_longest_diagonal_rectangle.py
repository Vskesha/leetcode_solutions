import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = max_area = 0
        for length, width in dimensions:
            curr_diag = length * length + width * width
            if curr_diag > max_diag:
                max_area = length * width
                max_diag = curr_diag
            elif curr_diag == max_diag:
                max_area = max(max_area, length * width)
        return max_area


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["areaOfMaxDiagonal"] * 2,
            "kwargs": [
                dict(dimensions=[[9, 3], [8, 6]]),
                dict(dimensions=[[3, 4], [4, 3]]),
            ],
            "expected": [48, 12],
        },
    ]


if __name__ == "__main__":
    unittest.main()

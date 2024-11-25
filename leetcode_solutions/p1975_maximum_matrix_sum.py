import unittest
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sm = sum(abs(val) for row in matrix for val in row)
        mn = min(abs(val) for row in matrix for val in row)
        cnt = sum(val < 0 for row in matrix for val in row)
        return sm - 2 * mn if cnt % 2 else sm


class Solution2:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sm = cnt = 0
        mn = inf

        for row in matrix:
            for val in row:
                if val < 0:
                    cnt += 1
                    sm -= val
                    mn = min(mn, -val)
                else:
                    sm += val
                    mn = min(mn, val)

        return sm - 2 * mn if cnt % 2 else sm


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxMatrixSum"] * 2,
            "kwargs": [
                dict(matrix=[[1, -1], [-1, 1]]),
                dict(matrix=[[1, 2, 3], [-1, -2, -3], [1, 2, 3]]),
            ],
            "expected": [4, 16],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        pr = [0] * n
        ans = 0

        for row in matrix:
            seq = row[0]
            nr = [0] * n
            nr[0] = row[0]
            ans += row[0]
            for i in range(1, n):
                if row[i]:
                    seq += 1
                    nr[i] = pr[i] + 1
                else:
                    seq = 0
                nr[i] = min(seq, nr[i], pr[i - 1] + 1)
                ans += nr[i]
            pr = nr

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countSquares"] * 2,
            "kwargs": [
                dict(matrix=[[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]),
                dict(matrix=[[1, 0, 1], [1, 1, 0], [1, 1, 0]]),
            ],
            "expected": [15, 7],
        },
    ]


if __name__ == "__main__":
    unittest.main()

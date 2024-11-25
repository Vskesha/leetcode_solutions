import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        rows = Counter()

        for row in matrix:
            t = tuple(row) if row[0] == 0 else tuple(x ^ 1 for x in row)
            rows[t] += 1

        return max(rows.values())


class Solution2:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        rows = Counter()

        for row in matrix:
            rows["".join(str(int(v == row[0])) for v in row)] += 1

        return max(rows.values())


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxEqualRowsAfterFlips"] * 3,
            "kwargs": [
                dict(matrix=[[0, 1], [1, 1]]),
                dict(matrix=[[0, 1], [1, 0]]),
                dict(matrix=[[0, 0, 0], [0, 0, 1], [1, 1, 0]]),
            ],
            "expected": [1, 2, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()

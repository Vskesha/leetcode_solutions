import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        mp = {mat[i][j]: (i, j) for i in range(m) for j in range(n)}
        rows, cols = [n] * m, [m] * n

        for ai, num in enumerate(arr):
            i, j = mp[num]
            rows[i] -= 1
            cols[j] -= 1
            if not (rows[i] and cols[j]):
                return ai


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["firstCompleteIndex"] * 2,
            "kwargs": [
                dict(arr=[1, 3, 4, 2], mat=[[1, 4], [2, 3]]),
                dict(
                    arr=[2, 8, 7, 4, 1, 3, 5, 6, 9],
                    mat=[[3, 2, 5], [1, 4, 6], [8, 7, 9]],
                ),
            ],
            "expected": [2, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()

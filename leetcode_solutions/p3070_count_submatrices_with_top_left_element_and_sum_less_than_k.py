import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        lr = len(grid[0])
        sums = [0] * lr
        ans = 0

        for row in grid:
            csum = 0
            for j, val in enumerate(row):
                sums[j] += val
                csum += sums[j]
                if csum > k:
                    ans += j
                    break
            else:
                ans += lr

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countSubmatrices"] * 2,
            "kwargs": [
                dict(grid=[[7, 6, 3], [6, 6, 1]], k=18),
                dict(grid=[[7, 2, 9], [1, 5, 0], [2, 6, 6]], k=20),
            ],
            "expected": [4, 6],
        },
    ]


if __name__ == "__main__":
    unittest.main()

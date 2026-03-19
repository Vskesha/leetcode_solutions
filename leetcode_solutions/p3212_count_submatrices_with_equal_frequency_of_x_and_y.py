import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n = len(grid[0])

        xcnt = [0] * n
        psum = [0] * n
        ans = 0

        for row in grid:
            sacc = 0
            xacc = 0
            for j, val in enumerate(row):
                if val == "X":
                    xcnt[j] += 1
                    psum[j] += 1
                elif val == "Y":
                    psum[j] -= 1
                sacc += psum[j]
                xacc += xcnt[j]
                if xacc and not sacc:
                    ans += 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["numberOfSubmatrices"] * 3,
            "kwargs": [
                dict(grid=[["X", "Y", "."], ["Y", ".", "."]]),
                dict(grid=[["X", "X"], ["X", "Y"]]),
                dict(grid=[[".", "."], [".", "."]]),
            ],
            "expected": [3, 0, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

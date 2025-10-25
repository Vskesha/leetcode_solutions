import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for i in range(n):
            values = sorted(
                (grid[i + j][j] for j in range(n - i)), reverse=True
            )
            for j, val in enumerate(values):
                grid[i + j][j] = val

        for j in range(1, n):
            values = sorted(grid[i][i + j] for i in range(n - j))
            for i, val in enumerate(values):
                grid[i][i + j] = val

        return grid


class Solution2:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for rng in range(n, 0, -1):
            for i in range(1, rng):
                for j in range(1, i + 1):
                    if grid[i][j] > grid[i - 1][j - 1]:
                        grid[i][j], grid[i - 1][j - 1] = (
                            grid[i - 1][j - 1],
                            grid[i][j],
                        )
                for j in range(i + 1, rng):
                    if grid[i][j] < grid[i - 1][j - 1]:
                        grid[i][j], grid[i - 1][j - 1] = (
                            grid[i - 1][j - 1],
                            grid[i][j],
                        )

        return grid


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["sortMatrix"] * 3,
            "kwargs": [
                dict(grid=[[1, 7, 3], [9, 8, 2], [4, 5, 6]]),
                dict(grid=[[0, 1], [1, 2]]),
                dict(grid=[[1]]),
            ],
            "expected": [
                [[8, 2, 3], [9, 6, 7], [4, 5, 1]],
                [[2, 1], [1, 0]],
                [[1]],
            ],
            "assert_methods": ["assertMatrixEqual"] * 3,
        },
    ]

    def assertMatrixEqual(
        self, actual: list[list[int]], expected: list[list[int]]
    ):
        self.assertEqual(len(actual), len(expected))
        for row1, row2 in zip(actual, expected):
            self.assertListEqual(row1, row2)


if __name__ == "__main__":
    unittest.main()

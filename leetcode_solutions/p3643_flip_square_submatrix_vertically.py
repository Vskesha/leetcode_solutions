import unittest
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


# fmt: off
class Solution:
    def reverseSubmatrix(
            self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        return [[grid[2 * x + k - 1 - i][j] if x <= i < (x + k) and y <= j < (y + k) else grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]  # noqa: E501
# fmt: on


class Solution2:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        x2 = 2 * x + k - 1
        for i in range(x, x + k // 2):
            for j in range(y, y + k):
                grid[i][j], grid[x2 - i][j] = grid[x2 - i][j], grid[i][j]
        return grid


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["reverseSubmatrix"] * 2,
            "kwargs": [
                dict(
                    grid=[
                        [1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, 16],
                    ],
                    x=1,
                    y=0,
                    k=3,
                ),
                dict(grid=[[3, 4, 2, 3], [2, 3, 4, 2]], x=0, y=2, k=2),
            ],
            "expected": [
                [
                    [1, 2, 3, 4],
                    [13, 14, 15, 8],
                    [9, 10, 11, 12],
                    [5, 6, 7, 16],
                ],
                [[3, 4, 4, 2], [2, 3, 2, 3]],
            ],
            "assert_methods": ["assertMatrixEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

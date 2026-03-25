import unittest
from itertools import accumulate
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        racc = list(accumulate(sum(row) for row in grid))
        cacc = list(accumulate(sum(col) for col in zip(*grid)))
        return not racc[-1] % 2 and (
            racc[-1] // 2 in racc or racc[-1] // 2 in cacc
        )


class Solution4:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        racc = list(accumulate(sum(row) for row in grid))
        cacc = list(accumulate(sum(col) for col in zip(*grid)))
        total = racc[-1]
        if total % 2:
            return False
        return total // 2 in racc or total // 2 in cacc


class Solution5:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(val for row in grid for val in row)
        if total % 2:
            return False
        t2 = total // 2

        rsum = 0
        for row in grid:
            rsum += sum(row)
            if rsum >= t2:
                if rsum == t2:
                    return True
                break

        csum = 0
        for col in zip(*grid):
            csum += sum(col)
            if csum >= t2:
                if csum == t2:
                    return True
                break

        return False


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["canPartitionGrid"] * 2,
            "kwargs": [
                dict(grid=[[1, 4], [2, 3]]),
                dict(grid=[[1, 3], [2, 4]]),
            ],
            "expected": [True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

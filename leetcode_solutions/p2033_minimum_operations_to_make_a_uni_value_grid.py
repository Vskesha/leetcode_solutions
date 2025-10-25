import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:

        vals = [n for row in grid for n in row]
        rem = vals[0] % x
        for n in vals:
            if n % x != rem:
                return -1

        vals.sort()
        mi = len(vals) // 2
        ans = (sum(vals[mi + len(vals) % 2 :]) - sum(vals[:mi], 0)) // x
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minOperations"] * 3,
            "kwargs": [
                dict(grid=[[2, 4], [6, 8]], x=2),
                dict(grid=[[1, 5], [2, 3]], x=1),
                dict(grid=[[1, 2], [3, 4]], x=2),
            ],
            "expected": [4, 5, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

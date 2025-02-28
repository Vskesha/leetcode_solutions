import unittest
from heapq import heappushpop
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        maxs = [(-inf, 0), (-inf, 0)]
        mins = [(-inf, 0), (-inf, 0)]

        for i, arr in enumerate(arrays):
            heappushpop(maxs, (arr[-1], i))
            heappushpop(mins, (-arr[0], i))

        if maxs[1][1] == mins[1][1]:
            return max(maxs[0][0] + mins[1][0], maxs[1][0] + mins[0][0])
        else:
            return maxs[1][0] + mins[1][0]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxDistance", "maxDistance"],
            "kwargs": [
                dict(arrays=[[1, 2, 3], [4, 5], [1, 2, 3]]),
                dict(arrays=[[1], [1]]),
            ],
            "expected": [4, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

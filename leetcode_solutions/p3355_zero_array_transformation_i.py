import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        ln = len(nums)
        diffs = [0] * (ln + 1)

        for li, ri in queries:
            diffs[li] += 1
            diffs[ri + 1] -= 1

        diff = 0
        for n, d in zip(nums, diffs):
            diff += d
            if diff < n:
                return False
        return True


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["isZeroArray"] * 2,
            "kwargs": [
                dict(nums=[1, 0, 1], queries=[[0, 2]]),
                dict(nums=[4, 3, 2, 1], queries=[[1, 3], [0, 2]]),
            ],
            "expected": [True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        ln = len(nums)

        def can_process(k):
            diffs = [0] * (ln + 1)
            for li, ri, val in queries[:k]:
                diffs[li] += val
                diffs[ri + 1] -= val
            diff = 0
            for n, d in zip(nums, diffs):
                diff += d
                if diff < n:
                    return False
            return True

        lq = len(queries)
        if not can_process(lq):
            return -1

        left, right = 0, lq
        while left < right:
            m = (left + right) // 2
            if can_process(m):
                right = m
            else:
                left = m + 1
        return left


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minZeroArray"] * 2,
            "kwargs": [
                dict(
                    nums=[2, 0, 2], queries=[[0, 2, 1], [0, 2, 1], [1, 1, 3]]
                ),
                dict(nums=[4, 3, 2, 1], queries=[[1, 3, 2], [0, 2, 1]]),
            ],
            "expected": [2, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

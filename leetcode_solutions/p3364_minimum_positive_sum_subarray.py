import unittest
from itertools import accumulate
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimumSumSubarray(
        self, nums: List[int], left: int, right: int
    ) -> int:
        ln = len(nums)
        acc = list(accumulate(nums, initial=0))
        return min(
            filter(
                lambda x: x > 0,
                [
                    acc[i + s] - acc[i]
                    for s in range(left, right + 1)
                    for i in range(ln - s + 1)
                ],
            ),
            default=-1,
        )


class Solution2:
    def minimumSumSubarray(
        self, nums: List[int], left: int, right: int
    ) -> int:
        ans = inf
        ln = len(nums)
        acc = list(accumulate(nums, initial=0))
        for sz in range(left, right + 1):
            for i in range(ln - sz + 1):
                sm = acc[i + sz] - acc[i]
                if sm > 0:
                    ans = min(ans, sm)
        return -1 if ans == inf else ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimumSumSubarray"] * 3,
            "kwargs": [
                dict(nums=[3, -2, 1, 4], left=2, right=3),
                dict(nums=[-2, 2, -3, 1], left=2, right=3),
                dict(nums=[1, 2, 3, 4], left=2, right=4),
            ],
            "expected": [1, -1, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()

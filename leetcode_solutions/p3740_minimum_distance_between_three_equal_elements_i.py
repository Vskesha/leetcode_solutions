import unittest
from collections import defaultdict
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        idx = defaultdict(list)
        for i, n in enumerate(nums):
            idx[n].append(i)

        return min(
            (
                min(inds[i + 2] - inds[i] for i in range(len(inds) - 2)) * 2
                for inds in idx.values()
                if len(inds) >= 3
            ),
            default=-1,
        )


class Solution2:
    def minimumDistance(self, nums: List[int]) -> int:
        idx = defaultdict(list)

        for i, n in enumerate(nums):
            idx[n].append(i)

        ans = inf
        for inds in idx.values():
            if len(inds) < 3:
                continue
            curr = min(inds[i + 2] - inds[i] for i in range(len(inds) - 2)) * 2
            ans = min(ans, curr)

        return -1 if ans == inf else ans


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimumDistance"] * 3,
            "kwargs": [
                dict(nums=[1, 2, 1, 1, 3]),
                dict(nums=[1, 1, 2, 3, 2, 1, 2]),
                dict(nums=[1]),
            ],
            "expected": [6, 8, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

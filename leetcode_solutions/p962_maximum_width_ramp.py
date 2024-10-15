import unittest
from bisect import bisect_left
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [(inf, inf)]
        ans = 0

        for j, n in enumerate(nums):
            if n < stack[-1][0]:
                stack.append((n, j))
            else:
                si = bisect_left(stack, (n, 0))
                i = stack[si][1]
                ans = max(ans, j - i)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxWidthRamp"] * 2,
            "kwargs": [
                dict(nums = [6,0,8,2,1,5]),
                dict(nums = [9,8,1,0,1,9,4,0,4,1]),
            ],
            "expected": [4, 7],
        },
    ]


if __name__ == '__main__':
    unittest.main()

import unittest
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        indices = sorted(range(len(nums)), key=lambda i: nums[i])
        mi = indices[0]
        ans = 0
        for i in indices:
            if i < mi:
                mi = i
            else:
                ans = max(ans, i - mi)
        return ans


class Solution3:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [(inf, inf)]
        ans = 0

        for j, n in enumerate(nums):
            if n < stack[-1][0]:
                stack.append((n, j))
            else:
                l, r = 0, len(stack) - 1
                while l < r:
                    m = (l + r) // 2
                    if stack[m][0] > n:
                        l = m + 1
                    else:
                        r = m
                ans = max(ans, j - stack[l][1])

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxWidthRamp"] * 2,
            "kwargs": [
                dict(nums=[6, 0, 8, 2, 1, 5]),
                dict(nums=[9, 8, 1, 0, 1, 9, 4, 0, 4, 1]),
            ],
            "expected": [4, 7],
        },
    ]


if __name__ == "__main__":
    unittest.main()

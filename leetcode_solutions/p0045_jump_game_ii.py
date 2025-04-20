import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def jump(self, nums: List[int]) -> int:
        nxt = reach = jumps = 0

        for i, n in enumerate(nums):
            if i > reach:
                jumps += 1
                reach = nxt
            nxt = max(nxt, i + n)

        return jumps


class Solution2:
    def jump(self, nums: List[int]) -> int:
        ln = len(nums)
        jumps = [ln] * ln
        jumps[0] = 0

        for i in range(ln):
            for j in range(1, min(ln, i + nums[i] + 1)):
                jumps[j] = min(jumps[j], jumps[i] + 1)

        return jumps[-1]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["jump"] * 2,
            "kwargs": [
                dict(nums = [2,3,1,1,4]),
                dict(nums = [2,3,0,1,4]),
            ],
            "expected": [2, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()

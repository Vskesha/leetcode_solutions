import unittest
from heapq import heappop, heappush
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        for i, lst in enumerate(nums):
            heappush(heap, (lst[0], i, 1))
        mx = max(lst[0] for lst in nums)
        ans = [-inf, inf]

        while True:
            v, i, j = heappop(heap)
            if mx - v < ans[1] - ans[0]:
                ans = [v, mx]
            if j == len(nums[i]):
                return ans
            mx = max(mx, nums[i][j])
            heappush(heap, (nums[i][j], i, j + 1))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["smallestRange"] * 2,
            "kwargs": [
                dict(nums=[[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]),
                dict(nums=[[1, 2, 3], [1, 2, 3], [1, 2, 3]]),
            ],
            "expected": [
                [20, 24],
                [1, 1],
            ],
        },
    ]


if __name__ == "__main__":
    unittest.main()

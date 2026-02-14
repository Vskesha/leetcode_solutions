import unittest
from typing import List

from sortedcontainers import SortedList

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ln = len(nums)
        li, ri = 0, 0
        ans = 0

        for i in range(ln - 1, 0, -1):
            nupper = upper - nums[i]
            nlower = lower - nums[i]
            while ri < i and nums[ri] <= nupper:
                ri += 1
            while li < i and nums[li] < nlower:
                li += 1
            if li == i:
                break
            ans += min(ri, i) - li

        return ans


class Solution2:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sl = SortedList()
        lower -= 1
        ans = 0

        for n in nums:
            ans += sl.bisect_right(upper - n) - sl.bisect_right(lower - n)
            sl.add(n)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countFairPairs"] * 3,
            "kwargs": [
                dict(nums=[0, 0, 0, 0, 0, 0], lower=0, upper=0),
                dict(nums=[0, 1, 7, 4, 4, 5], lower=3, upper=6),
                dict(nums=[1, 7, 9, 2, 5], lower=11, upper=11),
            ],
            "expected": [15, 6, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

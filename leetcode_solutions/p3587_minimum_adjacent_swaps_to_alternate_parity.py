import unittest
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ans = inf
        ln = len(nums)

        for oi in (0, 1):
            swaps = 0
            for i, n in enumerate(nums):
                if n % 2:
                    swaps += abs(i - oi)
                    oi += 2
            if ln <= oi <= ln + 1 and swaps < ans:
                ans = swaps

        return -1 if ans == inf else ans


class Solution2:
    def minSwaps(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln == 1:
            return 0

        even, odd = 0, 0
        for n in nums:
            if n % 2:
                odd += 1
            else:
                even += 1

        if abs(even - odd) > 1:
            return -1

        if len(nums) % 2:
            oi = 0 if even < odd else 1
            ans = 0
            for i, n in enumerate(nums):
                if n % 2:
                    ans += abs(i - oi)
                    oi += 2
            return ans

        ans1 = 0
        oi = 0
        for i, n in enumerate(nums):
            if n % 2:
                ans1 += abs(i - oi)
                oi += 2
        ans2 = 0
        oi = 1
        for i, n in enumerate(nums):
            if n % 2:
                ans2 += abs(i - oi)
                oi += 2
        return min(ans1, ans2)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minSwaps"] * 4,
            "kwargs": [
                dict(nums=[2, 4, 6, 5, 7]),
                dict(nums=[2, 4, 5, 7]),
                dict(nums=[1, 2, 3]),
                dict(nums=[4, 5, 6, 8]),
            ],
            "expected": [3, 1, 0, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

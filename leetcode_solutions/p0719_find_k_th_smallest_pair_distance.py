import unittest
from bisect import bisect_right
from heapq import heapify, heappop, heappush
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        ln = len(nums)
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2

            dists = j = 0
            for i in range(ln - 1):
                target = nums[i] + mid
                while j < ln and nums[j] <= target:
                    j += 1
                dists += j - i - 1

            if dists < k:
                left = mid + 1
            else:
                right = mid

        return left


class Solution1:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if (
                sum(
                    bisect_right(nums, nums[i] + mid) - i - 1
                    for i in range(len(nums) - 1)
                )
                < k
            ):
                left = mid + 1
            else:
                right = mid
        return left


class Solution2:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def dists_less_equal(target: int, nums: List[int]) -> int:
            ans = 0
            for i in range(len(nums) - 1):
                j = bisect_right(nums, nums[i] + target)
                ans += j - i - 1
            return ans

        nums.sort()
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            if dists_less_equal(mid, nums) < k:
                left = mid + 1
            else:
                right = mid

        return left


class Solution3:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        dists = [(nums[i + 1] - nums[i], i, i + 1) for i in range(n - 1)]
        heapify(dists)
        d = 0

        for _ in range(k):
            d, i, j = heappop(dists)
            if j < n - 1:
                heappush(dists, (nums[j + 1] - nums[i], i, j + 1))

        return d


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["smallestDistancePair"] * 3,
            "kwargs": [
                dict(nums=[1, 3, 1], k=1),
                dict(nums=[1, 1, 1], k=2),
                dict(nums=[1, 6, 1], k=3),
            ],
            "expected": [0, 0, 5],
        },
    ]


if __name__ == "__main__":
    unittest.main()

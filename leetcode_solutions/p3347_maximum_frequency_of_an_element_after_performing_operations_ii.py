import unittest
from collections import Counter
from itertools import groupby
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        freq = Counter(nums)
        ans = 1
        i, j = 0, 0
        ln = len(nums)

        for n in nums:
            while nums[i] < n - k:
                i += 1
            while j < ln and nums[j] <= n + k:
                j += 1
            ans = max(ans, min(j - i - freq[n], numOperations) + freq[n])

        if ans >= numOperations:
            return ans

        i = 0
        k *= 2
        for j, n in enumerate(nums, 1):
            while nums[i] < n - k:
                i += 1
            ans = max(ans, j - i)
            if ans >= numOperations:
                return numOperations

        return ans


class Solution2:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        ln = len(nums)
        sti, eni = 0, 1
        ans = 1

        for v, gr in groupby(nums):
            while nums[sti] < v - k:
                sti += 1
            while eni < ln and nums[eni] <= v + k:
                eni += 1
            lgr = len(list(gr))
            op = min(eni - sti - lgr, numOperations)
            ans = max(ans, op + lgr)

        eni = 1
        for sti in range(ln):
            while eni < ln and nums[eni] <= nums[sti] + 2 * k:
                eni += 1
            op = min(eni - sti, numOperations)
            ans = max(ans, op)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxFrequency"] * 3,
            "kwargs": [
                dict(nums=[93, 84, 148, 39, 46], k=32, numOperations=3),
                dict(nums=[1, 4, 5], k=1, numOperations=2),
                dict(nums=[5, 11, 20, 20], k=5, numOperations=1),
            ],
            "expected": [3, 2, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()

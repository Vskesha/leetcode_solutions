import unittest
from itertools import groupby
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        if minK == maxK:
            groups = (
                sum(1 for _ in gr) for k, gr in groupby(nums) if k == minK
            )
            return sum(n * (n + 1) // 2 for n in groups)

        sti = eni = mni = mxi = -1
        ans = 0

        for i, n in enumerate(nums):
            if n < minK or n > maxK:
                sti = eni = mni = mxi = i
            elif n == minK:
                mni = i
                eni = min(mni, mxi)
            elif n == maxK:
                mxi = i
                eni = min(mni, mxi)
            ans += eni - sti

        return ans


class Solution1:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        if minK == maxK:
            groups = (
                sum(1 for _ in gr) for k, gr in groupby(nums) if k == minK
            )
            return sum(n * (n + 1) // 2 for n in groups)

        sti = mni = mxi = -1
        ans = 0

        for i, n in enumerate(nums):
            if n < minK or n > maxK:
                sti = mni = mxi = i
            elif n == minK:
                mni = i
            elif n == maxK:
                mxi = i
            ans += min(mxi, mni) - sti

        return ans


class Solution2:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0

        if minK == maxK:
            gr = 0
            for n in nums:
                if n == minK:
                    gr += 1
                else:
                    ans += gr * (gr + 1) // 2
                    gr = 0
            ans += gr * (gr + 1) // 2
            return ans

        sti = mni = mxi = -1

        for i, n in enumerate(nums):
            if n < minK or n > maxK:
                sti = mni = mxi = i
            elif n == minK:
                mni = i
            elif n == maxK:
                mxi = i
            ans += min(mxi, mni) - sti

        return ans


class Solution3:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        def get_count_from_subarr(st, end) -> int:
            ans = 0
            min_idx = max_idx = begin = st - 1
            for i in range(st, end):
                if nums[i] == minK:
                    min_idx = i
                    begin = min(min_idx, max_idx)
                if nums[i] == maxK:
                    max_idx = i
                    begin = min(min_idx, max_idx)
                ans += begin - st + 1
            return ans

        ln = len(nums)
        i = 0
        ans = 0
        while i < ln:
            while i < ln and (nums[i] < minK or nums[i] > maxK):
                i += 1
            st = i
            while i < ln and minK <= nums[i] <= maxK:
                i += 1
            ans += get_count_from_subarr(st, i)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countSubarrays"] * 2,
            "kwargs": [
                dict(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5),
                dict(nums=[1, 1, 1, 1], minK=1, maxK=1),
            ],
            "expected": [2, 10],
        },
    ]


if __name__ == "__main__":
    unittest.main()

# def test_count_subarrays():
#     sol = Solution()
#
#     print("Test 1... ", end="")
#     assert sol.countSubarrays(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5) == 2
#     print("OK")
#
#     print("Test 2... ", end="")
#     assert sol.countSubarrays(nums=[1, 1, 1, 1], minK=1, maxK=1) == 10
#     print("OK")


# if __name__ == "__main__":
#     test_count_subarrays()

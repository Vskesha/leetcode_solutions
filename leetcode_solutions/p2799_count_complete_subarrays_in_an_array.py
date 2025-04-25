import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        d = len(set(nums))
        cnt = {}
        i = ans = 0
        inums = iter(nums)

        for n in inums:
            cnt[n] = cnt.get(n, 0) + 1
            if len(cnt) == d:
                break
        while cnt[nums[i]] > 1:
            cnt[nums[i]] -= 1
            i += 1
        ans += i + 1

        for n in inums:
            cnt[n] = cnt.get(n, 0) + 1
            while cnt[nums[i]] > 1:
                cnt[nums[i]] -= 1
                i += 1
            ans += i + 1

        return ans


class Solution2:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        d = len(set(nums))
        cnt = {}
        ans = j = 0
        ln = len(nums)

        for n in nums:
            while j < ln and len(cnt) < d:
                cnt[nums[j]] = cnt.get(nums[j], 0) + 1
                j += 1
            if len(cnt) < d:
                break
            ans += ln - j + 1
            if cnt[n] > 1:
                cnt[n] -= 1
            else:
                del cnt[n]

        return ans


class Solution3:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        d = len(set(nums))
        cnt = {}
        i = ans = 0

        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1
            if len(cnt) < d:
                continue
            while cnt[nums[i]] > 1:
                cnt[nums[i]] -= 1
                i += 1
            ans += i + 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countCompleteSubarrays"] * 2,
            "kwargs": [
                dict(nums=[1, 3, 1, 2, 2]),
                dict(nums=[5, 5, 5, 5]),
            ],
            "expected": [4, 10],
        },
    ]


if __name__ == "__main__":
    unittest.main()

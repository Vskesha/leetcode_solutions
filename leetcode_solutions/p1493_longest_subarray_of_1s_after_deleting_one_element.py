import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ln = len(nums)
        if all(nums):
            return ln - 1
        if not any(nums):
            return 0

        lengths = [0] * ln

        curr = 0
        for i, n in enumerate(nums):
            if n:
                curr += 1
            else:
                lengths[i] += curr
                curr = 0

        curr = 0
        for i in range(ln - 1, -1, -1):
            if nums[i]:
                curr += 1
            else:
                lengths[i] += curr
                curr = 0

        return max(lengths)


class Solution2:
    def longestSubarray(self, nums: list[int]) -> int:
        prev = curr = ans = 0
        for n in nums:
            if n:
                curr += 1
            else:
                ans = max(ans, prev + curr)
                prev = curr
                curr = 0
        ans = max(ans, prev + curr)

        return ans if ans < len(nums) else len(nums) - 1


class Solution3:
    def longestSubarray(self, nums: list[int]) -> int:
        prev_len = curr_len = gap = prev = ans = 0
        n = len(nums)
        nums.append(0)

        for num in nums:
            if num:
                if not prev:
                    prev_len = curr_len
                    curr_len = 0
                curr_len += 1
            else:
                if prev:
                    if gap == 1:
                        ans = max(ans, prev_len + curr_len)
                    else:
                        ans = max(ans, curr_len)
                    gap = 0
                gap += 1
            prev = num

        return ans if ans < n else n - 1


class Solution4:
    def longestSubarray(self, nums: list[int]) -> int:
        prev_len = 0
        curr_len = 0
        ans = 0
        gap = 0
        i = 0
        n = len(nums)
        while i < n:
            gap = 0
            while i < n and not nums[i]:
                gap += 1
                i += 1
            curr_len = 0
            while i < n and nums[i]:
                curr_len += 1
                i += 1
            if gap == 1:
                ans = max(ans, curr_len + prev_len)
            else:
                ans = max(ans, curr_len)
            prev_len = curr_len
        return ans if ans < n else n - 1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["longestSubarray"] * 3,
            "kwargs": [
                dict(nums=[1, 1, 0, 1]),
                dict(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]),
                dict(nums=[1, 1, 1]),
            ],
            "expected": [3, 5, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()

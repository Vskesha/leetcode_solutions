import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = {}
        ln = len(nums)
        li = curr = ans = 0

        for ri, num in enumerate(nums):
            if num in freq:
                curr += freq[num]
                freq[num] += 1
            else:
                freq[num] = 1

            while curr >= k:
                ans += ln - ri
                freq[nums[li]] -= 1
                curr -= freq[nums[li]]
                li += 1

        return ans


class Solution2:
    def countGood(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        curr_pairs = 0
        sti = 0
        ans = 0

        for num in nums:
            curr_pairs += cnt[num]
            cnt[num] += 1

            if curr_pairs < k:
                continue

            while curr_pairs - cnt[nums[sti]] + 1 >= k:
                cnt[nums[sti]] -= 1
                curr_pairs -= cnt[nums[sti]]
                sti += 1

            ans += sti + 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countGood"] * 2,
            "kwargs": [
                dict(nums=[1, 1, 1, 1, 1], k=10),
                dict(nums=[3, 1, 4, 3, 2, 2, 4], k=2),
            ],
            "expected": [1, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()

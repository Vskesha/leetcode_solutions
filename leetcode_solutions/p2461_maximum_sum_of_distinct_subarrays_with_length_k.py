import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        k -= 1
        cnt = Counter(nums[:k])
        curr = sum(nums[:k])
        ans = 0

        for cv, pv in zip(nums[k:], nums):
            cnt[cv] += 1
            curr += cv
            if len(cnt) > k:
                ans = max(ans, curr)
            curr -= pv
            cnt[pv] -= 1
            if not cnt[pv]:
                del cnt[pv]

        return ans


class Solution2:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i = ans = curr = 0
        seen = set()

        for n in nums:

            if n in seen:
                while nums[i] != n:
                    curr -= nums[i]
                    seen.remove(nums[i])
                    i += 1
                i += 1
            else:
                curr += n
                seen.add(n)

            if len(seen) == k:
                ans = max(ans, curr)
                curr -= nums[i]
                seen.remove(nums[i])
                i += 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumSubarraySum"] * 2,
            "kwargs": [
                dict(nums=[1, 5, 4, 2, 9, 9, 9], k=3),
                dict(nums=[4, 4, 4], k=3),
            ],
            "expected": [15, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        cnt = Counter(n - i for i, n in enumerate(nums))
        return (
            len(nums) * (len(nums) - 1) - sum(v * (v - 1) for v in cnt.values())
        ) // 2


class Solution2:
    def countBadPairs(self, nums: List[int]) -> int:
        cnt = Counter()
        ans = 0
        for i, n in enumerate(nums):
            ans += i - cnt[n - i]
            cnt[n - i] += 1
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countBadPairs"] * 2,
            "kwargs": [
                dict(nums=[4, 1, 3, 3]),
                dict(nums=[1, 2, 3, 4, 5]),
            ],
            "expected": [5, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        dom = max(cnt, key=lambda x: cnt[x])
        left = cnt[dom]

        ln = len(nums)
        seen = 0
        for i, n in enumerate(nums, 1):
            if n == dom:
                seen += 1
                left -= 1
            if seen > i // 2 and left > (ln - i) // 2:
                return i - 1

        return -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimumIndex"] * 3,
            "kwargs": [
                dict(nums=[1, 2, 2, 2]),
                dict(nums=[2, 1, 3, 1, 1, 1, 7, 1, 2, 1]),
                dict(nums=[3, 3, 3, 3, 7, 2, 2]),
            ],
            "expected": [2, 4, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from collections import Counter
from math import log
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        cnt = Counter()
        for n in candidates:
            for i, b in enumerate(bin(n)[::-1]):
                if b == "1":
                    cnt[i] += 1
        return max(cnt.values())


class Solution2:
    def largestCombination(self, candidates: List[int]) -> int:
        mi = int(log(max(candidates), 2)) + 1
        ni = 1
        ans = 0
        for i in range(mi):
            ans = max(ans, sum(1 for n in candidates if n & ni))
            ni *= 2
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["largestCombination"] * 2,
            "kwargs": [
                dict(candidates=[16, 17, 71, 62, 12, 24, 14]),
                dict(candidates=[8, 8]),
            ],
            "expected": [4, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()

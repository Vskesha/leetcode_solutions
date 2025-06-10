import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        return max(fr for fr in cnt.values() if fr % 2) - min(
            fr for fr in cnt.values() if fr % 2 == 0
        )


class Solution2:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        max_odd_freq = 0
        min_even_freq = len(s)
        for _, fr in cnt.items():
            if fr % 2:
                if fr > max_odd_freq:
                    max_odd_freq = fr
            elif fr < min_even_freq:
                min_even_freq = fr
        return max_odd_freq - min_even_freq


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxDifference"] * 2,
            "kwargs": [
                dict(s="aaaaabbc"),
                dict(s="abcabcab"),
            ],
            "expected": [3, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

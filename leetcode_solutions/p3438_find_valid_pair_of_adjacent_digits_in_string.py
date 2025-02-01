import unittest
from collections import Counter
from itertools import pairwise

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findValidPair(self, s: str) -> str:
        cnt = Counter(s)
        for a, b in pairwise(s):
            if a != b and cnt[a] == int(a) and cnt[b] == int(b):
                return a + b
        return ""


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findValidPair"] * 3,
            "kwargs": [
                dict(s="2523533"),
                dict(s="221"),
                dict(s="22"),
            ],
            "expected": ["23", "21", ""],
        },
    ]


if __name__ == "__main__":
    unittest.main()

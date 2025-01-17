import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return len(s) >= k and sum(v % 2 for v in Counter(s).values()) <= k


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["canConstruct"] * 3,
            "kwargs": [
                dict(s="annabelle", k=2),
                dict(s="leetcode", k=3),
                dict(s="true", k=4),
            ],
            "expected": [True, False, True],
        },
    ]


if __name__ == "__main__":
    unittest.main()

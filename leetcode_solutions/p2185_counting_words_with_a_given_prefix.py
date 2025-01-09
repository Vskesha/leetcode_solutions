import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(w.startswith(pref) for w in words)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["prefixCount"] * 2,
            "kwargs": [
                dict(words=["pay", "attention", "practice", "attend"], pref="at"),
                dict(words=["leetcode", "win", "loops", "success"], pref="code"),
            ],
            "expected": [2, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

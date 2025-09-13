import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxFreqSum(self, s: str) -> int:
        cnt = Counter(s)
        return max(
            (cnt.pop(ch) for ch in "aeiou" if ch in cnt),
            default=0
        ) + max(cnt.values(), default=0)

class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxFreqSum"] * 2,
            "kwargs": [
                dict(s = "successes"),
                dict(s = "aeiaeia"),
            ],
            "expected": [6, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()

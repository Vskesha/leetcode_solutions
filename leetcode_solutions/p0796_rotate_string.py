import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s * 2


class Solution2:
    def rotateString(self, s: str, goal: str) -> bool:
        if Counter(s) != Counter(goal):
            return False
        ls = len(s)
        for i in range(ls):
            if s[i:] + s[:i] == goal:
                return True
        return False


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["rotateString"] * 2,
            "kwargs": [
                dict(s="abcde", goal="cdeab"),
                dict(s="abcde", goal="abced"),
            ],
            "expected": [True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

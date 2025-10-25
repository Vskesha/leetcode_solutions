import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        lp = len(part)
        i = s.find(part)
        while i != -1:
            s = s[:i] + s[i + lp :]
            i = s.find(part)
        return s


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["removeOccurrences"] * 2,
            "kwargs": [
                dict(s="daabcbaabcbc", part="abc"),
                dict(s="axxxxyyyyb", part="xy"),
            ],
            "expected": ["dab", "ab"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        for i in range((len(s) + 1) // 2):
            if s[i] == s[~i]:
                return i
        return -1


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["firstMatchingIndex"] * 3,
            "kwargs": [
                dict(s="abcacbd"),
                dict(s="abc"),
                dict(s="abcdab"),
            ],
            "expected": [1, 1, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

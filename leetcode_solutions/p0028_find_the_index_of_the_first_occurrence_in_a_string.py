import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["strStr"] * 2,
            "kwargs": [
                dict(haystack = "sadbutsad", needle = "sad"),
                dict(haystack = "leetcode", needle = "leeto"),
            ],
            "expected": [0, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

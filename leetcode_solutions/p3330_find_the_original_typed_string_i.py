import unittest
from itertools import groupby

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 0
        for k, gr in groupby(word):
            ans += len(list(gr)) - 1
        return ans + 1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["possibleStringCount"] * 3,
            "kwargs": [
                dict(word="abbcccc"),
                dict(word="abcd"),
                dict(word="aaaa"),
            ],
            "expected": [5, 1, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()

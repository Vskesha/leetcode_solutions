import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i in range(len(words)) if x in words[i]]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findWordsContaining"] * 3,
            "kwargs": [
                dict(words=["leet", "code"], x="e"),
                dict(words=["abc", "bcd", "aaaa", "cbc"], x="a"),
                dict(words=["abc", "bcd", "aaaa", "cbc"], x="z"),
            ],
            "expected": [[0, 1], [0, 2], []],
            "assert_methods": ["assertListEqual"] * 3,
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return (
            len(word1) == len(word2)
            and set(word1) == set(word2)
            and Counter(Counter(word1).values()) == Counter(Counter(word2).values())
        )


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class":  Solution,
            "class_methods": ["closeStrings"] * 3,
            "kwargs": [
                dict(word1="abc", word2="bca"),
                dict(word1="a", word2="aa"),
                dict(word1="cabbba", word2="abbccc"),
            ],
            "expected": [True, False, True],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from itertools import combinations
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        return sum(
            w.startswith(ps) and w.endswith(ps) for ps, w in combinations(words, 2)
        )


class Solution2:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for j in range(1, len(words)):
            for i in range(j):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    ans += 1
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countPrefixSuffixPairs"] * 3,
            "kwargs": [
                dict(words=["a", "aba", "ababa", "aa"]),
                dict(words=["pa", "papa", "ma", "mama"]),
                dict(words=["abab", "ab"]),
            ],
            "expected": [4, 2, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

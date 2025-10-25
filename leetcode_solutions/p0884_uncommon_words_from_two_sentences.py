import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1, words2 = Counter(s1.split()), Counter(s2.split())

        uncommon = []
        for word, cnt in words1.items():
            if cnt == 1 and word not in words2:
                uncommon.append(word)
        for word, cnt in words2.items():
            if cnt == 1 and word not in words1:
                uncommon.append(word)

        return uncommon


class Solution2:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [
            word
            for word, cnt in Counter(s1.split() + s2.split()).items()
            if cnt == 1
        ]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["uncommonFromSentences"] * 2,
            "kwargs": [
                dict(s1="this apple is sweet", s2="this apple is sour"),
                dict(s1="apple apple", s2="banana"),
            ],
            "expected": [["sweet", "sour"], ["banana"]],
            "assert_methods": ["assertSameUncommon"] * 2,
        },
    ]

    def assertSameUncommon(self, actual: List[str], expected: List[str]):
        self.assertEqual(len(actual), len(expected))
        self.assertSetEqual(set(actual), set(expected))


if __name__ == "__main__":
    unittest.main()

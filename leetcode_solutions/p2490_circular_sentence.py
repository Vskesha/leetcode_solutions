import unittest
from itertools import pairwise

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        return sentence[0] == sentence[-1] and all(
            a[-1] == b[0] for a, b in pairwise(sentence.split())
        )


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["isCircularSentence"] * 3,
            "kwargs": [
                dict(sentence="leetcode exercises sound delightful"),
                dict(sentence="eetcode"),
                dict(sentence="Leetcode is cool"),
            ],
            "expected": [True, True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

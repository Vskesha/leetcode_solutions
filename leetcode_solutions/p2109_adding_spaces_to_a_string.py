import unittest
from itertools import pairwise
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        words = [s[: spaces[0]]]
        words.extend(s[i:j] for i, j in pairwise(spaces))
        words.append(s[spaces[-1] :])
        return " ".join(words)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["addSpaces"] * 3,
            "kwargs": [
                dict(s="LeetcodeHelpsMeLearn", spaces=[8, 13, 15]),
                dict(s="icodeinpython", spaces=[1, 5, 7, 9]),
                dict(s="spacing", spaces=[0, 1, 2, 3, 4, 5, 6]),
            ],
            "expected": [
                "Leetcode Helps Me Learn",
                "i code in py thon",
                " s p a c i n g",
            ],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count("U") == moves.count("D") and moves.count(
            "L"
        ) == moves.count("R")


class Solution2:
    def judgeCircle(self, moves: str) -> bool:
        cnt = Counter(moves)
        return cnt["L"] == cnt["R"] and cnt["U"] == cnt["D"]


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["judgeCircle"] * 2,
            "kwargs": [
                dict(moves="UD"),
                dict(moves="LL"),
            ],
            "expected": [True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

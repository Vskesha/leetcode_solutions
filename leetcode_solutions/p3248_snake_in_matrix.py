import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        cp = 0

        for c in commands:
            if c == "UP":
                cp -= n
            elif c == "RIGHT":
                cp += 1
            elif c == "DOWN":
                cp += n
            else:
                cp -= 1

        return cp


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["finalPositionOfSnake"] * 2,
            "kwargs": [
                dict(n=2, commands=["RIGHT", "DOWN"]),
                dict(n=3, commands=["DOWN", "RIGHT", "UP"]),
            ],
            "expected": [3, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

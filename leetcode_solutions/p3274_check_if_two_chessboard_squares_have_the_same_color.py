import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        return sum(ord(ch) for ch in coordinate1 + coordinate2) % 2 == 0


class Solution2:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        idx = ord(coordinate1[0]) + int(coordinate1[1])
        idx += ord(coordinate2[0]) + int(coordinate2[1])
        return idx % 2 == 0


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["checkTwoChessboards"] * 2,
            "kwargs": [
                dict(coordinate1="a1", coordinate2="c3"),
                dict(coordinate1="a1", coordinate2="h3"),
            ],
            "expected": [True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

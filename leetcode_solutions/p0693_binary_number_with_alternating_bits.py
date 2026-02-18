import unittest
from itertools import pairwise

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return all(a != b for a, b in pairwise(bin(n)[1:]))


class Solution2:
    def hasAlternatingBits(self, n: int) -> bool:
        for a, b in pairwise(bin(n)[1:]):
            if a == b:
                return False
        return True


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["hasAlternatingBits"] * 3,
            "kwargs": [
                dict(n=5),
                dict(n=7),
                dict(n=11),
            ],
            "expected": [True, False, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

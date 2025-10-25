import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        k = 1
        while True:
            x = num1 - num2 * k
            if x < k:
                return -1
            if k >= x.bit_count():
                return k
            k += 1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["makeTheIntegerZero"] * 2,
            "kwargs": [
                dict(num1=3, num2=-2),
                dict(num1=5, num2=7),
            ],
            "expected": [3, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n > 1:
            if n % 3:
                return False
            n //= 3
        return True


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["isPowerOfThree"] * 2,
            "kwargs": [
                dict(n=27),
                dict(n=0),
            ],
            "expected": [True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = list(map(int, s))
        while len(digits) > 2:
            for i in range(len(digits) - 1):
                digits[i] = (digits[i] + digits[i + 1]) % 10
            digits.pop()
        return digits[0] == digits[1]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["hasSameDigits"] * 2,
            "kwargs": [
                dict(s = "3902"),
                dict(s = "34789"),
            ],
            "expected": [True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

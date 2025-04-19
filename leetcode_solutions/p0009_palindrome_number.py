import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        snum = str(x)
        return snum == snum[::-1]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["isPalindrome"] * 3,
            "kwargs": [
                dict(x=121),
                dict(x=-121),
                dict(x=10),
            ],
            "expected": [True, False, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def canAliceWin(self, n: int) -> bool:
        curr = 10
        ans = False

        while n >= curr:
            n -= curr
            curr -= 1
            ans = not ans

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["canAliceWin"] * 2,
            "kwargs": [
                dict(n=12),
                dict(n=1),
            ],
            "expected": [True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

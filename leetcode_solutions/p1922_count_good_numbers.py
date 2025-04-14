import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        ans = pow(20, n // 2, mod)
        if n % 2:
            ans = ans * 5 % mod
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countGoodNumbers"] * 3,
            "kwargs": [
                dict(n=1),
                dict(n=4),
                dict(n=50),
            ],
            "expected": [5, 400, 564908303],
        },
    ]


if __name__ == "__main__":
    unittest.main()

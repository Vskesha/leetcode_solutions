import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = 0
        n -= 1
        pw = 1
        while n or x:
            if x % 2:
                ans += pw
            else:
                if n % 2:
                    ans += pw
                n //= 2
            x //= 2
            pw *= 2
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minEnd"] * 2,
            "kwargs": [
                dict(n=3, x=4),
                dict(n=2, x=7),
            ],
            "expected": [6, 15],
        },
    ]


if __name__ == "__main__":
    unittest.main()

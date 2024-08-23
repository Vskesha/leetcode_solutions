import unittest
from math import sqrt

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        ans = 0
        i = 2
        while i <= int(sqrt(n)):
            if n % i:
                i += 1
            else:
                n //= i
                ans += i
        return ans + n


class Solution1:
    def minSteps(self, n: int) -> int:
        ans = 0
        i = 2
        while i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                ans += i
        return ans


class Solution2:
    def minSteps(self, n: int) -> int:
        def get_first_prime(k):
            for i in range(2, int(sqrt(k)) + 1):
                if n % i == 0:
                    return i
            return n

        ans = 0
        while n > 1:
            pr = get_first_prime(n)
            n //= pr
            ans += pr

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minSteps"] * 2,
            "kwargs": [
                dict(n=3),
                dict(n=1),
            ],
            "expected": [3, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

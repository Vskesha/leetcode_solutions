import unittest
from functools import cache
from itertools import pairwise
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    mod = 10 ** 9 + 7
    f = [1] * 100001
    for i in range(1, 100001):
        f[i] = f[i - 1] * i % mod

    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        mod = 10 ** 9 + 7
        f = Solution.f
        tc = f[n - len(sick)] * pow(f[sick[0]], -1, mod) % mod

        for a, b in pairwise(sick):
            gh = b - a - 1
            if gh:
                tc = tc * pow(f[gh], -1, mod) * pow(2, gh - 1, mod) % mod

        return tc * pow(f[n - sick[-1] - 1], -1, mod) % mod


class Solution1:
    MOD = 10 ** 9 + 7

    @staticmethod
    @cache
    def factorial(n):
        if not n:
            return 1
        return Solution.factorial(n - 1) * n % Solution.MOD

    def numberOfSequence(self, n: int, sick: List[int]) -> int:

        tc = Solution.factorial(n - len(sick)) * pow(Solution.factorial(sick[0]), -1, Solution.MOD) % Solution.MOD

        for a, b in pairwise(sick):
            gh = b - a - 1
            if gh:
                tc = tc * pow(Solution.factorial(gh), -1, Solution.MOD) * pow(2, gh - 1, Solution.MOD) % Solution.MOD

        return tc * pow(Solution.factorial(n - sick[-1] - 1), -1, Solution.MOD) % Solution.MOD


class Solution2:
    MOD = 10 ** 9 + 7

    @staticmethod
    @cache
    def factorial(n):
        if not n:
            return 1
        return Solution.factorial(n - 1) * n % Solution.MOD

    def numberOfSequence(self, n: int, sick: List[int]) -> int:

        healthy = n - len(sick)
        tc = Solution.factorial(healthy)
        tc *= pow(Solution.factorial(sick[0]), -1, Solution.MOD)
        tc %= Solution.MOD

        for a, b in pairwise(sick):
            gh = b - a - 1
            if not gh:
                continue
            tc *= pow(Solution.factorial(gh), -1, Solution.MOD)
            tc %= Solution.MOD
            tc *= pow(2, gh - 1, Solution.MOD)
            tc %= Solution.MOD

        tc *= pow(Solution.factorial(n - sick[-1] - 1), -1, Solution.MOD)
        tc %= Solution.MOD

        return tc


class Solution3:
    MOD = 10 ** 9 + 7

    @staticmethod
    @cache
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        return n * Solution.factorial(n - 1) % Solution.MOD

    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        lengths = [sick[0], n - sick[-1] - 1]
        for a, b in pairwise(sick):
            length = b - a - 1
            if length > 0:
                lengths.append(length)

        res = Solution.factorial(sum(lengths))
        for i, x in enumerate(lengths):
            res *= pow(Solution.factorial(x), -1, Solution.MOD)
            res %= Solution.MOD

            # do not multiply by 2 for beginning and end
            if i >= 2:
                res *= pow(2, x - 1, Solution.MOD)
                res %= Solution.MOD

        return res


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["numberOfSequence"] * 4,
            "kwargs": [
                dict(n=5, sick=[0, 4]),
                dict(n=4, sick=[1]),
                dict(n=5, sick=[0, 1]),
                dict(n=100, sick=[0]),
            ],
            "expected": [4, 3, 1, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

# def test():
#     sol = Solution()
#
#     print('Test 1... ', end='')
#     assert sol.numberOfSequence(n=5, sick=[0, 4]) == 4
#     print('OK')
#
#     print('Test 2... ', end='')
#     assert sol.numberOfSequence(n=4, sick=[1]) == 3
#     print('OK')
#
#     print('Test 3... ', end='')
#     assert sol.numberOfSequence(n=5, sick=[0, 1]) == 1
#     print('OK')
#
#     print('Test 4... ', end='')
#     assert sol.numberOfSequence(n=100, sick=[0]) == 1
#     print('OK')


# if __name__ == '__main__':
#     test()

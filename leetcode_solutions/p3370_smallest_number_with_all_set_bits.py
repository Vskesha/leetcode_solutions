import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1 << (len(bin(n)) - 2)) - 1


class Solution2:
    def smallestNumber(self, n: int) -> int:
        b = 1
        ans = 0
        while n:
            ans += b
            b <<= 1
            n >>= 1
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["smallestNumber"] * 3,
            "kwargs": [
                dict(n=5),
                dict(n=10),
                dict(n=3),
            ],
            "expected": [7, 15, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()

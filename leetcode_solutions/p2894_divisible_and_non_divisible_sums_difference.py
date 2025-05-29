import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return n * (n + 1) // 2 - m * (k := n // m) * (k + 1)


class Solution2:
    def differenceOfSums(self, n: int, m: int) -> int:
        k = n // m
        return n * (n + 1) // 2 - m * k * (k + 1)


class Solution3:
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum(i if i % m else -i for i in range(1, n + 1))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["differenceOfSums"] * 3,
            "kwargs": [
                dict(n=10, m=3),
                dict(n=5, m=6),
                dict(n=5, m=1),
            ],
            "expected": [19, 15, -15],
        },
    ]


if __name__ == "__main__":
    unittest.main()

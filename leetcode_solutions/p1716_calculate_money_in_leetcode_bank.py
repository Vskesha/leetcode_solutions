import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def totalMoney(self, n: int) -> int:
        fw = n // 7
        d = n % 7

        return (7 * fw * (fw + 7) + (2 * fw + d + 1) * d) // 2


class Solution1:
    def totalMoney(self, n: int) -> int:
        w = n // 7
        return sum(28 + 7 * i for i in range(w)) + sum(
            w + i + 1 for i in range(n % 7)
        )


class Solution2:
    def totalMoney(self, n: int) -> int:
        ans = 0
        w = n // 7
        for i in range(w):
            ans += 28 + 7 * i
        for i in range(n % 7):
            ans += w + i + 1
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["totalMoney"] * 3,
            "kwargs": [
                dict(n=4),
                dict(n=10),
                dict(n=20),
            ],
            "expected": [10, 37, 96],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return ((n + 1) // 2) * (m // 2) + ((m + 1) // 2) * (n // 2)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["flowerGame"] * 2,
            "kwargs": [
                dict(n=3, m=2),
                dict(n=1, m=1),
            ],
            "expected": [3, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

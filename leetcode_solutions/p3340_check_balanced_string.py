import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def isBalanced(self, num: str) -> bool:
        return sum(map(int, num[::2])) == sum(map(int, num[1::2]))


class Solution2:
    def isBalanced(self, num: str) -> bool:
        return sum((-1) ** i * int(n) for i, n in enumerate(num)) == 0


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["isBalanced"] * 2,
            "kwargs": [
                dict(num="1234"),
                dict(num="24123"),
            ],
            "expected": [False, True],
        },
    ]


if __name__ == "__main__":
    unittest.main()

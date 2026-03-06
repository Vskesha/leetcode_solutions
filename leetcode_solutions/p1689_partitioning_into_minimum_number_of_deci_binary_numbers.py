import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minPartitions(self, n: str) -> int:
        for d in "987654321":
            if d in n:
                return int(d)
        return 0


class Solution2:
    def minPartitions(self, n: str) -> int:
        return int(max(n))


class Solution3:
    def minPartitions(self, n: str) -> int:
        return max(int(digit) for digit in n)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minPartitions"] * 3,
            "kwargs": [
                dict(n="32"),
                dict(n="82734"),
                dict(n="27346209830709182346"),
            ],
            "expected": [3, 8, 9],
        },
    ]


if __name__ == "__main__":
    unittest.main()

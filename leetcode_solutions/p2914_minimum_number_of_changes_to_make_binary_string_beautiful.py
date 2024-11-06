import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minChanges(self, s: str) -> int:
        return sum(s[i] != s[i + 1] for i in range(0, len(s), 2))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minChanges"] * 3,
            "kwargs": [
                dict(s="1001"),
                dict(s="10"),
                dict(s="0000"),
            ],
            "expected": [2, 1, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

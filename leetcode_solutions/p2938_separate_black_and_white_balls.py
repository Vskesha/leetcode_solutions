import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = ans = 0
        for ch in s:
            if ch == "1":
                ones += 1
            else:
                ans += ones
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimumSteps"] * 3,
            "kwargs": [
                dict(s="101"),
                dict(s="100"),
                dict(s="0111"),
            ],
            "expected": [1, 2, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

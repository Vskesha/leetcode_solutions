import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op = ans = 0
        for ch in s:
            if ch == "(":
                op += 1
            elif op:
                op -= 1
            else:
                ans += 1
        return ans + op


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minAddToMakeValid"] * 2,
            "kwargs": [
                dict(s="())"),
                dict(s="((("),
            ],
            "expected": [1, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()

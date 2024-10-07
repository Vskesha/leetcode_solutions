import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minLength(self, s: str) -> int:
        ans = ["$"]
        for ch in s:
            if ch == "B" and ans[-1] == "A" or ch == "D" and ans[-1] == "C":
                ans.pop()
            else:
                ans.append(ch)
        return len(ans) - 1


class Solution2:
    def minLength(self, s: str) -> int:
        ans = []
        for ch in s:
            if ch == "B" and ans and ans[-1] == "A":
                ans.pop()
            elif ch == "D" and ans and ans[-1] == "C":
                ans.pop()
            else:
                ans.append(ch)
        return len(ans)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minLength"] * 2,
            "kwargs": [
                dict(s="ABFCACDB"),
                dict(s="ACBBD"),
            ],
            "expected": [2, 5],
        },
    ]


if __name__ == "__main__":
    unittest.main()

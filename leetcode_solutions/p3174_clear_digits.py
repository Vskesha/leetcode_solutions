import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []
        for ch in s:
            if ch.isdigit():
                ans.pop()
            else:
                ans.append(ch)
        return "".join(ans)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["clearDigits"] * 2,
            "kwargs": [
                dict(s="abc"),
                dict(s="cb34"),
            ],
            "expected": ["abc", ""],
        },
    ]


if __name__ == "__main__":
    unittest.main()

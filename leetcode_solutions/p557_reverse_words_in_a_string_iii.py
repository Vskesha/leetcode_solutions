import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split())


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["reverseWords"] * 2,
            "kwargs": [
                dict(s="Let's take LeetCode contest"),
                dict(s="Mr Ding"),
            ],
            "expected": ["s'teL ekat edoCteeL tsetnoc", "rM gniD"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

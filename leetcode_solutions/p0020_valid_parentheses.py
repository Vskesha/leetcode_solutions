import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for ch in s:
            if ch in pairs:
                stack.append(ch)
            elif stack and ch == pairs[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack


class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            elif ch == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif ch == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif ch == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False

        return not stack


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["isValid"] * 4,
            "kwargs": [
                dict(s="()"),
                dict(s="()[]{}"),
                dict(s="(]"),
                dict(s="([])"),
            ],
            "expected": [True, True, False, True],
        },
    ]


if __name__ == "__main__":
    unittest.main()

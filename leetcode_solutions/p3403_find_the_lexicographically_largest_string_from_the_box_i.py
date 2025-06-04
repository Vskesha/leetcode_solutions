import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        k = len(word) - numFriends + 1
        return (
            max(word[i : i + k] for i in range(len(word))) if numFriends > 1 else word
        )


class Solution2:
    def answerString(self, word: str, numFriends: int) -> str:
        lw = len(word)
        ans = ""
        for i in range(lw):
            curr = word[i : i + lw + 1 - numFriends]
            if curr > ans:
                ans = curr
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["answerString"] * 3,
            "kwargs": [
                dict(word="dbca", numFriends=2),
                dict(word="gggg", numFriends=4),
                dict(word="gh", numFriends=1),
            ],
            "expected": ["dbc", "g", "gh"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

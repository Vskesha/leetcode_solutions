import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        return sum(not broken.intersection(word) for word in text.split())


class Solution2:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        broken = set(brokenLetters)

        for word in text.split():
            if not broken.intersection(word):
                ans += 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["canBeTypedWords"] * 3,
            "kwargs": [
                dict(text="hello world", brokenLetters="ad"),
                dict(text="leet code", brokenLetters="lt"),
                dict(text="leet code", brokenLetters="e"),
            ],
            "expected": [1, 1, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

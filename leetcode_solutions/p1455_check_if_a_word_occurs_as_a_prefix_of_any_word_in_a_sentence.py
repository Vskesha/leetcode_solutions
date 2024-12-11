import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split(), 1):
            if word.startswith(searchWord):
                return i
        return -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["isPrefixOfWord"] * 3,
            "kwargs": [
                dict(sentence="i love eating burger", searchWord="burg"),
                dict(sentence="this problem is an easy problem", searchWord="pro"),
                dict(sentence="i am tired", searchWord="you"),
            ],
            "expected": [4, 2, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()

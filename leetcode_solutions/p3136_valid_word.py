import string
import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False

        for c in word:
            if c.isalpha():
                if c.lower() in "aeiou":
                    has_vowel = True
                else:
                    has_consonant = True
            elif not c.isdigit():
                return False

        return has_vowel and has_consonant


class Solution2:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        allowed = set(
            string.ascii_lowercase + string.ascii_uppercase + string.digits
        )
        vowels = "aeiou"
        has_vowel = False
        has_consonant = False

        for ch in word:
            if ch not in allowed:
                return False
            if ch.lower() in vowels:
                has_vowel = True
            elif not ch.isnumeric():
                has_consonant = True

        return has_vowel and has_consonant


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["isValid"] * 3,
            "kwargs": [
                dict(word="234Adas"),
                dict(word="b3"),
                dict(word="a3$e"),
            ],
            "expected": [True, False, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

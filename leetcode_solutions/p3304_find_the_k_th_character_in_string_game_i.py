import unittest
from string import ascii_lowercase

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def kthCharacter(self, k: int) -> str:
        return chr((k - 1).bit_count() + 97)


class Solution1:
    def kthCharacter(self, k: int) -> str:
        return ascii_lowercase[(k - 1).bit_count()]


class Solution2:
    def kthCharacter(self, k: int) -> str:
        mp = {chr(i + 97): chr((i + 1) % 26 + 97) for i in range(26)}
        word = "a"
        while len(word) < k:
            word += "".join(mp[ch] for ch in word)
        return word[k - 1]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["kthCharacter"] * 2,
            "kwargs": [
                dict(k=5),
                dict(k=10),
            ],
            "expected": ["b", "c"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

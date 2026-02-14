import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        ls2 = len(str2)
        nxt = {chr(i + 97): chr((i + 1) % 26 + 97) for i in range(26)}
        i = 0

        for ch in str1:
            if ch == str2[i] or nxt[ch] == str2[i]:
                i += 1
                if i == ls2:
                    return True

        return False


class Solution1:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        ls2 = len(str2)
        str2 += "$"
        nxt = {chr(i + 97): chr((i + 1) % 26 + 97) for i in range(26)}
        i = 0

        for ch in str1:
            if ch == str2[i] or nxt[ch] == str2[i]:
                i += 1

        return i == ls2


class Solution2:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        ls2 = len(str2)
        i = 0

        for ch in str1:
            if ch == str2[i] or chr((ord(ch) - 96) % 26 + 97) == str2[i]:
                i += 1
                if i == ls2:
                    return True

        return False


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["canMakeSubsequence"] * 3,
            "kwargs": [
                dict(str1="abc", str2="ad"),
                dict(str1="zc", str2="ad"),
                dict(str1="ab", str2="d"),
            ],
            "expected": [True, True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

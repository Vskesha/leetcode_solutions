import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        ln1, ln2 = len(word1), len(word2)
        mp = [-1] * ln2
        j = ln1 - 1
        for i in range(ln2 - 1, -1, -1):
            while j >= 0 and word1[j] != word2[i]:
                j -= 1
            mp[i] = j
            j -= 1
        mp.append(ln1)
        used = False
        ans = []
        j = 0
        for i, ch in enumerate(word2):
            if j >= ln1:
                return []
            elif word1[j] == ch:
                ans.append(j)
                j += 1
            elif used or mp[i + 1] <= j:
                while j < ln1 and word1[j] != ch:
                    j += 1
                ans.append(j)
                j += 1
            elif mp[i + 1] > j:
                ans.append(j)
                j += 1
                used = True
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["validSequence"] * 5,
            "kwargs": [
                dict(word1="vbcca", word2="abc"),
                dict(word1="bacdc", word2="abc"),
                dict(word1="aaaaaa", word2="aaabc"),
                dict(word1="abc", word2="ab"),
                dict(word1="bbeigiibhjafjig", word2="iihhj"),
            ],
            "expected": [
                [0, 1, 2],
                [1, 2, 4],
                [],
                [0, 1],
                [3, 5, 6, 8, 9],
            ],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = {}

        for word in words:
            curr = trie
            for ch in word:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]
                curr["cnt"] = curr.get("cnt", 0) + 1

        ans = []
        for word in words:
            curr = trie
            ans.append(0)
            for ch in word:
                curr = curr[ch]
                ans[-1] += curr["cnt"]

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["sumPrefixScores"] * 2,
            "kwargs": [
                dict(words = ["abc","ab","bc","b"]),
                dict(words = ["abcd"]),
            ],
            "expected": [[5,4,3,2], [4]],
            "assert_methods": ["assertListEqual"],
        },
    ]


if __name__ == '__main__':
    unittest.main()

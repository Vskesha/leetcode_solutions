import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = {}

        def insert(num):
            curr = trie
            for d in str(num):
                if d not in curr:
                    curr[d] = {}
                curr = curr[d]

        def pref_len(num):
            curr = trie
            cnt = 0
            for d in str(num):
                if d not in curr:
                    break
                curr = curr[d]
                cnt += 1
            return cnt

        for num in arr1:
            insert(num)

        ans = 0
        for num in arr2:
            ans = max(ans, pref_len(num))

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["longestCommonPrefix"] * 2,
            "kwargs": [
                dict(arr1=[1, 10, 100], arr2=[1000]),
                dict(arr1=[1, 2, 3], arr2=[4, 4, 4]),
            ],
            "expected": [3, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()

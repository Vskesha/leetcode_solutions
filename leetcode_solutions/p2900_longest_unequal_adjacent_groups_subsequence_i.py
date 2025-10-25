import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def getLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        result, prev = [], -1

        for i, gr in enumerate(groups):
            if gr != prev:
                result.append(words[i])
                prev = gr

        return result


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["getLongestSubsequence"] * 2,
            "kwargs": [
                dict(words=["e", "a", "b"], groups=[0, 0, 1]),
                dict(words=["a", "b", "c", "d"], groups=[1, 0, 1, 1]),
            ],
            "expected": [["e", "b"], ["a", "b", "c"]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

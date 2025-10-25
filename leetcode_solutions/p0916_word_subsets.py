import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        setb = Counter()
        for w in words2:
            for ch, val in Counter(w).items():
                setb[ch] = max(setb[ch], val)

        ans = []
        for w in words1:
            wc = Counter(w)
            for ch, val in setb.items():
                if wc[ch] < val:
                    break
            else:
                ans.append(w)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["wordSubsets"] * 2,
            "kwargs": [
                dict(
                    words1=[
                        "amazon",
                        "apple",
                        "facebook",
                        "google",
                        "leetcode",
                    ],
                    words2=["e", "o"],
                ),
                dict(
                    words1=[
                        "amazon",
                        "apple",
                        "facebook",
                        "google",
                        "leetcode",
                    ],
                    words2=["l", "e"],
                ),
            ],
            "expected": [
                ["facebook", "google", "leetcode"],
                ["apple", "google", "leetcode"],
            ],
            "assert_methods": ["assertSameUniversal"] * 2,
        },
    ]

    def assertSameUniversal(self, result: List[str], expected: List[str]):
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == "__main__":
    unittest.main()

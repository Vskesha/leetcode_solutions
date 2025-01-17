import unittest
from itertools import accumulate
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        tot = 0
        ans = []
        for a, b in zip(A, B):
            if a in seen:
                tot += 1
            else:
                seen.add(a)
            if b in seen:
                tot += 1
            else:
                seen.add(b)
            ans.append(tot)

        return ans


class Solution2:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()

        def add(n):
            ans = n in seen
            seen.add(n)
            return ans

        return list(accumulate(add(a) + add(b) for a, b in zip(A, B)))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findThePrefixCommonArray"] * 2,
            "kwargs": [
                dict(A=[1, 3, 2, 4], B=[3, 1, 2, 4]),
                dict(A=[2, 3, 1], B=[3, 1, 2]),
            ],
            "expected": [[0, 2, 3, 4], [0, 1, 3]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from collections import Counter
from itertools import permutations
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cnt = Counter(nums)

        def dfs(perm, last):
            keys = sorted(cnt.keys())

            if len(keys) == 1:
                key = keys[0]
                ans.append(perm + [key] * cnt[key])
                return

            for key in keys:
                if key == last:
                    continue

                amount = cnt[key]
                perm.extend([key] * amount)
                del cnt[key]

                for _ in range(amount):
                    dfs(perm, key)
                    perm.pop()
                    cnt[key] += 1

        dfs([], inf)
        return ans


class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return [list(p) for p in set(permutations(nums))]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["permuteUnique"] * 2,
            "kwargs": [
                dict(nums=[1, 1, 2]),
                dict(nums=[1, 2, 3]),
            ],
            "expected": [
                [[1, 1, 2], [1, 2, 1], [2, 1, 1]],
                [
                    [1, 2, 3],
                    [1, 3, 2],
                    [2, 1, 3],
                    [2, 3, 1],
                    [3, 1, 2],
                    [3, 2, 1],
                ],
            ],
            "assert_methods": ["assertSamePermutations"],
        },
    ]

    def assertSamePermutations(self, actual, expected):
        self.assertEqual(len(actual), len(expected))
        actual_set = set(map(tuple, actual))
        expected_set = set(map(tuple, expected))
        self.assertEqual(actual_set, expected_set)


if __name__ == "__main__":
    unittest.main()

import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findKDistantIndices(
        self, nums: List[int], key: int, k: int
    ) -> List[int]:
        j = 0
        ans = []
        ln = len(nums)

        for i, n in enumerate(nums):
            if n == key:
                for j in range(max(j, i - k), min(ln, i + k + 1)):
                    ans.append(j)
                j += 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findKDistantIndices"] * 2,
            "kwargs": [
                dict(nums=[3, 4, 9, 1, 3, 9, 5], key=9, k=1),
                dict(nums=[2, 2, 2, 2, 2], key=2, k=2),
            ],
            "expected": [
                [1, 2, 3, 4, 5, 6],
                [0, 1, 2, 3, 4],
            ],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

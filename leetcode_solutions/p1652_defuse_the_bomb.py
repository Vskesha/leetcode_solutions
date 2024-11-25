import unittest
from itertools import accumulate
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n

        if not k:
            return ans

        acc = list(accumulate(code * 3, initial=0))

        if k > 0:
            for i, j in zip(range(n), range(n + 1, 3 * n)):
                ans[i] = acc[j + k] - acc[j]
        else:
            for i, j in zip(range(n), range(n, 2 * n)):
                ans[i] = acc[j] - acc[j + k]

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["decrypt"] * 3,
            "kwargs": [
                dict(code=[5, 7, 1, 4], k=3),
                dict(code=[1, 2, 3, 4], k=0),
                dict(code=[2, 4, 9, 3], k=-2),
            ],
            "expected": [
                [12, 10, 16, 13],
                [0, 0, 0, 0],
                [12, 5, 6, 13],
            ],
            "assert_methods": ["assertListEqual"] * 3,
        },
    ]


if __name__ == "__main__":
    unittest.main()

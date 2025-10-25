import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def construct2DArray(
        self, original: List[int], m: int, n: int
    ) -> List[List[int]]:
        lo = len(original)

        if m * n != lo:
            return []

        ans = []
        for i in range(0, lo, n):
            ans.append(original[i : i + n])

        return ans


class Solution2:
    def construct2DArray(
        self, original: List[int], m: int, n: int
    ) -> List[List[int]]:
        lo = len(original)

        if m * n != lo:
            return []

        ans = [[0] * n for _ in range(m)]

        for i, v in enumerate(original):
            ans[i // n][i % n] = v

        return ans


class Solution3:
    def construct2DArray(
        self, original: List[int], m: int, n: int
    ) -> List[List[int]]:
        lo = len(original)

        if m * n != lo:
            return []

        ans = []
        for i in range(0, lo, n):
            row = []
            for j in range(i, i + n):
                row.append(original[j])
            ans.append(row)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["construct2DArray"] * 3,
            "kwargs": [
                dict(original=[1, 2, 3, 4], m=2, n=2),
                dict(original=[1, 2, 3], m=1, n=3),
                dict(original=[1, 2], m=1, n=1),
            ],
            "expected": [[[1, 2], [3, 4]], [[1, 2, 3]], []],
            "assert_methods": ["assertListEqual"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

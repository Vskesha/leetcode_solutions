import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        crow = []
        ans = 0

        for row in matrix:
            seen = [False] * n
            nrow = []
            width = 0

            for height, j in crow:
                seen[j] = True
                if not row[j]:
                    continue
                height += 1
                width += 1
                nrow.append((height, j))
                ans = max(ans, height * width)

            for j in range(n):
                if not seen[j] and row[j]:
                    width += 1
                    nrow.append((1, j))
                    ans = max(ans, width)

            crow = nrow

        return ans


class Solution2:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        prev = matrix[0]
        m = len(prev)
        n = len(matrix)

        for i in range(1, n):
            row = matrix[i]
            for j in range(m):
                if row[j]:
                    row[j] += prev[j]
            prev = row

        ans = 0
        for row in matrix:
            row.sort(reverse=True)
            for i, n in enumerate(row, 1):
                ans = max(ans, i * n)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["largestSubmatrix"] * 3,
            "kwargs": [
                dict(matrix=[[0, 0, 1], [1, 1, 1], [1, 0, 1]]),
                dict(matrix=[[1, 0, 1, 0, 1]]),
                dict(matrix=[[1, 1, 0], [1, 0, 1]]),
            ],
            "expected": [4, 3, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()

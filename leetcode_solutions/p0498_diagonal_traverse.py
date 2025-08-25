import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        rev = True
        ans = []
        for d in range(m + n - 1):
            if rev:
                for i in range(min(d, m - 1), max(-1, d - n), -1):
                    ans.append(mat[i][d - i])
            else:
                for i in range(max(0, d - n + 1), min(d + 1, m)):
                    ans.append(mat[i][d - i])
            rev = not rev
        return ans


class Solution2:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        rev = True
        ans = []
        for d in range(m + n - 1):
            dia = []
            for i in range(max(0, d - n + 1), min(d + 1, m)):
                dia.append(mat[i][d - i])
            if rev:
                dia = dia[::-1]
            ans.extend(dia)
            rev = not rev
        return ans


class Solution3:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        rev = True
        ans = []
        for d in range(m + n - 1):
            dia = []
            for i in range(min(d + 1, m)):
                j = d - i
                if j >= n:
                    continue
                dia.append(mat[i][j])
            if rev:
                dia = dia[::-1]
            ans.extend(dia)
            rev = not rev
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findDiagonalOrder"] * 2,
            "kwargs": [
                dict(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                dict(mat=[[1, 2], [3, 4]]),
            ],
            "expected": [[1, 2, 4, 7, 5, 3, 6, 8, 9], [1, 2, 3, 4]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

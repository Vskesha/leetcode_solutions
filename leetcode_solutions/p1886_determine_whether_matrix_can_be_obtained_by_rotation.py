import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def findRotation(
        self, mat: List[List[int]], target: List[List[int]]
    ) -> bool:
        for _ in range(4):
            if all(row1 == row2 for row1, row2 in zip(mat, target)):
                return True
            mat = [list(rc) for rc in zip(*mat[::-1])]

        return False


class Solution2:
    def findRotation(
        self, mat: List[List[int]], target: List[List[int]]
    ) -> bool:
        cnt1 = Counter(val for row in mat for val in row)
        cnt2 = Counter(val for row in mat for val in row)

        if cnt1 != cnt2:
            return False

        if all(row1 == row2 for row1, row2 in zip(mat, target)):
            return True

        for _ in range(3):
            mat = [list(rc) for rc in zip(*mat[::-1])]
            if all(row1 == row2 for row1, row2 in zip(mat, target)):
                return True

        return False


class Solution3:
    def findRotation(
        self, mat: List[List[int]], target: List[List[int]]
    ) -> bool:
        n = len(mat)

        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]:
                    break
            else:
                continue
            break
        else:
            return True

        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[j][n - i - 1]:
                    break
            else:
                continue
            break
        else:
            return True

        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[n - i - 1][n - j - 1]:
                    break
            else:
                continue
            break
        else:
            return True

        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[n - j - 1][i]:
                    break
            else:
                continue
            break
        else:
            return True

        return False


class Solution4:
    def findRotation(
        self, mat: List[List[int]], target: List[List[int]]
    ) -> bool:
        n = len(mat)

        cnt1 = Counter(val for row in mat for val in row)
        cnt2 = Counter(val for row in mat for val in row)

        if cnt1 != cnt2:
            return False

        if all(row1 == row2 for row1, row2 in zip(mat, target)):
            return True

        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[j][n - i - 1]:
                    break
            else:
                continue
            break
        else:
            return True

        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[n - i - 1][n - j - 1]:
                    break
            else:
                continue
            break
        else:
            return True

        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[n - j - 1][i]:
                    break
            else:
                continue
            break
        else:
            return True

        return False


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findRotation"] * 3,
            "kwargs": [
                dict(mat=[[0, 1], [1, 0]], target=[[1, 0], [0, 1]]),
                dict(mat=[[0, 1], [1, 1]], target=[[1, 0], [0, 1]]),
                dict(
                    mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]],
                    target=[[1, 1, 1], [0, 1, 0], [0, 0, 0]],
                ),
            ],
            "expected": [True, False, True],
        },
    ]


if __name__ == "__main__":
    unittest.main()

import unittest
from heapq import heappush, heappushpop
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        ans = -inf
        values = []
        for i in range(m):
            heap = []
            for j in range(3):
                heappush(heap, (board[i][j], i, j))
            for j in range(3, n):
                heappushpop(heap, (board[i][j], i, j))
            values.extend(heap)
        values.sort(reverse=True)

        for vx, ix, jx in values:
            biggest_four = []
            for value in values:
                if value[1] != ix and value[2] != jx:
                    biggest_four.append(value)
                    if len(biggest_four) == 4:
                        break
            for y in range(1, 4):
                vy, iy, jy = biggest_four[y]
                for z in range(y):
                    vz, iz, jz = biggest_four[z]
                    if iy != iz and jy != jz:
                        ans = max(ans, vx + vy + vz)

        return ans


class Solution1:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        m_n, mn = m + n, m * n
        vals = [(board[i][j], i, j) for i in range(m) for j in range(n)]
        vals.sort(reverse=True)
        ans = -inf

        for x in range(m_n):
            vx, ix, jx = vals[x]
            for y in range(x + 1, m_n):
                vy, iy, jy = vals[y]
                if ix != iy and jx != jy:
                    for vz, iz, jz in vals:
                        if iz != ix and iz != iy and jz != jx and jz != jy:
                            ans = max(ans, vx + vy + vz)
                            break
        return ans


class Solution2:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        m_n, mn = m + n, m * n
        vals = sorted(
            [(board[i][j], i, j) for i in range(m) for j in range(n)],
            reverse=True,
        )
        ans = -inf

        for x in range(m_n):
            v1, i1, j1 = vals[x]
            for y in range(x + 1, min(m_n + x + 1, mn)):
                v2, i2, j2 = vals[y]
                if i1 == i2 or j1 == j2:
                    continue
                z = y + 1
                i12, j12 = {i1, i2}, {j1, j2}
                while z < mn and (vals[z][1] in i12 or vals[z][2] in j12):
                    z += 1
                if z != mn:
                    ans = max(ans, v1 + v2 + vals[z][0])

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumValueSum"] * 3,
            "kwargs": [
                dict(board=[[-3, 1, 1, 1], [-3, 1, -3, 1], [-3, 2, 1, 1]]),
                dict(board=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                dict(board=[[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
            ],
            "expected": [4, 15, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()

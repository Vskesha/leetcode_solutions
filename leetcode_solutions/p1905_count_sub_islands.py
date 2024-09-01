import unittest
from collections import deque
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid2), len(grid2[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    grid2[i][j] = 0
                    que = deque([(i, j)])
                    is_sub = True
                    while que:
                        ci, cj = que.popleft()
                        if not grid1[ci][cj]:
                            is_sub = False
                        for ni, nj in (
                            (ci - 1, cj),
                            (ci, cj + 1),
                            (ci + 1, cj),
                            (ci, cj - 1),
                        ):
                            if 0 <= ni < m and 0 <= nj < n and grid2[ni][nj]:
                                que.append((ni, nj))
                                grid2[ni][nj] = 0
                    if is_sub:
                        ans += 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countSubIslands"] * 2,
            "kwargs": [
                dict(grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]),
                dict(grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]),
            ],
            "expected": [3, 2],
        },
    ]


if __name__ == '__main__':
    unittest.main()


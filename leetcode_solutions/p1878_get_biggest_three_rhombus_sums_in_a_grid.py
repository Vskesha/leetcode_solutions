import unittest
from heapq import heappop, heappushpop
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        top_left = [row.copy() for row in grid]
        top_right = [row.copy() for row in grid]

        for i in range(1, m):
            for j in range(1, n):
                top_left[i][j] += top_left[i - 1][j - 1]
            for j in range(0, n - 1):
                top_right[i][j] += top_right[i - 1][j + 1]

        ans = [0, 0, 0]
        for i in range(m):
            for j in range(n):
                if grid[i][j] not in ans:
                    heappushpop(ans, grid[i][j])
                for sz in range(1, min(i // 2 + 1, j + 1, n - j)):
                    mi = i - sz
                    ti = mi - sz
                    bl = top_left[i][j] - top_left[mi][j - sz]
                    br = top_right[i][j] - top_right[mi][j + sz]
                    tr = top_left[mi][j + sz] - top_left[ti][j]
                    tl = top_right[mi][j - sz] - top_right[ti][j]
                    rsum = bl + br + tr + tl + grid[ti][j] - grid[i][j]
                    if rsum not in ans:
                        heappushpop(ans, rsum)

        while not ans[0]:
            heappop(ans)

        return sorted(ans, reverse=True)


class Solution2:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        top_left = [row.copy() for row in grid]
        top_right = [row.copy() for row in grid]

        for i in range(1, m):
            for j in range(1, n):
                top_left[i][j] += top_left[i - 1][j - 1]
            for j in range(0, n - 1):
                top_right[i][j] += top_right[i - 1][j + 1]

        ans = []
        for i in range(m):
            for j in range(n):
                ans.append(grid[i][j])
                max_size = min(i // 2, j, n - j - 1)
                for sz in range(1, max_size + 1):
                    mi = i - sz
                    ti = mi - sz
                    bl = top_left[i][j] - top_left[mi][j - sz]
                    br = top_right[i][j] - top_right[mi][j + sz]
                    tr = top_left[mi][j + sz] - top_left[ti][j]
                    tl = top_right[mi][j - sz] - top_right[ti][j]
                    rsum = bl + br + tr + tl + grid[ti][j] - grid[i][j]
                    ans.append(rsum)

        ans = sorted(set(ans), reverse=True)[:3]
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["getBiggestThree"] * 3,
            "kwargs": [
                dict(
                    grid=[
                        [3, 4, 5, 1, 3],
                        [3, 3, 4, 2, 3],
                        [20, 30, 200, 40, 10],
                        [1, 5, 5, 4, 1],
                        [4, 3, 2, 2, 5],
                    ]
                ),
                dict(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                dict(grid=[[7, 7, 7]]),
            ],
            "expected": [[228, 216, 211], [20, 9, 8], [7]],
            "assert_methods": ["assertListEqual"] * 3,
        },
    ]


if __name__ == "__main__":
    unittest.main()

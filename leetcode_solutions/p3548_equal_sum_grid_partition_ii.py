import unittest
from collections import Counter
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        cnt = Counter(val for row in grid for val in row)
        total = sum(val for row in grid for val in row)

        if m == 1 or n == 1:
            row = [val for row in grid for val in row]
            rsum = 0
            for i in range(len(row) - 1):
                rsum += row[i]
                diff = rsum + rsum - total
                if not diff:
                    return True
                elif diff > 0:
                    if diff == row[0] or diff == row[i]:
                        return True
                elif diff < 0:
                    diff = -diff
                    if diff == row[i + 1] or diff == row[-1]:
                        return True
            return False

        rsum = 0
        rcnt = Counter()

        for i in range(m - 1):
            rsum += sum(grid[i])
            rcnt.update(grid[i])
            diff = rsum + rsum - total
            if not diff:
                return True
            elif diff > 0:
                if i > 0 and rcnt[diff] > 0:
                    return True
                elif i == 0 and (diff == grid[0][0] or diff == grid[0][-1]):
                    return True
            elif diff < 0:
                diff = -diff
                if i < m - 2 and cnt[diff] - rcnt[diff] > 0:
                    return True
                elif i == m - 2 and (
                    diff == grid[-1][0] or diff == grid[-1][-1]
                ):
                    return True

        csum = 0
        ccnt = Counter()
        for j in range(n - 1):
            col = [row[j] for row in grid]
            csum += sum(col)
            ccnt.update(col)
            diff = csum + csum - total
            if not diff:
                return True
            elif diff > 0:
                if j > 0 and ccnt[diff] > 0:
                    return True
                elif j == 0 and (diff == grid[0][0] or diff == grid[-1][0]):
                    return True
            elif diff < 0:
                diff = -diff
                if j < n - 2 and cnt[diff] - ccnt[diff] > 0:
                    return True
                elif j == n - 2 and (
                    diff == grid[0][-1] or diff == grid[-1][-1]
                ):
                    return True

        return False


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["canPartitionGrid"] * 5,
            "kwargs": [
                dict(grid=[[1, 4], [2, 3]]),
                dict(grid=[[1, 2], [3, 4]]),
                dict(grid=[[1, 2, 4], [2, 3, 5]]),
                dict(grid=[[253, 10, 10]]),
                dict(grid=[[10, 5, 4, 5]]),
            ],
            "expected": [True, True, False, True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()

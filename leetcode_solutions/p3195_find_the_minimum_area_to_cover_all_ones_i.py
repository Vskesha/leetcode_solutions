import unittest
from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        l, r, t, b = 0, len(grid[0]) - 1, 0, len(grid) - 1

        while 1 not in grid[t]:
            t += 1
        while 1 not in grid[b]:
            b -= 1
        while 1 not in [grid[i][l] for i in range(t, b + 1)]:
            l += 1
        while 1 not in [grid[i][r] for i in range(t, b + 1)]:
            r -= 1

        return (r - l + 1) * (b - t + 1)


class Solution2:
    def minimumArea(self, grid: List[List[int]]) -> int:
        left, right, top, bottom = 0, 0, 0, 0

        m, n = len(grid), len(grid[0])

        for i in range(m):
            if 1 in grid[i]:
                top = i
                break

        for i in range(m - 1, -1, -1):
            if 1 in grid[i]:
                bottom = i + 1
                break

        for j in range(n):
            if 1 in [row[j] for row in grid]:
                left = j
                break

        for j in range(n - 1, -1, -1):
            if 1 in [row[j] for row in grid]:
                right = j + 1
                break

        return (right - left) * (bottom - top)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_minimum_area_1(self):
        print("Test minimumArea 1 ... ", end="")
        self.assertEqual(self.sol.minimumArea(grid=[[0, 1, 0], [1, 0, 1]]), 6)
        print("OK")

    def test_minimum_area_2(self):
        print("Test minimumArea 2 ... ", end="")
        self.assertEqual(self.sol.minimumArea(grid=[[1, 0], [0, 0]]), 1)
        print("OK")


if __name__ == "__main__":
    unittest.main()

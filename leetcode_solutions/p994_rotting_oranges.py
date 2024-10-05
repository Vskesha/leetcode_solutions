import unittest
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        bfs = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    bfs.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if not fresh:
            return 0
        time = 0
        while bfs:
            for _ in range(len(bfs)):
                i, j = bfs.popleft()
                for ni, nj in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        bfs.append((ni, nj))
                        fresh -= 1
                        if not fresh:
                            return time + 1
            time += 1
        return -1


class Solution1:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)

        for i in range(n):
            if 1 in grid[i]:
                break
        else:
            return 0

        dist = 0
        deq = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    deq.append((i, j, 0))

        while len(deq) > 0:
            i, j, dist = deq.popleft()
            if i and grid[i - 1][j] == 1:  # top
                grid[i - 1][j] = 3
                deq.append((i - 1, j, dist + 1))
            if j and grid[i][j - 1] == 1:  # left
                grid[i][j - 1] = 3
                deq.append((i, j - 1, dist + 1))
            if i < n - 1 and grid[i + 1][j] == 1:  # bottom
                grid[i + 1][j] = 3
                deq.append((i + 1, j, dist + 1))
            if j < m - 1 and grid[i][j + 1] == 1:  # right
                grid[i][j + 1] = 3
                deq.append((i, j + 1, dist + 1))

        for i in range(n):
            if 1 in grid[i]:
                return -1

        return dist


class Solution2:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def traverse(i, j, dist=0):
            aux[i][j] = dist
            if i > 0 and grid[i - 1][j] == 1 and aux[i - 1][j] > dist + 1:
                traverse(i - 1, j, dist + 1)
            if j > 0 and grid[i][j - 1] == 1 and aux[i][j - 1] > dist + 1:
                traverse(i, j - 1, dist + 1)
            if j < m - 1 and grid[i][j + 1] == 1 and aux[i][j + 1] > dist + 1:
                traverse(i, j + 1, dist + 1)
            if i < n - 1 and grid[i + 1][j] == 1 and aux[i + 1][j] > dist + 1:
                traverse(i + 1, j, dist + 1)

        m = len(grid[0])
        n = len(grid)
        aux = [[100] * m for _ in range(n)]
        rotten = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 2]
        for coords in rotten:
            traverse(*coords)

        max_dist = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and max_dist < aux[i][j]:
                    max_dist = aux[i][j]
        return max_dist if max_dist < 100 else -1


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_oranges_rotting_1(self):
        print("Test orangesRotting 1... ", end="")
        self.assertEqual(
            self.sol.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]), 4
        )
        print("OK")

    def test_oranges_rotting_2(self):
        print("Test orangesRotting 2... ", end="")
        self.assertEqual(
            self.sol.orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]), -1
        )
        print("OK")

    def test_oranges_rotting_3(self):
        print("Test orangesRotting 3... ", end="")
        self.assertEqual(self.sol.orangesRotting(grid=[[0, 2]]), 0)
        print("OK")

    def test_oranges_rotting_4(self):
        print("Test orangesRotting 4... ", end="")
        self.assertEqual(self.sol.orangesRotting(grid=[[0, 1]]), -1)
        print("OK")

    def test_oranges_rotting_5(self):
        print("Test orangesRotting 5... ", end="")
        self.assertEqual(
            self.sol.orangesRotting(
                grid=[
                    [2, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                ]
            ),
            58,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

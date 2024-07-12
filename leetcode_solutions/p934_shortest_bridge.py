import unittest
from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fi = 0
        while 1 not in grid[fi]:
            fi += 1
        fj = grid[fi].index(1)
        grid[fi][fj] = 2

        bfs, qi = [(fi, fj)], 0
        while qi < len(bfs):
            i, j = bfs[qi]
            for y, x in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
                if 0 <= y < m and 0 <= x < n and grid[y][x] == 1:
                    bfs.append((y, x))
                    grid[y][x] = 2
            qi += 1

        bfs, qi = deque(bfs), 0
        while bfs:
            for _ in range(len(bfs)):
                i, j = bfs.popleft()
                for y, x in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
                    if 0 <= y < m and 0 <= x < n and grid[y][x] != 2:
                        if not grid[y][x]:
                            bfs.append((y, x))
                            grid[y][x] = 2
                        else:
                            return qi
            qi += 1
        return -1


class Solution2:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island = deque()
        dfs = deque()
        i = j = 0

        # locate cell of first island
        while i < n:
            j = 0
            while j < n:
                if grid[i][j]:
                    island.append((i, j, 0))
                    dfs.append((i, j))
                    grid[i][j] = 2
                    i = j = n
                else:
                    grid[i][j] = 3
                j += 1
            i += 1

        # add all cells of first island to the queue
        while dfs:
            i, j = dfs.popleft()

            for y, x in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                if 0 <= x < n and 0 <= y < n and grid[y][x] == 1:
                    grid[y][x] = 2
                    dfs.append((y, x))
                    island.append((y, x, 0))

        # traverse through empty fields with keeping distance
        while island:
            i, j, dist = island.popleft()

            for y, x in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                if 0 <= x < n and 0 <= y < n:
                    if grid[y][x] == 1:
                        return dist
                    elif grid[y][x] == 0:
                        grid[y][x] = 2
                        island.append((y, x, dist + 1))


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_shortest_bridge_1(self):
        print("Test shortestBridge 1... ", end="")
        self.assertEqual(self.sol.shortestBridge(grid=[[0, 1], [1, 0]]), 1)
        print("OK")

    def test_shortest_bridge_2(self):
        print("Test shortestBridge 2... ", end="")
        self.assertEqual(
            self.sol.shortestBridge(grid=[[0, 1, 0], [0, 0, 0], [0, 0, 1]]), 2
        )
        print("OK")

    def test_shortest_bridge_3(self):
        print("Test shortestBridge 3... ", end="")
        self.assertEqual(
            self.sol.shortestBridge(
                grid=[
                    [1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 1, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1],
                ]
            ),
            1,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

import unittest
from typing import List


class DisjointSet:
    def __init__(self, rows, cols):
        self.root = [[(r, c) for c in range(cols)] for r in range(rows)]

    def find(self, cell: tuple[int, int]) -> tuple[int, int]:
        r, c = cell
        if self.root[r][c] == cell:
            return cell
        self.root[r][c] = self.find(self.root[r][c])
        return self.root[r][c]

    def union(self, cell1: tuple[int, int], cell2: tuple[int, int]) -> None:
        root1 = self.find(cell1)
        root2 = self.find(cell2)
        if root1 != root2:
            self.root[root2[0]][root2[1]] = root1

    def connected(
        self, cell1: tuple[int, int], cell2: tuple[int, int]
    ) -> bool:
        return self.find(cell1) == self.find(cell2)


class Solution:
    def latestDayToCross(
        self, row: int, col: int, cells: List[List[int]]
    ) -> int:
        ds = DisjointSet(row + 2, col + 2)
        water = set()
        directions = [(r, c) for r in (0, -1, 1) for c in (0, -1, 1)][1:]
        col += 1

        for r in range(0, row + 2, 3):
            water.add((r, 0))
            water.add((r, col))
            ds.union((0, 0), (r, 0))
            ds.union((0, col), (r, col))

        for day, cell in enumerate(map(tuple, cells)):
            water.add(cell)
            for dr, dc in directions:
                neib = (cell[0] + dr, cell[1] + dc)
                if neib in water:
                    ds.union(cell, neib)
            if ds.connected((0, 0), (0, col)):
                return day


class Solution2:
    def latestDayToCross(
        self, row: int, col: int, cells: List[List[int]]
    ) -> int:
        self.root = [[0] * (col + 2) for _ in range(row + 2)]

        self.root[0][0] = (0, 0)
        self.root[0][col + 1] = (0, col + 1)

        for day, coords in enumerate(cells):
            r, c = coords
            self.root[r][c] = (r, c)
            if c == 1:
                self.union((0, 0), (r, c))
            if c == col:
                self.union((0, col + 1), (r, c))
            con_prev = False
            for y, x in (
                (r - 1, c),
                (r - 1, c + 1),
                (r, c + 1),
                (r + 1, c + 1),
                (r + 1, c),
                (r + 1, c - 1),
                (r, c - 1),
                (r - 1, c - 1),
            ):
                if con_prev:
                    if not self.root[y][x]:
                        con_prev = False
                elif self.root[y][x]:
                    self.union((y, x), (r, c))
                    con_prev = True
            if self.connected((0, 0), (0, col + 1)):
                return day

    def find(self, node):
        if node == self.root[node[0]][node[1]]:
            return node
        self.root[node[0]][node[1]] = self.find(self.root[node[0]][node[1]])
        return self.root[node[0]][node[1]]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.root[root2[0]][root2[1]] = root1

    def connected(self, node1, node2):
        return self.find(node1) == self.find(node2)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_latest_day_to_cross_1(self):
        print("Test latestDayToCross 1... ", end="")
        self.assertEqual(
            self.sol.latestDayToCross(
                row=2, col=2, cells=[[1, 1], [2, 1], [1, 2], [2, 2]]
            ),
            2,
        )
        print("OK")

    def test_latest_day_to_cross_2(self):
        print("Test latestDayToCross 2... ", end="")
        self.assertEqual(
            self.sol.latestDayToCross(
                row=2, col=2, cells=[[1, 1], [1, 2], [2, 1], [2, 2]]
            ),
            1,
        )
        print("OK")

    def test_latest_day_to_cross_3(self):
        print("Test latestDayToCross 3... ", end="")
        self.assertEqual(
            self.sol.latestDayToCross(
                row=3,
                col=3,
                cells=[
                    [1, 2],
                    [2, 1],
                    [3, 3],
                    [2, 2],
                    [1, 1],
                    [1, 3],
                    [2, 3],
                    [3, 2],
                    [3, 1],
                ],
            ),
            3,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

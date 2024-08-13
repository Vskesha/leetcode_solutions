import unittest
from collections import deque
from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        n3 = n * 3
        g = [[1] * n3 for _ in range(n3)]

        for i in range(0, n3, 3):
            for j in range(0, n3, 3):
                ch = grid[i // 3][j // 3]
                if ch == "/":
                    g[i][j + 2] = g[i + 1][j + 1] = g[i + 2][j] = 0
                elif ch == "\\":
                    g[i][j] = g[i + 1][j + 1] = g[i + 2][j + 2] = 0

        def dfs(i, j):
            if i == -1 or j == -1 or i == n3 or j == n3 or g[i][j] == 0:
                return
            g[i][j] = 0
            for ni, nj in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                dfs(ni, nj)

        ans = 0
        for i in range(n3):
            for j in range(n3):
                if g[i][j]:
                    dfs(i, j)
                    ans += 1

        return ans


class Solution2:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid) * 3
        gr = [[1] * n for _ in range(n)]

        for i in range(0, n, 3):
            for j in range(0, n, 3):
                ch = grid[i // 3][j // 3]
                if ch == "/":
                    gr[i][j + 2] = gr[i + 1][j + 1] = gr[i + 2][j] = 0
                elif ch == "\\":
                    gr[i][j] = gr[i + 1][j + 1] = gr[i + 2][j + 2] = 0
        ans = 0
        for i in range(n):
            for j in range(n):
                if gr[i][j]:
                    ans += 1
                    self.bfs(i, j, gr, n)

        return ans

    @staticmethod
    def bfs(i, j, gr, n):
        gr[i][j] = 0
        que = deque([(i, j)])
        while que:
            i, j = que.popleft()
            for y, x in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                if 0 <= y < n and 0 <= x < n and gr[y][x]:
                    que.append((y, x))
                    gr[y][x] = 0


class DisjointSet:
    def __init__(self, n):
        self._groups = n
        self.root = list(range(n))

    def find(self, node):
        if node != self.root[node]:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.root[root2] = root1
            self.decrease_groups(1)

    def decrease_groups(self, n):
        self._groups -= n

    def get_groups(self):
        return self._groups


class Solution3:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid) * 3
        ds = DisjointSet(n * n)
        gr = [[1] * n for _ in range(n)]

        for i in range(0, n, 3):
            for j in range(0, n, 3):
                ch = grid[i // 3][j // 3]
                if ch == "/":
                    ds.decrease_groups(3)
                    gr[i][j + 2] = gr[i + 1][j + 1] = gr[i + 2][j] = 0
                elif ch == "\\":
                    ds.decrease_groups(3)
                    gr[i][j] = gr[i + 1][j + 1] = gr[i + 2][j + 2] = 0

        for j in range(1, n):
            if gr[0][j] and gr[0][j - 1]:
                ds.union(j, j - 1)
        for i in range(1, n):
            if gr[i][0] and gr[i - 1][0]:
                ds.union(i * n, (i - 1) * n)
        for i in range(1, n):
            for j in range(1, n):
                if gr[i][j]:
                    cc = i * n + j
                    if gr[i - 1][j]:
                        ds.union(cc, cc - n)
                    if gr[i][j - 1]:
                        ds.union(cc, cc - 1)

        return ds.get_groups()


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        dots = len(grid) + 1
        parent = [i for i in range(dots * dots)]
        count = 1

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x != parent_y:
                if parent_x < parent_y:
                    parent[parent_y] = parent_x
                else:
                    parent[parent_x] = parent_y
                return False
            return True

        for i in range(dots):
            for j in range(dots):
                if i == 0 or j == 0 or i == dots - 1 or j == dots - 1:
                    cell = i * dots + j
                    union(0, cell)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == " ":
                    continue
                if grid[i][j] == "/":
                    # point1 = (i+1, j)
                    # point2 = (i, j+1)
                    cell1 = (i + 1) * dots + j
                    cell2 = i * dots + j + 1
                    if union(cell1, cell2):
                        count += 1
                elif grid[i][j] == "\\":
                    # point1 = (i,j)
                    # point2 = (i+1, j+1)
                    cell1 = i * dots + j
                    cell2 = (i + 1) * dots + j + 1
                    if union(cell1, cell2):
                        count += 1
        return count


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_regions_by_slashes1(self):
        print("Test regionsBySlashes 1 ... ", end="")
        self.assertEqual(self.sol.regionsBySlashes(grid=[" /", "/ "]), 2)
        print("OK")

    def test_regions_by_slashes2(self):
        print("Test regionsBySlashes 2 ... ", end="")
        self.assertEqual(self.sol.regionsBySlashes(grid=[" /", "  "]), 1)
        print("OK")

    def test_regions_by_slashes3(self):
        print("Test regionsBySlashes 3 ... ", end="")
        self.assertEqual(self.sol.regionsBySlashes(grid=["/\\", "\\/"]), 5)
        print("OK")


if __name__ == "__main__":
    unittest.main()

from collections import deque
from typing import List


class DisjointSet:

    def __init__(self, gr):
        self.gr = gr
        self.root = list(range(self.gr))

    def find(self, node):
        if self.root[node] == node:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.root[root2] = root1
            self.gr -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid[0])
        n = len(grid)
        zero, one = '0', '1'

        ds = DisjointSet(m * n)
        ds.gr -= int(grid[0][0] == zero)

        for i in range(1, n):
            if grid[i][0] == zero:
                ds.gr -= 1
            elif grid[i - 1][0] == one:
                ds.union(i * m, (i - 1) * m)

        for j in range(1, m):
            if grid[0][j] == zero:
                ds.gr -= 1
            elif grid[0][j - 1] == one:
                ds.union(j, j - 1)

        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] == zero:
                    ds.gr -= 1
                    continue
                if grid[i - 1][j] == one:
                    ds.union(i * m + j, (i - 1) * m + j)
                if grid[i][j - 1] == one:
                    ds.union(i * m + j, i * m + j - 1)

        return ds.gr


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j):
            if i == -1 or i == n or j == -1 or j == m or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                dfs(i + di, j + dj)

        ans = 0
        m, n = len(grid[0]), len(grid)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)

        return ans


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:

        def traverse(i, j):
            bfs = deque()
            bfs.append((i, j))

            while bfs:
                y, x = bfs.popleft()
                if y and grid[y - 1][x] == '1' and not visited[y - 1][x]:
                    bfs.append((y - 1, x))
                    visited[y - 1][x] = True
                if x and grid[y][x - 1] == '1' and not visited[y][x - 1]:
                    bfs.append((y, x - 1))
                    visited[y][x - 1] = True
                if y < n - 1 and grid[y + 1][x] == '1' and not visited[y + 1][x]:
                    bfs.append((y + 1, x))
                    visited[y + 1][x] = True
                if x < m - 1 and grid[y][x + 1] == '1' and not visited[y][x + 1]:
                    bfs.append((y, x + 1))
                    visited[y][x + 1] = True

        m = len(grid[0])
        n = len(grid)

        visited = [[False] * m for _ in range(n)]
        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0' or visited[i][j]:
                    continue
                visited[i][j] = True
                ans += 1
                traverse(i, j)

        return ans


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.numIslands(grid=[["1", "1", "1", "1", "0"],
                                ["1", "1", "0", "1", "0"],
                                ["1", "1", "0", "0", "0"],
                                ["0", "0", "0", "0", "0"]]) == 1
    print('OK')

    print('Test 2... ', end='')
    assert sol.numIslands(grid=[["1", "1", "0", "0", "0"],
                                ["1", "1", "0", "0", "0"],
                                ["0", "0", "1", "0", "0"],
                                ["0", "0", "0", "1", "1"]]) == 3
    print('OK')


if __name__ == '__main__':
    test()

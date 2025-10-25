from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat[0])
        n = len(mat)

        bfs = deque()

        for i in range(n):
            for j in range(m):
                if mat[i][j]:
                    mat[i][j] = -1
                else:
                    bfs.append((i, j))

        while bfs:
            i, j = bfs.popleft()
            d = mat[i][j] + 1

            if i and mat[i - 1][j] == -1:
                mat[i - 1][j] = d
                bfs.append((i - 1, j))
            if j and mat[i][j - 1] == -1:
                mat[i][j - 1] = d
                bfs.append((i, j - 1))
            if i < n - 1 and mat[i + 1][j] == -1:
                mat[i + 1][j] = d
                bfs.append((i + 1, j))
            if j < m - 1 and mat[i][j + 1] == -1:
                mat[i][j + 1] = d
                bfs.append((i, j + 1))

        return mat


class Solution1:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat[0])
        n = len(mat)
        dist = [[-1] * m for _ in range(n)]
        bfs = deque()

        for i in range(n):
            for j in range(m):
                if not mat[i][j]:
                    dist[i][j] = 0
                    bfs.append((i, j))

        while bfs:
            i, j = bfs.popleft()
            if i > 0 and dist[i - 1][j] == -1:
                dist[i - 1][j] = dist[i][j] + 1
                bfs.append((i - 1, j))
            if j > 0 and dist[i][j - 1] == -1:
                dist[i][j - 1] = dist[i][j] + 1
                bfs.append((i, j - 1))
            if i < n - 1 and dist[i + 1][j] == -1:
                dist[i + 1][j] = dist[i][j] + 1
                bfs.append((i + 1, j))
            if j < m - 1 and dist[i][j + 1] == -1:
                dist[i][j + 1] = dist[i][j] + 1
                bfs.append((i, j + 1))

        return dist


class Solution2:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        n = len(mat)
        m = len(mat[0])
        b = m + n
        dist = [[b if mat[i][j] else 0 for j in range(m)] for i in range(n)]

        for j in range(1, m):
            dist[0][j] = min(dist[0][j], dist[0][j - 1] + 1)
        for i in range(1, n):
            dist[i][0] = min(dist[i][0], dist[i - 1][0] + 1)
            for j in range(1, m):
                dist[i][j] = min(
                    dist[i][j], min(dist[i][j - 1], dist[i - 1][j]) + 1
                )

        for j in range(m - 2, -1, -1):
            dist[n - 1][j] = min(dist[n - 1][j], dist[n - 1][j + 1] + 1)
        for i in range(n - 2, -1, -1):
            dist[i][m - 1] = min(dist[i][m - 1], dist[i + 1][m - 1] + 1)
            for j in range(m - 2, -1, -1):
                dist[i][j] = min(
                    dist[i][j], min(dist[i][j + 1], dist[i + 1][j]) + 1
                )

        return dist


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    out = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    for i, m in enumerate(sol.updateMatrix(mat)):
        assert out[i] == m
    print("OK")

    print("Test 2 ... ", end="")
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    out = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    for i, m in enumerate(sol.updateMatrix(mat)):
        assert out[i] == m
    print("OK")


if __name__ == "__main__":
    test()

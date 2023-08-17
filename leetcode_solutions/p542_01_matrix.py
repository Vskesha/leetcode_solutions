from collections import deque


class Solution:
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
                dist[i][j] = min(dist[i][j], min(dist[i][j - 1], dist[i - 1][j]) + 1)

        for j in range(m - 2, -1, -1):
            dist[n - 1][j] = min(dist[n - 1][j], dist[n - 1][j + 1] + 1)
        for i in range(n - 2, -1, -1):
            dist[i][m - 1] = min(dist[i][m - 1], dist[i + 1][m - 1] + 1)
            for j in range(m - 2, -1, -1):
                dist[i][j] = min(dist[i][j], min(dist[i][j + 1], dist[i + 1][j]) + 1)

        return dist


def main():
    sol = Solution()
    mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(' [[0, 0, 0], [0, 1, 0], [0, 0, 0]]\n', sol.updateMatrix(mat))
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    print(' [[0, 0, 0], [0, 1, 0], [1, 2, 1]]\n', sol.updateMatrix(mat))


if __name__ == '__main__':
    main()

def updateMatrix(mat):
    n, m = len(mat), len(mat[0])
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


if __name__ == '__main__':
    mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(updateMatrix(mat), 'should be Output: [[0,0,0],[0,1,0],[0,0,0]]')
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    print(updateMatrix(mat), 'should be Output: [[0,0,0],[0,1,0],[1,2,1]]')

class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n = len(grid)

        aux = [[0] * n for _ in range(n)]
        aux[-1][-1] = grid[-1][-1]
        for i in range(n - 2, -1, -1):
            aux[i][n - 1] = -1 if grid[i][n - 1] == - \
                1 else grid[i][n - 1] + aux[i + 1][n - 1]
        for j in range(n - 2, -1, -1):
            aux[n - 1][j] = -1 if grid[n - 1][j] == - \
                1 else grid[n - 1][j] + aux[n - 1][j + 1]
        for i in range(n - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if grid[i][j] == -1:
                    aux[i][j] = -1
                aux[i][j] = max(aux[i + 1][j], aux[i][j + 1])
                if aux[i][j] != -1:
                    aux[i][j] += grid[i][j]

        if aux[0][0] == -1:
            return 0
        total = grid[0][0]

        i, j = 0, 0
        while i < n and j < n:
            grid[i][j] = 0
            if i == n - 1 or aux[i][j + 1] > aux[i + 1][j]:
                j += 1
            else:
                i += 1

        return total


if __name__ == '__main__':
    sol = Solution()
    print('5 ===', sol.cherryPickup(grid=[[0, 1, -1], [1, 0, -1], [1, 1, 1]]))
    print('0 ===', sol.cherryPickup(grid=[[1, 1, -1], [1, -1, 1], [-1, 1, 1]]))

class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n = len(grid)
        aux = [[0] * (n + 2) for _ in range(n + 2)]

        for i in range(n, 0, -1):
            for j in range(n, 0, -1):
                if grid[i - 1][j - 1] == -1:
                    aux[i][j] = -1
                    continue
                aux[i][j] = max(aux[i + 1][j], aux[i][j + 1])
                if aux[i][j] != -1:
                    aux[i][j] += grid[i - 1][j - 1]

        ans = aux[1][1]
        if ans == -1:
            return 0

        i, j = 0, 0
        while i < n and j < n:
            grid[i][j] = 0
            if i == n - 1:
                j += 1
            elif j == n - 1:
                i += 1
            elif aux[i + 1][j + 2] > aux[i + 2][j + 1]:
                j += 1
            elif aux[i + 1][j + 2] < aux[i + 2][j + 1]:
                i += 1
            elif i > j:
                j += 1
            else:
                i += 1

        for i in range(1, n+1):
            for j in range(1, n+1):
                if grid[i - 1][j - 1] == -1:
                    aux[i][j] = -1
                    continue
                aux[i][j] = max(aux[i - 1][j], aux[i][j - 1])
                if aux[i][j] != -1:
                    aux[i][j] += grid[i - 1][j - 1]
        ans += aux[n][n]

        return ans


if __name__ == '__main__':
    sol = Solution()
    print('5 ===', sol.cherryPickup(grid=[[0, 1, -1], [1, 0, -1], [1, 1, 1]]))
    print('0 ===', sol.cherryPickup(grid=[[1, 1, -1], [1, -1, 1], [-1, 1, 1]]))
    print('15 ===', sol.cherryPickup([[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]]))

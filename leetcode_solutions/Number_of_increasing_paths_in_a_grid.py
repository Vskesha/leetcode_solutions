class Solution:
    def count_paths(self, grid: list[list[int]]) -> int:
        mod = 10 ** 9 + 7
        n = len(grid)
        m = len(grid[0])

        aux = [[1] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]

        def dfs(i, j):
            if not visited[i][j]:
                for y, x in ((i-1, j), (i, j+1), (i+1, j), (i, j-1)):
                    if 0 <= y < n and 0 <= x < m and grid[i][j] > grid[y][x]:
                        aux[i][j] += dfs(y, x) % mod
                visited[i][j] = True
            return aux[i][j]

        return sum(dfs(i, j) for i in range(n) for j in range(m)) % mod


def main():
    sol = Solution()
    print('8 ===', sol.count_paths(grid=[[1, 1], [3, 4]]))
    print('3 ===', sol.count_paths(grid=[[1], [2]]))


if __name__ == '__main__':
    main()
from functools import lru_cache


class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n = len(grid)

        @lru_cache(None)
        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2
            if r1 == n or r2 == n or c1 == n or c2 == n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            if r1 == c1 == n - 1:
                return grid[r1][c1]
            return max(dp(r1 + 1, c1, c2), dp(r1 + 1, c1, c2 + 1), dp(r1, c1 + 1, c2), dp(r1, c1 + 1, c2 + 1)) + grid[r1][c1] + grid[r2][c2] * (r1 != r2)

        return max(0, dp(0, 0, 0))


if __name__ == '__main__':
    sol = Solution()
    print('5 ===', sol.cherryPickup(grid=[[0, 1, -1],
                                          [1, 0, -1],
                                          [1, 1, 1]]))
    print('0 ===', sol.cherryPickup(grid=[[1, 1, -1],
                                          [1, -1, 1],
                                          [-1, 1, 1]]))
    print('15 ===', sol.cherryPickup([[1, 1, 1, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 1],
                                      [1, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 1, 1, 1]]))

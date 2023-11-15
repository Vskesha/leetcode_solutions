from functools import lru_cache
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        M = len(grid[0])
        N = len(grid)

        @lru_cache(None)
        def dp(i, j1, j2):
            if i == N:
                return 0
            if j1 < 0 or j2 == M or j2 <= j1:
                return -1
            return (max(dp(i + 1, jf, js)
                        for jf in range(j1 - 1, j1 + 2)
                        for js in range(j2 - 1, j2 + 2))
                    + grid[i][j1]
                    + grid[i][j2])

        return dp(0, 0, M - 1)


class Solution2:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)

        @lru_cache(None)
        def dp(i, j1, j2):
            if i == n:
                return 0
            ans = 0
            for jf in range(max(0, j1 - 1), min(j1 + 2, m - 1)):
                for js in range(max(jf + 1, j2 - 1), min(j2 + 2, m)):
                    ans = max(ans, dp(i + 1, jf, js))

            ans += grid[i][j1] + grid[i][j2]
            return ans

        return dp(0, 0, m - 1)


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.cherryPickup(grid=[[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]) == 24
    print('OK')

    print('Test 1... ', end='')
    assert sol.cherryPickup(
        grid=[[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0],
              [1, 0, 2, 3, 0, 0, 6]]) == 28
    print('OK')


if __name__ == '__main__':
    test()

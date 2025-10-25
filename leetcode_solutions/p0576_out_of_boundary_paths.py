from functools import lru_cache


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        MOD = 10**9 + 7
        gr = [[0] * (n + 2) for _ in range(m + 2)]
        gr[startRow + 1][startColumn + 1] = 1
        ans = 0
        for _ in range(maxMove):
            for i in range(1, m + 1):
                ans = (ans + gr[i][1] + gr[i][n]) % MOD
            for j in range(1, n + 1):
                ans = (ans + gr[1][j] + gr[m][j]) % MOD
            ngr = [[0] * (n + 2) for _ in range(m + 2)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    ngr[i][j] = (
                        gr[i - 1][j]
                        + gr[i + 1][j]
                        + gr[i][j - 1]
                        + gr[i][j + 1]
                    ) % MOD
            gr = ngr
        return ans


class Solution2:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        @lru_cache(None)
        def recursive_run(i, j, moves):
            if i >= m or j >= n or i < 0 or j < 0:
                return 1
            elif moves == 0:
                return 0
            out = recursive_run(i + 1, j, moves - 1)
            out += recursive_run(i - 1, j, moves - 1)
            out += recursive_run(i, j + 1, moves - 1)
            out += recursive_run(i, j - 1, moves - 1)
            return out

        return recursive_run(startRow, startColumn, maxMove) % (10**9 + 7)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0) == 6
    print("OK")

    print("Test 2... ", end="")
    assert sol.findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1) == 12
    print("OK")

    print("Test 3... ", end="")
    assert (
        sol.findPaths(m=1, n=2, maxMove=50, startRow=0, startColumn=0) == 150
    )
    print("OK")


if __name__ == "__main__":
    test()

from functools import lru_cache


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @lru_cache(None)
        def dfs(i, j, k):
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0
            if k == 0:
                return 1

            return (
                sum(
                    dfs(di, dj, k - 1)
                    for di, dj in (
                        (i - 2, j - 1),
                        (i - 2, j + 1),
                        (i - 1, j - 2),
                        (i - 1, j + 2),
                        (i + 1, j - 2),
                        (i + 1, j + 2),
                        (i + 2, j - 1),
                        (i + 2, j + 1),
                    )
                )
                / 8
            )

        return dfs(row, column, k)


# recursive dp solution
class Solution1:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @lru_cache(None)
        def pr(i: int, j: int, moves: int):
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0

            if not moves:
                return 1

            prob = 0
            for y, x in (
                (i - 2, j + 1),
                (i - 1, j + 2),
                (i + 1, j + 2),
                (i + 2, j + 1),
                (i + 2, j - 1),
                (i + 1, j - 2),
                (i - 1, j - 2),
                (i - 2, j - 1),
            ):
                prob += pr(y, x, moves - 1) / 8

            return prob

        return pr(row, column, k)


# iterative dp solution
class Solution2:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:
            return 1

        dp = [[[0] * n for _ in range(n)] for _ in range(k)]

        for i in range(n):
            for j in range(n):
                dp[0][i][j] = 1

        for m in range(1, k):
            for i in range(n):
                for j in range(n):
                    for y, x in (
                        (i - 2, j + 1),
                        (i - 2, j - 1),
                        (i - 1, j + 2),
                        (i - 1, j - 2),
                        (i + 1, j + 2),
                        (i + 1, j - 2),
                        (i + 2, j + 1),
                        (i + 2, j - 1),
                    ):
                        if 0 <= y < n and 0 <= x < n:
                            dp[m][i][j] += dp[m - 1][y][x] / 8

        ans = 0
        for y, x in (
            (row - 2, column + 1),
            (row - 2, column - 1),
            (row + 2, column + 1),
            (row + 2, column - 1),
            (row - 1, column + 2),
            (row - 1, column - 2),
            (row + 1, column + 2),
            (row + 1, column - 2),
        ):
            if 0 <= y < n and 0 <= x < n:
                ans += dp[k - 1][y][x] / 8
        return ans


def test_knight_probability():
    sol = Solution()

    print("Test 1... ", end="")
    assert 0.06250 == sol.knightProbability(n=3, k=2, row=0, column=0)
    print("OK")

    print("Test 2... ", end="")
    assert 1.0000 == sol.knightProbability(n=1, k=0, row=0, column=0)
    print("OK")


if __name__ == "__main__":
    test_knight_probability()

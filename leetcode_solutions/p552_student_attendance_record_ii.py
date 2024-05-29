from functools import lru_cache


class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7

        dp = [1] * 6

        for _ in range(n):
            dp = [
                (dp[0] + dp[1] + dp[3]) % mod,
                (dp[0] + dp[2] + dp[3]) % mod,
                (dp[0] + dp[3]) % mod,
                (dp[3] + dp[4]) % mod,
                (dp[3] + dp[5]) % mod,
                dp[3],
            ]

        return dp[0]


class Solution1:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [[1] * 3 for _ in range(2)]

        for _ in range(n):
            ndp = [[0] * 3 for _ in range(2)]
            for wa in range(2):
                for lc in range(3):
                    ndp[wa][lc] = dp[wa][0]
                    if lc < 2:
                        ndp[wa][lc] += dp[wa][lc + 1]
                    if not wa:
                        ndp[wa][lc] += dp[1][0]
                    ndp[wa][lc] %= mod
            dp = ndp

        return dp[0][0]


# Not valid solution because of maximum recursion depth
class Solution2:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7

        @lru_cache(None)
        def comb(n, lc, wa) -> int:
            if not n:
                return 1
            n -= 1
            res = comb(n, 0, wa)  # ends with "P"
            if lc < 2:
                res += comb(n, lc + 1, wa)  # ends with "L"
            if not wa:
                res += comb(n, 0, 1)  # ends with "A"
            return res % mod

        return comb(n, 0, 0)


def test_check_record():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.checkRecord(n=2) == 8
    print("OK")

    print("Test 2... ", end="")
    assert sol.checkRecord(n=1) == 3
    print("OK")

    print("Test 3... ", end="")
    assert sol.checkRecord(n=10101) == 183236316
    print("OK")


if __name__ == "__main__":
    test_check_record()

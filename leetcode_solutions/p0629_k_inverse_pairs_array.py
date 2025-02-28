class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        mip = n * (n - 1) // 2
        if k > mip:
            return 0
        if k == 0 or k == mip:
            return 1
        if k > mip // 2:
            k = mip - k
        k += 1
        dp = [0] * k
        dp[0] = 1

        for win in range(1, n):
            ndp = [0] * k
            ws = 0
            for i in range(min(win, k)):
                ws = (ws + dp[i]) % mod
                ndp[i] = ws
            for j, i in enumerate(range(win, k)):
                ws = (ws + dp[i]) % mod
                ndp[i] = ws
                ws = ws - dp[j]
            dp = ndp
        return dp[-1]


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.kInversePairs(n=3, k=0) == 1
    print("OK")

    print("Test 2... ", end="")
    assert sol.kInversePairs(n=3, k=1) == 2
    print("OK")


if __name__ == "__main__":
    test()

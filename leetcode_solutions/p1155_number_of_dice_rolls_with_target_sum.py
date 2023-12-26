from functools import lru_cache, cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 1_000_000_007

        @lru_cache(None)
        def dp(n, target):
            if n == target or target == n * k:
                return 1
            if target < n or target > n * k:
                return 0
            res = 0
            for i in range(1, k + 1):
                res += dp(n - 1, target - i)
                res %= mod
            return res

        return dp(n, target)


class Solution1:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 1_000_000_007

        @lru_cache(None)
        def dp(n, target):
            if n == target or target == n * k:
                return 1
            if target < n or target > n * k:
                return 0
            res = 0
            for i in range(1, k + 1):
                res = (res + dp(n - 1, target - i)) % mod
            return res

        return dp(n, target)


class Solution2:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(n, t):
            if t <= 0:
                return 0
            if n == 1:
                return 0 if t > k else 1
            ans = 0
            for i in range(1, k + 1):
                ans = (ans + dp(n - 1, t - i)) % MOD
            return ans

        return dp(n, target)


def main():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.numRollsToTarget(n=1, k=6, target=3) == 1
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.numRollsToTarget(n=2, k=6, target=7) == 6
    print("OK")

    print("Test 3 ... ", end="")
    assert sol.numRollsToTarget(n=30, k=30, target=500) == 222616187
    print("OK")


if __name__ == "__main__":
    main()

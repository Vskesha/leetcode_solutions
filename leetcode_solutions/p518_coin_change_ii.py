from functools import lru_cache


# faster recursive dp solution
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:

        @lru_cache(None)
        def dp(remains, i):
            if not remains:
                return 1
            if not i:
                return 0 if remains % coins[0] else 1
            coin = coins[i]
            combs = dp(remains, i - 1)
            if coin <= remains:
                combs += dp(remains - coin, i)
            return combs

        return dp(amount, len(coins) - 1)


# recursive dp solution
class Solution1:
    def change(self, amount: int, coins: list[int]) -> int:

        @lru_cache(None)
        def dp(remains, idx):
            if remains == 0:
                return 1
            if not idx:
                return int(not(remains % coins[idx]))

            combs = 0
            coin = coins[idx]
            for i in range(remains // coin + 1):
                combs += dp(remains - i * coin, idx - 1)
            return combs

        return dp(amount, len(coins) - 1)


# iterative dp solution
class Solution2:
    def change(self, amount: int, coins: list[int]) -> int:
        lc = len(coins)

        dp = [[0] * (amount + 1) for _ in range(lc)]

        coin = coins[0]
        for rem in range(amount + 1):
            dp[0][rem] = 0 if rem % coin else 1

        for j in range(1, lc):
            for rem in range(amount + 1):
                for i in range(rem, -1, -coins[j]):
                    dp[j][rem] += dp[j - 1][i]

        return dp[lc - 1][amount]


# iterative dp solution with memory optimization
class Solution3:
    def change(self, amount: int, coins: list[int]) -> int:
        lc = len(coins)

        dp = [0] * (amount + 1)

        coin = coins[0]
        for rem in range(amount + 1):
            dp[rem] = 0 if rem % coin else 1

        for j in range(1, lc):
            new_dp = [0] * (amount + 1)
            for rem in range(amount + 1):
                for i in range(rem, -1, -coins[j]):
                    new_dp[rem] += dp[i]
            dp = new_dp

        return dp[amount]


# faster iterative dp solution with memory optimization
class Solution4:
    def change(self, amount: int, coins: list[int]) -> int:
        lc = len(coins)
        coin = coins[0]
        dp = [int(not(rem % coin)) for rem in range(amount + 1)]

        for j in range(1, lc):
            new_dp = [0] * (amount + 1)
            for rem in range(amount + 1):
                new_dp[rem] = dp[rem]
                if coins[j] <= rem:
                    new_dp[rem] += new_dp[rem - coins[j]]
            dp = new_dp

        return dp[amount]


def main():
    sol = Solution()
    print('4 ===', sol.change(amount=5, coins=[1, 2, 5]))
    print('0 ===', sol.change(amount=3, coins=[2]))
    print('1 ===', sol.change(amount=10, coins=[10]))


if __name__ == '__main__':
    main()

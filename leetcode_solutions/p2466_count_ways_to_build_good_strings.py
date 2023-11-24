class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        if one < zero:
            one, zero = zero, one
        for ln in range(zero, one):
            dp[ln] = dp[ln - zero]
        for ln in range(one, low):
            dp[ln] = (dp[ln - zero] + dp[ln - one]) % mod
        ans = 0
        for ln in range(low, high + 1):
            dp[ln] = (dp[ln - zero] + dp[ln - one]) % mod
            ans = (ans + dp[ln]) % mod
        return ans


class Solution2:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        for e in range(1, high + 1):
            if e >= zero:
                dp[e] += dp[e - zero]
            if e >= one:
                dp[e] += dp[e - one]
            dp[e] %= mod

        return sum(dp[low:]) % mod


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.countGoodStrings(low=3, high=3, zero=1, one=1) == 8
    print('OK')

    print('Test 2... ', end='')
    assert sol.countGoodStrings(low=2, high=3, zero=1, one=2) == 5
    print('OK')


if __name__ == '__main__':
    test()

class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        a = b = c = d = 1

        for _ in range(n - 1):
            a, b, c, d = (b + c) % mod, a * 2 % mod, (a * 2 + d) % mod, c * 2 % mod

        return (4 * a + 2 * b + 2 * c + d) % mod + int(n == 1)


class Solution1:
    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7

        dp = [1] * 10
        for _ in range(n - 1):
            new = [0] * 10
            new[0] = (dp[4] + dp[6]) % mod
            new[1] = new[3] = new[7] = new[9] = (dp[6] + dp[8]) % mod
            new[2] = new[8] = (dp[7] + dp[9]) % mod
            new[4] = new[6] = (dp[3] + dp[9] + dp[0]) % mod
            dp = new

        return sum(dp) % mod


class Solution2:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        mod = 10 ** 9 + 7
        a, b, c, d = 4, 2, 2, 1

        for _ in range(n - 1):
            a, b, c, d = (b + c) * 2 % mod, a, (a + d * 2) % mod, c

        return (a + b + c + d) % mod


class Solution3:
    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        adj_map = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [],
                   6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}

        dp = [1] * 10

        for _ in range(n - 1):
            newdp = [0] * 10
            for i in range(10):
                for d in adj_map[i]:
                    newdp[i] = (newdp[i] + dp[d]) % mod
            dp = newdp

        return sum(dp) % mod


class Solution4:
    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7

        dp = [1] * 10
        for _ in range(n - 1):
            new = []
            new.append((dp[4] + dp[6]) % mod)
            new.append((dp[6] + dp[8]) % mod)
            new.append((dp[7] + dp[9]) % mod)
            new.append((dp[4] + dp[8]) % mod)
            new.append((dp[3] + dp[9] + dp[0]) % mod)
            new.append(0)
            new.append((dp[1] + dp[7] + dp[0]) % mod)
            new.append((dp[2] + dp[6]) % mod)
            new.append((dp[1] + dp[3]) % mod)
            new.append((dp[2] + dp[4]) % mod)
            dp = new

        return sum(dp) % mod


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.knightDialer(n=1) == 10
    print('OK')

    print('Test 2... ', end='')
    assert sol.knightDialer(n=2) == 20
    print('OK')

    print('Test 3... ', end='')
    assert sol.knightDialer(n=3131) == 136006598
    print('OK')


if __name__ == '__main__':
    test()

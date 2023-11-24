class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        a, b = 1, 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] in '12':
                    a, b = b, a
                else:
                    return 0
            elif 10 < int(s[i-1]+s[i]) < 27:
                a, b = b, a + b
            else:
                a, b = b, b

        return b


class Solution2:
    def numDecodings(self, s: str) -> int:
        ls = len(s)
        dp = [1] * (ls + 1)
        if s[0] == '0':
            return 0

        for i in range(1, ls):
            if s[i] == '0':
                if s[i-1] in '12':
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            elif 10 < int(s[i-1]+s[i]) < 27:
                dp[i+1] = dp[i] + dp[i-1]
            else:
                dp[i+1] = dp[i]

        return dp[-1]


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.numDecodings(s="12") == 2
    print('OK')

    print('Test 2... ', end='')
    assert sol.numDecodings(s="226") == 3
    print('OK')

    print('Test 3... ', end='')
    assert sol.numDecodings(s="06") == 0
    print('OK')

    print('Test 4... ', end='')
    assert sol.numDecodings(s="2101") == 1
    print('OK')


if __name__ == '__main__':
    test()

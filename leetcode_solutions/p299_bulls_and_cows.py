from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bullnumber = 0

        nonbullsecret = Counter()
        nonbullguess = Counter()

        for a, b in zip(secret, guess):
            if a == b:
                bullnumber += 1
            else:
                nonbullsecret[a] += 1
                nonbullguess[b] += 1

        nonbullnumber = 0
        for ch in nonbullguess:
            nonbullnumber += min(nonbullguess[ch], nonbullsecret[ch])

        return f'{bullnumber}A{nonbullnumber}B'


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.getHint(secret='1807', guess='7810') == '1A3B'
    print('OK')

    print('Test 2... ', end='')
    assert sol.getHint(secret='1123', guess='0111') == '1A1B'
    print('OK')


if __name__ == '__main__':
    test()

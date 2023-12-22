class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        sm = s.count('1')
        for i in range(len(s) - 1):
            sm += int(s[i]) * (-2) + 1
            ans = max(ans, sm)
        return ans


class Solution:
    def maxScore(self, s: str) -> int:
        b = -1
        o = z = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                z += 1
                b = max(b, z - o)
            else:
                o += 1
        o += int(s[-1])
        return o + b


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.maxScore(s="011101") == 5
    print('OK')

    print('Test 2... ', end='')
    assert sol.maxScore(s="00111") == 5
    print('OK')

    print('Test 3... ', end='')
    assert sol.maxScore(s="1111") == 3
    print('OK')


if __name__ == '__main__':
    test()

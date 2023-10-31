class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        a = e = i = o = u = 1
        for _ in range(n - 1):
            a, e, i, o, u = e, (a + i) % mod, (a + e + o + u) % mod, (i + u) % mod, a
        return (a + e + i + o + u) % mod


class Solution2:
    def countVowelPermutation(self, n: int) -> int:
        mod = 1_000_000_007
        a = e = i = o = u = 1

        for _ in range(n - 1):
            a, e, i, o, u = (e + i + u) % mod, (a + i) % mod, (e + o) % mod, i, (i + o) % mod
        return (a + e + i + o + u) % mod


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.countVowelPermutation(1) == 5
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.countVowelPermutation(2) == 10
    print('ok')

    print('Test 3 ... ', end='')
    assert sol.countVowelPermutation(5) == 68
    print('ok')


if __name__ == '__main__':
    test()

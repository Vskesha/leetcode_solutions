class Solution:
    def stringCount(self, n: int) -> int:
        mod = 10 ** 9 + 7

        return (pow(26, n, mod) - (pow(25, n, mod) - pow(24, n, mod)) * 3 - pow(23, n, mod) + (
                pow(24, n - 1, mod) * 2 - pow(25, n - 1, mod) - pow(23, n - 1, mod)) * n) % mod


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.stringCount(n=1) == 0
    print('ok')

    print('Test 1... ', end='')
    assert sol.stringCount(n=4) == 12
    print('ok')

    print('Test 1... ', end='')
    assert sol.stringCount(n=10) == 83943898
    print('ok')


if __name__ == '__main__':
    test()

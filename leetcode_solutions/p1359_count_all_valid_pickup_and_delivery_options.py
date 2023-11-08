class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10 ** 9 + 7
        ans = 1

        for i in range(1, n):
            p = i * 2 + 1
            c = p * (p + 1) // 2
            ans = ans * c % mod

        return ans


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.countOrders(n=1) == 1
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.countOrders(n=2) == 6
    print('ok')

    print('Test 3 ... ', end='')
    assert sol.countOrders(n=3) == 90
    print('ok')


if __name__ == '__main__':
    test()

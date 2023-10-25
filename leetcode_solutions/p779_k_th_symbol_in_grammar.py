class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k-1).count('1') % 2


class Solution1:
    def kthGrammar(self, n: int, k: int) -> int:
        def dp(i, j):
            if not i:
                return False
            prev = dp(i - 1, j // 2)
            return not prev if j % 2 else prev

        return int(dp(n - 1, k - 1))


class Solution2:
    def kthGrammar(self, n: int, k: int) -> int:
        z = 0
        k -= 1
        for _ in range(n - 1):
            if k % 2:
                z = 1 - z
            k //= 2
        return z


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.kthGrammar(n=1, k=1) == 0
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.kthGrammar(n=2, k=1) == 0
    print('ok')

    print('Test 3 ... ', end='')
    assert sol.kthGrammar(n=2, k=2) == 1
    print('ok')


if __name__ == '__main__':
    test()

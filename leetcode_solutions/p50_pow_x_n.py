from functools import lru_cache


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        @lru_cache
        def power(x: float, n: int) -> float:
            if n == 1:
                return x
            if n % 2:
                return power(x, n - 1) * x
            return power(x, n // 2) ** 2

        return power(x, n)


def main():
    sol = Solution()
    print('1024.00000 ===', sol.myPow(x=2.00000, n=10))
    print('9.26100 ===', sol.myPow(x=2.10000, n=3))
    print('0,25000 ===', sol.myPow(x=2.00000, n=-2))


if __name__ == '__main__':
    main()

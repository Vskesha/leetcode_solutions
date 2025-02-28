from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b


class Solution2:
    def climbStairs(self, n: int) -> int:
        @cache
        def fib(n):
            return 1 if n < 2 else fib(n - 1) + fib(n - 2)

        return fib(n)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.climbStairs(2) == 2
    print("OK")

    print("Test 2... ", end="")
    assert sol.climbStairs(3) == 3
    print("OK")


if __name__ == "__main__":
    test()

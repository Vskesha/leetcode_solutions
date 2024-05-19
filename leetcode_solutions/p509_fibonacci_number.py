class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a


def test_fib():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.fib(n=2) == 1
    print("OK")

    print("Test 2... ", end="")
    assert sol.fib(n=3) == 2
    print("OK")

    print("Test 3... ", end="")
    assert sol.fib(n=4) == 3
    print("OK")


if __name__ == "__main__":
    test_fib()

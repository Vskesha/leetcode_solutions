class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 4:
            return (n + 1) // 2

        a, b, c = 0, 1, 1
        for _ in range(2, n):
            a, b, c = b, c, a + b + c
        return c


def test_tribonacci():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.tribonacci(n=4) == 4
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.tribonacci(n=25) == 1389537
    print("OK")


if __name__ == "__main__":
    test_tribonacci()

class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        if n % 3 == 2:
            return 3 ** (n // 3) * 2
        if n % 3 == 1:
            return 3 ** (n // 3 - 1) * 4
        return 3 ** (n // 3)


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.integerBreak(n=2) == 1
    print("ok")

    print("Test 1 ... ", end="")
    assert sol.integerBreak(n=10) == 36
    print("ok")


if __name__ == "__main__":
    test()

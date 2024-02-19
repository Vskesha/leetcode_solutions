class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count("1") == 1


class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.isPowerOfTwo(n=1) is True
    print("OK")

    print("Test 2... ", end="")
    assert sol.isPowerOfTwo(n=16) is True
    print("OK")

    print("Test 3... ", end="")
    assert sol.isPowerOfTwo(n=3) is False
    print("OK")


if __name__ == "__main__":
    test()

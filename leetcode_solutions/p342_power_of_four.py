from math import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        bn = bin(n)
        return n and len(bn) % 2 and bn[3:] == "0" * (len(bn) - 3)


class Solution1:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        b = bin(n)[2:]
        return b.count("1") == 1 and b.count("0") % 2 == 0


class Solution2:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0:
            p = int(log(n, 4))
            return pow(4, p) == n
        return False


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if not n:
            return False
        if n == 1:
            return True
        if n % 4:
            return False
        return self.isPowerOfFour(n // 4)


def test_is_power_of_four():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.isPowerOfFour(n=16) is True
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.isPowerOfFour(n=5) is False
    print("OK")

    print("Test 3 ... ", end="")
    assert sol.isPowerOfFour(n=1) is True
    print("OK")


if __name__ == "__main__":
    test_is_power_of_four()

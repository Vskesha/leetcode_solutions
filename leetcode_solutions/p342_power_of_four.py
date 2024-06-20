import unittest
from math import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        b = bin(n)
        return len(b) % 2 and b.count("1") == 1


class Solution1:
    def isPowerOfFour(self, n: int) -> bool:
        bn = bin(n)
        return n and len(bn) % 2 and bn[3:] == "0" * (len(bn) - 3)


class Solution2:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        b = bin(n)[2:]
        return b.count("1") == 1 and b.count("0") % 2 == 0


class Solution3:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0:
            p = int(log(n, 4))
            return pow(4, p) == n
        return False


class Solution4:
    def isPowerOfFour(self, n: int) -> bool:
        if not n:
            return False
        if n == 1:
            return True
        if n % 4:
            return False
        return self.isPowerOfFour(n // 4)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_is_power_of_four_1(self):
        print("Test isPowerOfFour 1... ", end="")
        self.assertTrue(self.sol.isPowerOfFour(n=16))
        print("OK")

    def test_is_power_of_four_2(self):
        print("Test isPowerOfFour 2... ", end="")
        self.assertFalse(self.sol.isPowerOfFour(n=5))
        print("OK")

    def test_is_power_of_four_3(self):
        print("Test isPowerOfFour 3... ", end="")
        self.assertTrue(self.sol.isPowerOfFour(n=1))
        print("OK")


if __name__ == "__main__":
    unittest.main()

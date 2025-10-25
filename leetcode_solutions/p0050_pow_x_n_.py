import unittest
from functools import lru_cache


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x

        res = 1
        for i in bin(n)[2:]:
            res *= res
            if i == "1":
                res *= x

        return res


class Solution2:
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


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_my_pow_1(self):
        print("Test myPow 1... ", end="")
        self.assertAlmostEqual(
            self.sol.myPow(x=2.00000, n=10), 1024.00000, places=5
        )
        print("OK")

    def test_my_pow_2(self):
        print("Test myPow 2... ", end="")
        self.assertAlmostEqual(
            self.sol.myPow(x=2.10000, n=3), 9.26100, places=5
        )
        print("OK")

    def test_my_pow_3(self):
        print("Test myPow 3... ", end="")
        self.assertAlmostEqual(
            self.sol.myPow(x=2.00000, n=-2), 0.25000, places=5
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

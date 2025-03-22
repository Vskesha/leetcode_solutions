import unittest
from math import ceil, sqrt


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        lb = ceil(sqrt(l))
        rb = int(sqrt(r)) + 1

        primes = [True] * rb
        primes[0] = primes[1] = False
        for div in range(2, int(sqrt(rb)) + 1):
            if primes[div]:
                for num in range(div * div, rb, div):
                    primes[num] = False

        special = 0
        for n in range(lb, rb):
            if primes[n]:
                special += 1

        return r - l + 1 - special


class Solution2:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_single_number(n):
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        sl = int((l - 1) ** 0.5) + 1
        sr = int(r**0.5) + 1

        ans = r - l + 1
        for i in range(sl, sr):
            if is_single_number(i):
                ans -= 1
        if l == 1:
            ans += 1
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_nonSpecialCount_1(self):
        print("Test nonSpecialCount 1... ", end="")
        self.assertEqual(3, self.sol.nonSpecialCount(l=5, r=7))
        print("OK")

    def test_nonSpecialCount_2(self):
        print("Test nonSpecialCount 2... ", end="")
        self.assertEqual(11, self.sol.nonSpecialCount(l=4, r=16))
        print("OK")


if __name__ == "__main__":
    unittest.main()

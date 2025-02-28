# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
import unittest
from unittest.mock import patch


def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            gm = guess(m)
            if gm == 0:
                return m
            elif gm == 1:
                l = m + 1
            else:
                r = m - 1


class Solution2:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l < r:
            m = (l + r) // 2
            if guess(m) == 1:
                l = m + 1
            else:
                r = m

        return l


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def get_guess(self, pick: int) -> callable:
        def guess_func(num: int) -> int:
            if num == pick:
                return 0
            elif num < pick:
                return 1
            else:
                return -1
        return guess_func

    def test_guessNumber_1(self):
        print("Test guessNumber 1... ", end="")
        n = 10
        pick = 6
        with patch(__name__ + ".guess", self.get_guess(pick)):
            result = self.sol.guessNumber(n)
        self.assertEqual(pick, result)
        print("OK")

    def test_guessNumber_2(self):
        print("Test guessNumber 2... ", end="")
        n = 1
        pick = 1
        with patch(__name__ + ".guess", self.get_guess(pick)):
            result = self.sol.guessNumber(n)
        self.assertEqual(pick, result)
        print("OK")

    def test_guessNumber_3(self):
        print("Test guessNumber 3... ", end="")
        n = 2
        pick = 1
        with patch(__name__ + ".guess", self.get_guess(pick)):
            result = self.sol.guessNumber(n)
        self.assertEqual(pick, result)
        print("OK")


if __name__ == '__main__':
    unittest.main()

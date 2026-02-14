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
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            gm = guess(mid)
            if gm == 0:
                return mid
            elif gm == 1:
                left = mid + 1
            else:
                right = mid - 1


class Solution2:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2
            if guess(mid) == 1:
                left = mid + 1
            else:
                right = mid

        return left


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


if __name__ == "__main__":
    unittest.main()

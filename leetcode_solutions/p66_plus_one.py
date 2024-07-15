import unittest
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = 1

        for i in range(len(digits) - 1, -1, -1):
            if not d:
                break
            d, digits[i] = divmod(d + digits[i], 10)

        if d:
            return [d] + digits
        return digits


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_plusOne_1(self):
        print("Test plusOne 1... ", end="")
        self.assertEqual([1, 2, 4], self.sol.plusOne(digits=[1, 2, 3]))
        print("OK")

    def test_plusOne_2(self):
        print("Test plusOne 2... ", end="")
        self.assertEqual([4, 3, 2, 2], self.sol.plusOne(digits=[4, 3, 2, 1]))
        print("OK")

    def test_plusOne_3(self):
        print("Test plusOne 3... ", end="")
        self.assertEqual([1, 0], self.sol.plusOne(digits=[9]))
        print("OK")


if __name__ == "__main__":
    unittest.main()

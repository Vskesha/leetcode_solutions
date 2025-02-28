import unittest
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones = ones ^ (num & ~twos)
            twos = twos ^ (num & ~ones)

        return ones


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_single_number_1(self):
        print("Test singleNumber 1... ", end="")
        self.assertEqual(self.sol.singleNumber([2, 2, 3, 2]), 3)
        print("OK")

    def test_single_number_2(self):
        print("Test singleNumber 2... ", end="")
        self.assertEqual(self.sol.singleNumber([0, 1, 0, 1, 0, 1, 99]), 99)
        print("OK")


if __name__ == "__main__":
    unittest.main()

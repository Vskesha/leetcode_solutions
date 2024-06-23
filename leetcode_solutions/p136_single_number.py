import unittest
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_single_number_1(self):
        print("Test singleNumber 1 ... ", end="")
        self.assertEqual(self.sol.singleNumber([2, 2, 1]), 1)
        print("OK")

    def test_single_number_2(self):
        print("Test singleNumber 2 ... ", end="")
        self.assertEqual(self.sol.singleNumber([4, 1, 2, 1, 2]), 4)
        print("OK")

    def test_single_number_3(self):
        print("Test singleNumber 3 ... ", end="")
        self.assertEqual(self.sol.singleNumber([1]), 1)
        print("OK")


if __name__ == "__main__":
    unittest.main()

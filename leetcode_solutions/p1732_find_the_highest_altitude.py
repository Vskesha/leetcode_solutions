import unittest
from itertools import accumulate
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate(gain, initial=0))


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_largest_altitude_1(self):
        print("Test largestAltitude 1... ", end="")
        self.assertEqual(self.sol.largestAltitude(gain=[-5, 1, 5, 0, -7]), 1)
        print("OK")

    def test_largest_altitude_2(self):
        print("Test largestAltitude 2... ", end="")
        self.assertEqual(self.sol.largestAltitude(gain=[-4, -3, -2, -1, 4, 3, 2]), 0)
        print("OK")


if __name__ == "__main__":
    unittest.main()

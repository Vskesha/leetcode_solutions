import unittest
from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s1 = sum(x for x in nums if x < 10)
        s2 = sum(x for x in nums if x >= 10)
        return s1 != s2


class Solution2:
    def canAliceWin(self, nums: List[int]) -> bool:
        s1 = sum(x for x in nums if x < 10)
        s2 = sum(nums) - s1
        return s1 != s2


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_canAliceWin_1(self):
        print("Test canAliceWin 1... ", end="")
        self.assertFalse(self.sol.canAliceWin(nums=[1, 2, 3, 4, 10]))
        print("OK")

    def test_canAliceWin_2(self):
        print("Test canAliceWin 2... ", end="")
        self.assertTrue(self.sol.canAliceWin(nums=[1, 2, 3, 4, 5, 14]))
        print("OK")

    def test_canAliceWin_3(self):
        print("Test canAliceWin 3... ", end="")
        self.assertTrue(self.sol.canAliceWin(nums=[5, 5, 5, 25]))
        print("OK")


if __name__ == "__main__":
    unittest.main()

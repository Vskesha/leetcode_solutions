import unittest
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1


class Solution2:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        ch1 = True
        while i < len(bits):
            ch1 = False if bits[i] else True
            i += 1 if ch1 else 2
        return ch1


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_is_one_bit_character_1(self):
        print("Test isOneBitCharacter 1... ", end="")
        self.assertTrue(self.sol.isOneBitCharacter(bits=[1, 0, 0]))
        print("OK")

    def test_is_one_bit_character_2(self):
        print("Test isOneBitCharacter 2... ", end="")
        self.assertFalse(self.sol.isOneBitCharacter(bits=[1, 1, 1, 0]))
        print("OK")


if __name__ == "__main__":
    unittest.main()

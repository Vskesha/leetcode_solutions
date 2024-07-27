import unittest
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_sortByBits_1(self):
        print("Test sortByBits 1 ... ", end="")
        self.assertListEqual(
            [0, 1, 2, 4, 8, 3, 5, 6, 7],
            self.sol.sortByBits(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8]),
        )
        print("OK")

    def test_sortByBits_2(self):
        print("Test sortByBits 2 ... ", end="")
        self.assertListEqual(
            [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
            self.sol.sortByBits(arr=[1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

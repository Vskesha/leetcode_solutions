import unittest
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(a != b for a, b in zip(heights, sorted(heights)))


class Solution2:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(1 for a, b in zip(heights, sorted(heights)) if a != b)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_height_checker1(self):
        print("Test heightChecker 1 ... ", end="")
        self.assertEqual(self.sol.heightChecker(heights=[1, 1, 4, 2, 1, 3]), 3)
        print("OK")

    def test_height_checker2(self):
        print("Test heightChecker 2 ... ", end="")
        self.assertEqual(self.sol.heightChecker(heights=[5, 1, 2, 3, 4]), 5)
        print("OK")

    def test_height_checker3(self):
        print("Test heightChecker 3 ... ", end="")
        self.assertEqual(self.sol.heightChecker(heights=[1, 2, 3, 4, 5]), 0)
        print("OK")


if __name__ == "__main__":
    unittest.main()

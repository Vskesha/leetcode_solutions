import unittest
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [n for _, n in sorted(zip(heights, names), reverse=True)]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_sortPeople_1(self):
        print("Test sortPeople 1... ", end="")
        self.assertListEqual(
            ["Mary", "Emma", "John"],
            self.sol.sortPeople(
                names=["Mary", "John", "Emma"], heights=[180, 165, 170]
            ),
        )
        print("OK")

    def test_sortPeople_2(self):
        print("Test sortPeople 2... ", end="")
        self.assertListEqual(
            ["Bob", "Alice", "Bob"],
            self.sol.sortPeople(names=["Alice", "Bob", "Bob"], heights=[155, 185, 150]),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

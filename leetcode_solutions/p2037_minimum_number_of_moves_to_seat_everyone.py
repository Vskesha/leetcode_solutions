import unittest
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(a - b) for a, b in zip(sorted(seats), sorted(students)))


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_min_moves_to_seat_1(self):
        print("Test minMovesToSeat 1 ... ", end="")
        self.assertEqual(
            self.sol.minMovesToSeat(seats=[3, 1, 5], students=[2, 7, 4]), 4
        )
        print("OK")

    def test_min_moves_to_seat_2(self):
        print("Test minMovesToSeat 2 ... ", end="")
        self.assertEqual(
            self.sol.minMovesToSeat(seats=[4, 1, 5, 9], students=[1, 3, 2, 6]),
            7,
        )
        print("OK")

    def test_min_moves_to_seat_3(self):
        print("Test minMovesToSeat 3 ... ", end="")
        self.assertEqual(
            self.sol.minMovesToSeat(seats=[2, 2, 6, 6], students=[1, 3, 2, 6]),
            4,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

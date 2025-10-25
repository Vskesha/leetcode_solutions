import unittest
from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        lg = len(grumpy)
        win = sum(customers[i] for i in range(minutes) if grumpy[i])
        wmax = win

        for si, ei in zip(range(lg), range(minutes, lg)):
            win += customers[ei] * grumpy[ei] - customers[si] * grumpy[si]
            wmax = max(wmax, win)

        return wmax + sum(customers[i] for i in range(lg) if not grumpy[i])


class Solution2:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        lg = len(grumpy)

        sat = sum(customers[i] for i in range(lg) if not grumpy[i])

        win = sum(customers[i] for i in range(minutes - 1) if grumpy[i])
        wmax = win

        for si, ei in zip(range(lg), range(minutes - 1, lg)):
            if grumpy[ei]:
                win += customers[ei]
            wmax = max(wmax, win)
            if grumpy[si]:
                win -= customers[si]

        return wmax + sat


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_max_satisfied_1(self):
        print("Test maxSatisfied 1 ... ", end="")
        self.assertEqual(
            self.sol.maxSatisfied(
                customers=[1, 0, 1, 2, 1, 1, 7, 5],
                grumpy=[0, 1, 0, 1, 0, 1, 0, 1],
                minutes=3,
            ),
            16,
        )
        print("OK")

    def test_max_satisfied_2(self):
        print("Test maxSatisfied 2 ... ", end="")
        self.assertEqual(
            self.sol.maxSatisfied(customers=[1], grumpy=[0], minutes=1), 1
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

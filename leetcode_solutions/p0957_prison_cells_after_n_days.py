import unittest
from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        combs, p = [], 0
        c = tuple(cells)
        b = c = (0, *(int(c[i] == c[i + 2]) for i in range(6)), 0)

        for i in range(1, n):
            combs.append(c)
            c = (0, *(int(c[i] == c[i + 2]) for i in range(6)), 0)
            if c == b:
                p = i
                break

        if p:
            c = combs[(n - 1) % p]

        return list(c)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_prison_after_n_days_1(self):
        print("Test prisonAfterNDays 1... ", end="")
        self.assertListEqual(
            self.sol.prisonAfterNDays(cells=[0, 1, 0, 1, 1, 0, 0, 1], n=7),
            [0, 0, 1, 1, 0, 0, 0, 0],
        )
        print("OK")

    def test_prison_after_n_days_2(self):
        print("Test prisonAfterNDays 2... ", end="")
        self.assertListEqual(
            self.sol.prisonAfterNDays(
                cells=[1, 0, 0, 1, 0, 0, 1, 0], n=1000000000
            ),
            [0, 0, 1, 1, 1, 1, 1, 0],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

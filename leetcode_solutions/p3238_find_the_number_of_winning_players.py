import unittest
from collections import Counter
from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        picks = [[] for _ in range(n)]

        for pl, col in pick:
            picks[pl].append(col)
        ans = 0
        for i, balls in enumerate(picks):
            if balls and max(Counter(balls).values()) > i:
                ans += 1

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_winningPlayerCount_1(self):
        print("Test winningPlayerCount 1... ", end="")
        self.assertEqual(
            2,
            self.sol.winningPlayerCount(
                n=4, pick=[[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]]
            ),
        )
        print("OK")

    def test_winningPlayerCount_2(self):
        print("Test winningPlayerCount 2... ", end="")
        self.assertEqual(
            0, self.sol.winningPlayerCount(n=5, pick=[[1, 1], [1, 2], [1, 3], [1, 4]])
        )
        print("OK")

    def test_winningPlayerCount_3(self):
        print("Test winningPlayerCount 3... ", end="")
        self.assertEqual(
            1, self.sol.winningPlayerCount(n=5, pick=[[1, 1], [2, 4], [2, 4], [2, 4]])
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

import unittest
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        lb = len(books)
        inf = float("inf")
        dp = [inf] * lb
        dp.append(0)

        for i in range(lb - 1, -1, -1):
            w, h = 0, 0
            for j in range(i, lb):
                w += books[j][0]
                if w > shelfWidth:
                    break
                h = max(h, books[j][1])
                dp[i] = min(dp[i], h + dp[j + 1])

        return dp[0]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_min_height_shelves_1(self):
        print("Test minHeightShelves 1... ", end="")
        self.assertEqual(
            self.sol.minHeightShelves(
                books=[[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]],
                shelfWidth=4,
            ),
            6,
        )
        print("OK")

    def test_min_height_shelves_2(self):
        print("Test minHeightShelves 2... ", end="")
        self.assertEqual(
            self.sol.minHeightShelves(
                books=[[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]],
                shelfWidth=4,
            ),
            6,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

import unittest
from functools import cache
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ht = len(triangle)

        for i in range(ht - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += min(
                    triangle[i + 1][j], triangle[i + 1][j + 1]
                )

        return triangle[0][0]


class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ht = len(triangle)

        @cache
        def dp(h, i) -> int:
            if h == ht:
                return 0
            return triangle[h][i] + min(dp(h + 1, i), dp(h + 1, i + 1))

        return dp(0, 0)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_minimum_total_1(self):
        print("Test minimumTotal 1... ", end="")
        self.assertEqual(
            self.sol.minimumTotal(
                triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
            ),
            11,
        )
        print("OK")

    def test_minimum_total_2(self):
        print("Test minimumTotal 2... ", end="")
        self.assertEqual(self.sol.minimumTotal(triangle=[[-10]]), -10)
        print("OK")


if __name__ == "__main__":
    unittest.main()

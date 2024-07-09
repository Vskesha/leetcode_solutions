import unittest
from functools import cache
from itertools import accumulate
from typing import List



class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        ap = list(accumulate(piles, initial=0))
        lp = len(piles)

        @cache
        def dfs(i: int, m: int, alice: bool):
            if lp - i <= m * 2:
                return ap[lp] - ap[i] if alice else 0

            if alice:
                return (
                    max(
                        ap[i + j] + dfs(i + j, max(m, j), False)
                        for j in range(1, 2 * m + 1)
                    )
                    - ap[i]
                )

            return min(dfs(i + j, max(m, j), True) for j in range(1, 2 * m + 1))

        return dfs(0, 1, True)


class Solution2:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dpt = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(2)]

        def dp(i, m, alice):
            if i == n:
                return 0

            if dpt[alice][i][m] != -1:
                return dpt[alice][i][m]

            res = 0 if alice else 1000000
            curr_sum = 0

            for x in range(1, min(2 * m, n - i) + 1):
                if alice:
                    curr_sum += piles[i + x - 1]
                    res = max(res, curr_sum + dp(i + x, max(x, m), 0))
                else:
                    res = min(res, dp(i + x, max(x, m), 1))

            dpt[alice][i][m] = res

            return res

        return dp(0, 1, 1)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_stone_game_ii_1(self):
        print("Test stoneGameII 1... ", end="")
        self.assertEqual(self.sol.stoneGameII(piles=[2, 7, 9, 4, 4]), 10)
        print("OK")

    def test_stone_game_ii_2(self):
        print("Test stoneGameII 2... ", end="")
        self.assertEqual(self.sol.stoneGameII(piles=[1, 2, 3, 4, 5, 100]), 104)
        print("OK")

    def test_stone_game_ii_3(self):
        print("Test stoneGameII 3... ", end="")
        self.assertEqual(self.sol.stoneGameII(piles=[1, 5, 7, 9, 9]), 17)
        print("OK")

    def test_stone_game_ii_4(self):
        print("Test stoneGameII 4... ", end="")
        self.assertEqual(
            self.sol.stoneGameII(
                piles=[
                    3111,
                    4303,
                    2722,
                    2183,
                    6351,
                    5227,
                    8964,
                    7167,
                    9286,
                    6626,
                    2347,
                    1465,
                    5201,
                    7240,
                    5463,
                    8523,
                    8163,
                    9391,
                    8616,
                    5063,
                    7837,
                    7050,
                    1246,
                    9579,
                    7744,
                    6932,
                    7704,
                    9841,
                    6163,
                    4829,
                    7324,
                    6006,
                    4689,
                    8781,
                    621,
                ]
            ),
            112766,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

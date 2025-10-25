import unittest
from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b1 = b0 = inf
        s1 = s0 = 0
        for x in prices:
            if b0 > x:
                b0 = x
            elif s0 < x - b0:
                s0 = x - b0
            if b1 > x - s0:
                b1 = x - s0
            elif s1 < x - b1:
                s1 = x - b1
        return s1


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        lp = len(prices)
        max_price = prices[-1]
        profits = [0] * len(prices)
        for i in range(lp - 2, -1, -1):
            price = prices[i]
            if price > max_price:
                max_price = price
            profits[i] = max(profits[i + 1], max_price - price)
        print(profits)
        min_price = prices[0]
        max_profit = profits[0]
        for i in range(1, lp - 1):
            price = prices[i]
            if price < min_price:
                min_price = price
            else:
                max_profit = max(
                    max_profit, price - min_price + profits[i + 1]
                )

        return max_profit


class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        lp = len(prices)
        profits = [0] * lp

        min_price = prices[0]
        first_max = 0

        for i in range(1, lp):
            price = prices[i]
            if price < min_price:
                min_price = price
            elif price - min_price > first_max:
                first_max = price - min_price
            profits[i] = first_max

        max_price = prices[-1]
        second_max = 0

        for i in range(lp - 2, -1, -1):
            price = prices[i]
            if price > max_price:
                max_price = price
            elif max_price - price > second_max:
                second_max = max_price - price
            profits[i] += second_max

        return max(profits)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_maxProfit_1(self):
        print("Test maxProfit 1... ", end="")
        self.assertEqual(
            6, self.sol.maxProfit(prices=[3, 3, 5, 0, 0, 3, 1, 4])
        )
        print("OK")

    def test_maxProfit_2(self):
        print("Test maxProfit 2... ", end="")
        self.assertEqual(4, self.sol.maxProfit(prices=[1, 2, 3, 4, 5]))
        print("OK")

    def test_maxProfit_3(self):
        print("Test maxProfit 3... ", end="")
        self.assertEqual(0, self.sol.maxProfit(prices=[7, 6, 4, 3, 1]))
        print("OK")


if __name__ == "__main__":
    unittest.main()

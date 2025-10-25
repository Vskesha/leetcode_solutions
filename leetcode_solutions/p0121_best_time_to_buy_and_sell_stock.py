import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                ans = max(ans, price - min_price)

        return ans


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = prices[0]
        for price in prices:
            if price - buy > ans:
                ans = price - buy
            elif price < buy:
                buy = price
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_maxProfit_1(self):
        print("Test maxProfit 1... ", end="")
        self.assertEqual(5, self.sol.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
        print("OK")

    def test_maxProfit_2(self):
        print("Test maxProfit 2... ", end="")
        self.assertEqual(0, self.sol.maxProfit(prices=[7, 6, 4, 3, 1]))
        print("OK")


if __name__ == "__main__":
    unittest.main()

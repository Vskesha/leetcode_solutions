import unittest
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[1000, 0] for _ in range(k + 1)]
        # dp[i][0] - money spent on bying 'i' lots minus profit that was
        #            received from previous 'i-1' buy-sell transactions.
        #            It must be as small as possible.
        # dp[i][1] - profit from 'i'-th buy-sell transactions.
        #            We try to maximize it.

        for price in prices:   # for each endprice in price list
            for i in range(1, k + 1):  # for each number of transactions
                curr_spent = price - dp[i - 1][1]
                # spent money if we buy at this price
                dp[i][0] = min(dp[i][0], curr_spent)
                # and we want to minimize this amount
                curr_profit = price - dp[i][0]
                # received profit if we sell at this price
                dp[i][1] = max(dp[i][1], curr_profit)
                # and we want to maximize this profit

        return dp[k][1]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_maxProfit_1(self):
        print('Test maxProfit 1... ', end='')
        self.assertEqual(2, self.sol.maxProfit(k=2, prices=[2, 4, 1]))
        print('OK')

    def test_maxProfit_2(self):
        print('Test maxProfit 2... ', end='')
        self.assertEqual(7, self.sol.maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3]))
        print('OK')


if __name__ == '__main__':
    unittest.main()

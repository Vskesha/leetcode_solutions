from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = sell = prices[0]
        max_profit = 0
        for price in prices:
            if price > sell + fee:
                sell = price - fee
            elif price < sell:
                max_profit += sell - buy
                buy = sell = price
        max_profit += sell - buy
        return max_profit


def test():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert 8 == sol.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2)
    print("ok\nTest 2 ... ", end="")
    assert 6 == sol.maxProfit(prices=[1, 3, 7, 5, 10, 3], fee=3)
    print("ok")


if __name__ == "__main__":
    test()

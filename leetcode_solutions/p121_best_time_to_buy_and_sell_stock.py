class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


def main():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert 5 == sol.maxProfit(prices=[7, 1, 5, 3, 6, 4])
    print('ok')

    print('Test 2 ... ', end='')
    assert 0 == sol.maxProfit(prices=[7, 6, 4, 3, 1])
    print('ok')


if __name__ == '__main__':
    main()

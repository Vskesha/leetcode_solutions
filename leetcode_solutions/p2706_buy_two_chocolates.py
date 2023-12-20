from heapq import nsmallest
from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        s, ss = 100, 100
        for p in prices:
            if p < s:
                s, ss = p, s
            elif p < ss:
                ss = p
        lo = money - s - ss
        return money if lo < 0 else lo

class Solution2:
    def buyChoco(self, prices: List[int], money: int) -> int:
        cost = sum(nsmallest(2, prices))
        return money-cost if money >= cost else money


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.buyChoco(prices = [1,2,2], money = 3) == 0
    print('OK')

    print('Test 2... ', end='')
    assert sol.buyChoco(prices = [3,2,3], money = 3) == 3
    print('OK')


if __name__ == '__main__':
    test()

import unittest
from heapq import nsmallest
from typing import List

from leetcode_solutions._test_meta import TestMeta


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
        return money - cost if money >= cost else money


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            # "cls_init_args": [],
            # "cls_init_kwargs": dict(),
            "class_methods": ["buyChoco"] * 2,
            # "args": [[], ],
            "kwargs": [
                dict(prices=[1, 2, 2], money=3),
                dict(prices=[3, 2, 3], money=3),
            ],
            "expected": [0, 3],
            # "assert_methods": ["assertMethod"] * n,
        },
    ]


if __name__ == "__main__":
    unittest.main()

# def test():
#     sol = Solution()
#
#     print('Test 1... ', end='')
#     assert sol.buyChoco(prices = [1,2,2], money = 3) == 0
#     print('OK')
#
#     print('Test 2... ', end='')
#     assert sol.buyChoco(prices = [3,2,3], money = 3) == 3
#     print('OK')


# if __name__ == '__main__':
#     test()

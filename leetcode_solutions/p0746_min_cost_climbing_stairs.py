from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost_it = iter(cost)
        a = next(cost_it)
        b = next(cost_it)

        for c in cost_it:
            a, b = b, c + min(a, b)

        return min(a, b)


class Solution1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = b = 0
        for c in cost:
            a, b = b, min(a, b) + c
        return min(a, b)


class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[0], cost[1]

        for i in range(2, len(cost)):
            a, b = b, min(a, b) + cost[i]

        return min(a, b)


def main():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.minCostClimbingStairs(cost=[10, 15, 20]) == 15
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    print('ok')


if __name__ == '__main__':
    main()

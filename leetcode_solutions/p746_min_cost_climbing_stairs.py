class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost_it = iter(cost)
        a = next(cost_it)
        b = next(cost_it)

        for c in cost_it:
            a, b = b, c + min(a, b)

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

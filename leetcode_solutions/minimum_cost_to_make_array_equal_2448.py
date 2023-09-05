class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        left, right = min(nums), max(nums) + 1
        while left < right:
            m = (left + right) // 2
            curr = sum(cost[i] * abs(m - nums[i]) for i in range(n))
            nxt = sum(cost[i] * abs(m + 1 - nums[i]) for i in range(n))

            if nxt > curr:
                right = m
            else:
                left = m + 1

        return sum(cost[i] * abs(nums[i] - left) for i in range(n))


def main():
    sol = Solution()
    print('8 ===', sol.minCost(nums=[1, 3, 5, 2], cost=[2, 3, 1, 14]))
    print('0 ===', sol.minCost(nums=[2, 2, 2, 2, 2], cost=[4, 2, 8, 1, 3]))


if __name__ == '__main__':
    main()

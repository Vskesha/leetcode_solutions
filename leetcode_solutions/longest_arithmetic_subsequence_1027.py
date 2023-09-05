class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        dp = {}
        for r in range(1, len(nums)):
            for l in range(r):
                d = nums[r] - nums[l]
                dp[(r, d)] = dp.get((l, d), 1) + 1
        return max(dp.values())


def main():
    sol = Solution()
    print('4 ===', sol.longestArithSeqLength([3, 6, 9, 12]))
    print('3 ===', sol.longestArithSeqLength([9, 4, 7, 2, 10]))
    print('4 ===', sol.longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]))


if __name__ == '__main__':
    main()

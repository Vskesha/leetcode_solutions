class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        n = len(nums)
        start = 0
        max_len = 1
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                max_len = max(max_len, i - start)
                start = i
        return max(max_len, n - start)


def main():
    sol = Solution()
    print("3 ===", sol.findLengthOfLCIS(nums=[1, 3, 5, 4, 7]))
    print("1 ===", sol.findLengthOfLCIS(nums=[2, 2, 2, 2, 2]))


if __name__ == "__main__":
    main()

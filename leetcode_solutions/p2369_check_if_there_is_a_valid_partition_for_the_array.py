from functools import lru_cache


# recursive dp solution
class Solution:
    def validPartition(self, nums: list[int]) -> bool:

        @lru_cache(None)
        def dp(i):
            if not i:
                return True

            if i > 1 and nums[i - 1] == nums[i - 2] and dp(i - 2):
                return True

            if i > 2 and (nums[i - 1] == nums[i - 2] == nums[i - 3] or nums[i - 3] + 2 == nums[i - 2] + 1 == nums[
                i - 1]) and dp(i - 3):
                return True

            return False

        return dp(len(nums))


# iterative dp solution
class Solution2:
    def validPartition(self, nums: list[int]) -> bool:
        ln = len(nums)
        dp = [False] * (ln + 1)
        dp[0] = True
        dp[1] = False
        dp[2] = nums[0] == nums[1]

        for i in range(3, ln + 1):
            if dp[i - 2] and nums[i - 1] == nums[i - 2]:
                dp[i] = True
            if dp[i - 3]:
                if nums[i - 1] == nums[i - 2] == nums[i - 3] or nums[i - 3] + 2 == nums[i - 2] + 1 == nums[i - 1]:
                    dp[i] = True

        return dp[ln]


def main():
    sol = Solution()
    print('True ===', sol.validPartition(nums=[4, 4, 4, 5, 6]))
    print('False ===', sol.validPartition(nums=[1, 1, 1, 2]))


if __name__ == '__main__':
    main()

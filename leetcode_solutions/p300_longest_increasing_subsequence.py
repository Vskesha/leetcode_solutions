from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        tails = [nums[0]]
        for n in nums:
            if n > tails[-1]:
                tails.append(n)
            else:
                tails[bisect_left(tails, n)] = n
        return len(tails)


def main():
    sol = Solution()
    print('4 ===', sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print('4 ===', sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))
    print('1 ===', sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))


if __name__ == '__main__':
    main()

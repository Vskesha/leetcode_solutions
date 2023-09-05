class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        prev = curr = ans = 0
        for n in nums:
            if n:
                curr += 1
            else:
                ans = max(ans, prev + curr)
                prev = curr
                curr = 0
        ans = max(ans, prev + curr)

        return ans if ans < len(nums) else len(nums) - 1

    def longestSubarray1(self, nums: list[int]) -> int:
        prev_len = curr_len = gap = prev = ans = 0
        n = len(nums)
        nums.append(0)

        for num in nums:
            if num:
                if not prev:
                    prev_len = curr_len
                    curr_len = 0
                curr_len += 1
            else:
                if prev:
                    if gap == 1:
                        ans = max(ans, prev_len + curr_len)
                    else:
                        ans = max(ans, curr_len)
                    gap = 0
                gap += 1
            prev = num

        return ans if ans < n else n - 1

    def longestSubarray2(self, nums: list[int]) -> int:
        prev_len = 0
        curr_len = 0
        ans = 0
        gap = 0
        i = 0
        n = len(nums)
        while i < n:
            gap = 0
            while i < n and not nums[i]:
                gap += 1
                i += 1
            curr_len = 0
            while i < n and nums[i]:
                curr_len += 1
                i += 1
            if gap == 1:
                ans = max(ans, curr_len + prev_len)
            else:
                ans = max(ans, curr_len)
            prev_len = curr_len
        return ans if ans < n else n - 1


def main():
    sol = Solution()
    print('3 ===', sol.longestSubarray([1, 1, 0, 1]))
    print('5 ===', sol.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
    print('2 ===', sol.longestSubarray([1, 1, 1]))


if __name__ == '__main__':
    main()

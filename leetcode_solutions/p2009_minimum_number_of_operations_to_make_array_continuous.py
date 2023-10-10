from bisect import bisect_right
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        new_nums = sorted(set(nums))
        ans = ln = len(nums)
        lnn =len(new_nums)
        i = j = 0
        while i < lnn - ln + ans:
            right = new_nums[i] + ln
            while j < lnn and new_nums[j] < right:
                j += 1
            ans = min(ans, ln + i - j)
            i += 1
        return ans


class Solution1:
    def minOperations(self, nums: List[int]) -> int:
        new_nums = sorted(set(nums))
        ln = len(nums)
        lnn =len(new_nums)
        i = j = 0
        c = 1
        while i < lnn - c:
            right = new_nums[i] + ln
            while j < lnn and new_nums[j] < right:
                j += 1
            c = max(c, j - i)
            i += 1
        return ln - c


class Solution2:
    def minOperations(self, nums: List[int]) -> int:
        ln = len(nums)
        ans = ln
        new_nums = sorted(set(nums))

        for i in range(len(new_nums)):
            right = new_nums[i] + ln - 1
            j = bisect_right(new_nums, right)
            ans = min(ans, ln + i - j)

        return ans


class Solution3:
    def minOperations(self, nums: List[int]) -> int:
        new_nums = sorted(set(nums))
        return min(len(nums) + i - bisect_right(new_nums, new_nums[i] + len(nums) - 1) for i in range(len(new_nums)))


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.minOperations(nums=[4, 2, 5, 3]) == 0
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.minOperations(nums=[1, 2, 3, 5, 6]) == 1
    print('ok')

    print('Test 3 ... ', end='')
    assert sol.minOperations(nums=[1, 10, 100, 1000]) == 3
    print('ok')


if __name__ == '__main__':
    test()

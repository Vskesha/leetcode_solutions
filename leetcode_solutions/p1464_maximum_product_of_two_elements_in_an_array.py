from heapq import heappush, heappushpop
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = b = 0
        for n in nums:
            if n > b:
                a, b = b, n
            elif n > a:
                a = n
        return (a - 1) * (b - 1)


class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        nums = iter(nums)
        h = []
        heappush(h, next(nums))
        heappush(h, next(nums))
        for n in nums:
            heappushpop(h, n)
        return (h[0] - 1) * (h[1] - 1)


class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        h = []
        heappush(h, nums[0])
        heappush(h, nums[1])
        for i in range(2, len(nums)):
            heappushpop(h, nums[i])
        return (h[0] - 1) * (h[1] - 1)


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.maxProduct(nums=[3, 4, 5, 2]) == 12
    print('OK')

    print('Test 2... ', end='')
    assert sol.maxProduct(nums=[1, 5, 4, 5]) == 16
    print('OK')

    print('Test 3... ', end='')
    assert sol.maxProduct(nums=[3, 7]) == 12
    print('OK')


if __name__ == '__main__':
    test()

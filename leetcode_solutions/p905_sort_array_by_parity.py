from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        for n in nums:
            if n % 2:   odd.append(n)
            else:       even.append(n)
        return even + odd


class Solution1:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 == 1]


class Solution2:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] % 2:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1

        return nums


class Solution3:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            while l < r and not nums[l] % 2:
                l += 1
            while l < r and nums[r] % 2:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]

        return nums


def prove(solution: Solution, nums: List[int]):
    nums = solution.sortArrayByParity(nums)
    l, r = 0, len(nums) - 1
    while l < r and not nums[l] % 2:
        l += 1
    while l < r and nums[r] % 2:
        r -= 1
    return r == l


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert prove(sol, nums=[3, 1, 2, 4])
    print('ok\nTest 2 ... ', end='')
    assert prove(sol, nums=[0])
    print('ok')


if __name__ == '__main__':
    test()

from itertools import pairwise
from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return sum(i for i in range(1, len(nums)) if nums[i] != nums[i - 1])


class Solution1:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        k, ans = 0, 0
        for a, b in pairwise(nums):
            if a != b:
                k += 1
            ans += k
        return ans


class Solution2:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                ans += i
        return ans


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.reductionOperations(nums=[5, 1, 3]) == 3
    print('OK')

    print('Test 2 ... ', end='')
    assert sol.reductionOperations(nums=[1, 1, 1]) == 0
    print('OK')

    print('Test 3 ... ', end='')
    assert sol.reductionOperations(nums=[1, 1, 2, 2, 3]) == 4
    print('OK')


if __name__ == '__main__':
    test()

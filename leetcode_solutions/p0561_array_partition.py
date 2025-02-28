from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[i] for i in range(0, len(nums), 2))


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.arrayPairSum(nums=[1, 4, 3, 2]) == 4
    print('OK')

    print('Test 2... ', end='')
    assert sol.arrayPairSum(nums=[6, 2, 6, 5, 1, 2]) == 9
    print('OK')


if __name__ == '__main__':
    test()

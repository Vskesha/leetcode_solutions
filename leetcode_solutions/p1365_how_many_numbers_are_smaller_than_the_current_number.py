from bisect import bisect_left
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        snums = sorted(nums)
        ans = []
        for n in nums:
            ans.append(bisect_left(snums, n))
        return ans


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]
    print('OK')

    print('Test 2... ', end='')
    assert sol.smallerNumbersThanCurrent(nums=[6, 5, 4, 8]) == [2, 1, 0, 3]
    print('OK')

    print('Test 3... ', end='')
    assert sol.smallerNumbersThanCurrent(nums=[7, 7, 7, 7]) == [0, 0, 0, 0]
    print('OK')


if __name__ == '__main__':
    test()

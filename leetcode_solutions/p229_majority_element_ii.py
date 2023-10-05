from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        k = len(nums) / 3
        return [n for n, c in cnt.items() if c > k]


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.majorityElement(nums=[3, 2, 3]) == [3]
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.majorityElement(nums=[1]) == [1]
    print('ok')

    print('Test 3 ... ', end='')
    assert sol.majorityElement(nums=[1, 2]) == [1, 2]
    print('ok')


if __name__ == '__main__':
    test()

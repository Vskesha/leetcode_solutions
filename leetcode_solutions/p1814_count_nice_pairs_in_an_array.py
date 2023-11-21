from collections import Counter
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        cnt = Counter(n - int(str(n)[::-1]) for n in nums)
        ans = 0
        for g in cnt.values():
            ans = (ans + g * (g - 1) // 2) % mod
        return ans


class Solution2:
    def countNicePairs(self, nums: List[int]) -> int:
        return sum(g * (g - 1) // 2 for g in Counter(n - int(str(n)[::-1]) for n in nums).values()) % 1_000_000_007


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.countNicePairs(nums=[42, 11, 1, 97]) == 2
    print('OK')

    print('Test 2 ... ', end='')
    assert sol.countNicePairs(nums=[13, 10, 35, 24, 76]) == 4
    print('OK')


if __name__ == '__main__':
    test()

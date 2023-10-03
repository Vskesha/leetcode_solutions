from collections import Counter
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        counter = Counter(nums)
        for q in counter.values():
            ans += q * (q - 1) // 2
        return ans


class Solution1:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans, cnt = 0, {}
        for n in nums:
            if n in cnt:
                cnt[n] += 1
                ans += cnt[n]
            else:
                cnt[n] = 0
        return ans


class Solution2:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(q * (q - 1) for q in Counter(nums).values()) // 2


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]) == 4
    print('ok')
    print('Test 2 ... ', end='')
    assert sol.numIdenticalPairs(nums=[1, 1, 1, 1]) == 6
    print('ok')
    print('Test 3 ... ', end='')
    assert sol.numIdenticalPairs(nums=[1, 2, 3]) == 0
    print('ok')


if __name__ == '__main__':
    test()

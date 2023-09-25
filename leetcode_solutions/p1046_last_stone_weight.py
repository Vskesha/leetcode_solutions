from bisect import insort
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sts = sorted(stones)
        while len(sts) > 1:
            d = sts.pop() - sts.pop()
            if d:
                insort(sts, d)
        return sts[0] if sts else 0


class Solution2:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = [-w for w in stones]
        heapify(hp)
        while len(hp) > 1:
            heappush(hp, heappop(hp) - heappop(hp))
        return -hp[0]


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.lastStoneWeight(stones = [2,7,4,1,8,1]) == 1
    print('ok\nTest 2 ... ', end='')
    assert sol.lastStoneWeight(stones = [1]) == 1
    print('ok')


if __name__ == '__main__':
    test()

from heapq import heappush
from itertools import accumulate
from typing import List


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        return sum(1 for i, m in enumerate(accumulate(flips, func=max), 1) if i == m)


class Solution1:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans, m = 0, 0

        for i, fl in enumerate(flips, 1):
            m = max(m, fl)
            ans += m == i

        return ans


class Solution2:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans, h = 0, []

        for i, fl in enumerate(flips, 1):
            heappush(h, -fl)
            ans += h[0] == -i

        return ans


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.numTimesAllBlue(flips=[3, 2, 4, 1, 5]) == 2
    print('OK')

    print('Test 2... ', end='')
    assert sol.numTimesAllBlue(flips=[4, 1, 2, 3]) == 1
    print('OK')


if __name__ == '__main__':
    test()

from heapq import heapify, heappop
from math import ceil
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)

        arrivals = [ceil(d / s) for d, s in zip(dist, speed)]
        counts = [0] * n

        for ar in arrivals:
            if ar < n:
                counts[ar] += 1

        for i in range(1, n):
            counts[i] += counts[i - 1]
            if counts[i] > i:
                return i

        return n


class Solution2:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minutes = [d / s for d, s in zip(dist, speed)]
        heapify(minutes)

        for i in range(len(dist)):
            if heappop(minutes) <= i:
                return i

        return len(dist)


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.eliminateMaximum(dist=[1, 3, 4], speed=[1, 1, 1]) == 3
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.eliminateMaximum(dist=[1, 1, 2, 3], speed=[1, 1, 1, 1]) == 1
    print('ok')

    print('Test 3 ... ', end='')
    assert sol.eliminateMaximum(dist=[3, 2, 4], speed=[5, 3, 2]) == 1
    print('ok')


if __name__ == '__main__':
    test()

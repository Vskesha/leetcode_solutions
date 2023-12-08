from bisect import bisect_right, bisect_left
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cp = list(zip(capital, profits))
        heapify(cp)
        af = []

        for _ in range(k):
            while cp and cp[0][0] <= w:
                heappush(af, -heappop(cp)[1])
            if af:
                w -= heappop(af)
            else:
                break

        return w

class Solution1:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profits = [x for _, x in sorted(zip(capital, profits))]
        capital.sort()
        heap = []
        pi = 0

        for _ in range(k):
            li = bisect_right(capital, w)
            for i in range(pi, li):
                heappush(heap, -profits[i])
            pi = li
            if heap:
                w -= heappop(heap)
            else:
                break

        return w


class Solution2:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cp = sorted((c, p) for c, p in zip(capital, profits))
        heap = []
        pi = 0

        for _ in range(k):
            li = bisect_left(cp, (w + 1, 0))
            for i in range(pi, li):
                heappush(heap, -cp[i][1])
            pi = li
            if heap:
                w -= heappop(heap)
            else:
                break

        return w


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.findMaximizedCapital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]) == 4
    print('OK')

    print('Test 2... ', end='')
    assert sol.findMaximizedCapital(k=3, w=0, profits=[1, 2, 3], capital=[0, 1, 2]) == 6
    print('OK')


if __name__ == '__main__':
    test()

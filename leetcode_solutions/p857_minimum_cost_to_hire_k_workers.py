from heapq import heappush, heappop
from fractions import Fraction


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        workers = sorted((Fraction(w, q), q, w)
                         for q, w in zip(quality, wage))

        ans = float('inf')
        pool = []
        sumq = 0
        for ratio, q, w in workers:
            heappush(pool, -q)
            sumq += q

            if len(pool) > k:
                sumq += heappop(pool)

            if len(pool) == k:
                ans = min(ans, ratio * sumq)

        return float(ans)


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert round(sol.mincostToHireWorkers(quality=[10, 20, 5], wage=[70, 50, 30], k=2), 5) == 105.00000
    print('OK')

    print('Test 2... ', end='')
    assert round(sol.mincostToHireWorkers(quality=[3, 1, 10, 10, 1], wage=[4, 8, 2, 2, 7], k=3), 5) == 30.66667
    print('OK')


if __name__ == '__main__':
    test()

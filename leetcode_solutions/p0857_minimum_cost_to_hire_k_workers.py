import unittest
from heapq import heappush, heappop, heappushpop
from fractions import Fraction


class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        workers = sorted((w / q, q) for q, w in zip(quality, wage))
        pool, sumq = [], 0

        for i in range(k):
            heappush(pool, -workers[i][1])
            sumq += workers[i][1]

        ans = workers[k - 1][0] * sumq

        for i in range(k, len(wage)):
            ratio, q = workers[i]
            sumq += q + heappushpop(pool, -q)
            ans = min(ans, ratio * sumq)

        return ans


class Solution2:
    def mincostToHireWorkers(self, quality, wage, k):
        workers = sorted((w / q, q, w) for q, w in zip(quality, wage))

        ans = float("inf")
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


class Solution3:
    def mincostToHireWorkers(self, quality, wage, k):
        workers = sorted((Fraction(w, q), q, w) for q, w in zip(quality, wage))

        ans = float("inf")
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


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_mincost_to_hire_workers_1(self):
        print("Test mincostToHireWorkers 1... ", end="")
        self.assertAlmostEqual(
            self.sol.mincostToHireWorkers(quality=[10, 20, 5], wage=[70, 50, 30], k=2),
            105.00000,
            places=5,
        )
        print("OK")

    def test_mincost_to_hire_workers_2(self):
        print("Test mincostToHireWorkers 2... ", end="")
        self.assertAlmostEqual(
            self.sol.mincostToHireWorkers(
                quality=[3, 1, 10, 10, 1], wage=[4, 8, 2, 2, 7], k=3
            ),
            30.66667,
            places=5,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

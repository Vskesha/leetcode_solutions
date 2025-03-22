import unittest
from heapq import heapify, heappop, heappush, heapreplace, nsmallest
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        l, r, ans = candidates, max(candidates, len(costs) - candidates), 0
        heap = [(n, 0) for n in costs[:l]] + [(n, 1) for n in costs[r:]]
        heapify(heap)
        for _ in range(k):
            val, right = heappop(heap)
            ans += val
            if l != r:
                if right:
                    r -= 1
                    heappush(heap, (costs[r], 1))
                else:
                    heappush(heap, (costs[l], 0))
                    l += 1
        return ans


class Solution1:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        lc = len(costs)
        l, r = candidates, max(candidates, lc - candidates)
        heap = [(n, 0) for n in costs[:l]]
        heap.extend((n, 1) for n in costs[r:])
        heapify(heap)
        ans = 0

        for i in range(k):
            val, right = heappop(heap)
            ans += val
            if l != r:
                r -= right
                heappush(heap, (costs[r if right else l], right))
                l += 1 - right

        return ans


class Solution2:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        lc = len(costs)
        if lc <= candidates * 2:
            return sum(nsmallest(k, costs))

        l, r = candidates, lc - candidates
        lheap, rheap = costs[:l], costs[r:]
        heapify(lheap)
        heapify(rheap)

        ans = 0
        for i in range(k):
            if l == r:
                return ans + sum(nsmallest(k - i, lheap + rheap))
            if rheap[0] < lheap[0]:
                r -= 1
                ans += heapreplace(rheap, costs[r])
            else:
                ans += heapreplace(lheap, costs[l])
                l += 1
        return ans


class Solution3:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if n <= candidates * 2:
            return sum(sorted(costs)[:k])

        total = 0
        l, r = candidates, max(candidates, n - candidates)
        lheap = costs[:l]
        rheap = costs[r:]
        heapify(lheap)
        heapify(rheap)

        for _ in range(k):
            if not rheap or (lheap and lheap[0] <= rheap[0]):
                total += heapreplace(lheap, costs[l]) if l < r else heappop(lheap)
                l += 1
            else:
                total += heapreplace(rheap, costs[r - 1]) if l < r else heappop(rheap)
                r -= 1

        return total


class Solution4:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if n <= candidates * 2:
            costs.sort()
            return sum(costs[:k])

        total = 0
        l, r = candidates, n - candidates
        lcost = sorted(costs[:l], reverse=True)
        rcost = sorted(costs[r:], reverse=True)

        def insor(lst, val):
            l, r = 0, len(lst)
            while l < r:
                m = (l + r) // 2
                if val >= lst[m]:
                    r = m
                else:
                    l = m + 1
            lst.insert(l, val)

        for _ in range(k):
            lmin = lcost[-1] if lcost else 1000000
            rmin = rcost[-1] if rcost else 1000000
            if lmin <= rmin:
                total += lcost.pop()
                if l < r:
                    insor(lcost, costs[l])
                    l += 1
            else:
                total += rcost.pop()
                if l < r:
                    r -= 1
                    insor(rcost, costs[r])

        return total


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_total_cost_1(self):
        print("Test totalCost 1... ", end="")
        self.assertEqual(
            self.sol.totalCost(
                costs=[17, 12, 10, 2, 7, 2, 11, 20, 8], k=3, candidates=4
            ),
            11,
        )
        print("OK")

    def test_total_cost_2(self):
        print("Test totalCost 2... ", end="")
        self.assertEqual(
            self.sol.totalCost(costs=[1, 2, 4, 1], k=3, candidates=3),
            4,
        )
        print("OK")

    def test_total_cost_3(self):
        print("Test totalCost 3... ", end="")
        self.assertEqual(
            self.sol.totalCost(
                costs=[
                    18,
                    64,
                    12,
                    21,
                    21,
                    78,
                    36,
                    58,
                    88,
                    58,
                    99,
                    26,
                    92,
                    91,
                    53,
                    10,
                    24,
                    25,
                    20,
                    92,
                    73,
                    63,
                    51,
                    65,
                    87,
                    6,
                    17,
                    32,
                    14,
                    42,
                    46,
                    65,
                    43,
                    9,
                    75,
                ],
                k=13,
                candidates=23,
            ),
            223,
        )
        print("OK")

    def test_total_cost_4(self):
        print("Test totalCost 4... ", end="")
        self.assertEqual(
            self.sol.totalCost(
                costs=[31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58],
                k=11,
                candidates=2,
            ),
            423,
        )
        print("OK")

    def test_total_cost_5(self):
        print("Test totalCost 5... ", end="")
        self.assertEqual(
            self.sol.totalCost(costs=[10, 1, 11, 10], k=2, candidates=1),
            11,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

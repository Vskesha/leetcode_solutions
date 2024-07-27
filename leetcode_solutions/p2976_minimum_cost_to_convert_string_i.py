import unittest
from collections import defaultdict
from functools import cache
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        def dijkstra(a, adj):
            heap = [(0, a)]
            costs = [-1] * 26

            while heap:
                c, b = heappop(heap)
                for nb, nc in adj[b]:
                    nc += c
                    if costs[nb] == -1 or costs[nb] > nc:
                        costs[nb] = nc
                        heappush(heap, (nc, nb))

            return costs

        adj = [[] for _ in range(26)]
        for a, b, cst in zip(original, changed, cost):
            adj[ord(a) - 97].append((ord(b) - 97, cst))

        min_cost = [[-1] * 26 for _ in range(26)]
        for i in range(26):
            min_cost[i] = dijkstra(i, adj)

        total_cost = 0
        for a, b in zip(source, target):
            if a != b:
                mc = min_cost[ord(a) - 97][ord(b) - 97]
                if mc == -1:
                    return -1
                total_cost += mc

        return total_cost


class Solution2:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        costs = defaultdict(list)
        for orig, chng, cst in zip(original, changed, cost):
            costs[orig].append((chng, cst))

        @cache
        def bfs(orig: str, trgt: str) -> int:
            heap = [(0, orig)]
            visited = set()

            while heap:
                cst, ch = heappop(heap)
                if ch == trgt:
                    return cst
                visited.add(ch)
                for neib, ncst in costs[ch]:
                    if neib not in visited:
                        heappush(heap, (cst + ncst, neib))

            return 0

        ans = 0
        for a, b in zip(source, target):
            if a == b:
                continue
            c = bfs(a, b)
            if c == 0:
                return -1
            ans += c

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_minimumCost_1(self):
        print("Test minimumCost 1... ", end="")
        self.assertEqual(
            28,
            self.sol.minimumCost(
                source="abcd",
                target="acbe",
                original=["a", "b", "c", "c", "e", "d"],
                changed=["b", "c", "b", "e", "b", "e"],
                cost=[2, 5, 5, 1, 2, 20],
            ),
        )
        print("OK")

    def test_minimumCost_2(self):
        print("Test minimumCost 2... ", end="")
        self.assertEqual(
            12,
            self.sol.minimumCost(
                source="aaaa",
                target="bbbb",
                original=["a", "c"],
                changed=["c", "b"],
                cost=[1, 2],
            ),
        )
        print("OK")

    def test_minimumCost_3(self):
        print("Test minimumCost 3... ", end="")
        self.assertEqual(
            -1,
            self.sol.minimumCost(
                source="abcd",
                target="abce",
                original=["a"],
                changed=["e"],
                cost=[10000],
            ),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()

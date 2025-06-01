import unittest
from collections import defaultdict
from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        dijkstra = [inf] * (n + 1)
        dijkstra[0] = dijkstra[k] = 0
        heap = [k]

        while heap:
            curr = heappop(heap)
            for neib, dt in adj[curr]:
                dt += dijkstra[curr]
                if dt < dijkstra[neib]:
                    dijkstra[neib] = dt
                    heappush(heap, neib)

        ans = max(dijkstra)
        return ans if ans < inf else -1


class Solution2:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for fr, to, ti in times:
            graph[fr].append((to, ti))

        heap = [(0, k)]
        visited = {k}

        while len(visited) < n:
            if not heap:
                return -1
            cti, cfr = heappop(heap)
            visited.add(cfr)
            for to, ti in graph[cfr]:
                if to not in visited:
                    heappush(heap, (ti + cti, to))

        return cti


class Solution3:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for fr, to, ti in times:
            graph[fr].append((to, ti))

        nts = [inf] * (n + 1)
        nts[0] = nts[k] = 0
        heap = [(0, k)]

        while heap:
            cti, cfr = heappop(heap)
            for to, ti in graph[cfr]:
                ti += cti
                if ti < nts[to]:
                    nts[to] = ti
                    heappush(heap, (ti, to))

        ans = max(nts)
        return -1 if ans == inf else ans


class Solution4:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for fr, to, tm in times:
            graph[fr].append((to, tm))

        visited = set()
        heap = [(0, k)]
        ans = 0

        while heap:
            d, node = heappop(heap)
            if node in visited:
                continue
            ans = d
            visited.add(node)
            for to, tm in graph[node]:
                if to not in visited:
                    heappush(heap, (d + tm, to))

        return ans if len(visited) == n else -1


class Solution5:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = defaultdict(list)
        time = [-1] * n
        for fr, to, tim in times:
            nodes[fr].append((to, tim))

        def move_from(fr):
            for to, tim in nodes[fr]:
                if time[to - 1] == -1 or time[to - 1] > time[fr - 1] + tim:
                    time[to - 1] = time[fr - 1] + tim
                    move_from(to)

        time[k - 1] = 0
        move_from(k)
        mx = time[0]
        for t in time:
            if t == -1:
                return -1
            if t > mx:
                mx = t
        return mx


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_network_delay_time_1(self):
        print("test networkDelayTime 1... ", end="")
        self.assertEqual(
            self.sol.networkDelayTime(
                times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2
            ),
            2,
        )
        print("OK")

    def test_network_delay_time_2(self):
        print("test networkDelayTime 2... ", end="")
        self.assertEqual(self.sol.networkDelayTime(times=[[1, 2, 1]], n=2, k=1), 1)
        print("OK")

    def test_network_delay_time_3(self):
        print("test networkDelayTime 3... ", end="")
        self.assertEqual(self.sol.networkDelayTime(times=[[1, 2, 1]], n=2, k=2), -1)
        print("OK")


if __name__ == "__main__":
    unittest.main()

import unittest
from collections import defaultdict
from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    def modifiedGraphEdges(
        self, n: int, edges: List[List[int]], source: int, destination: int, target: int
    ) -> List[List[int]]:
        graph = defaultdict(dict)
        allowed = [[False] * n for _ in range(n)]

        for fr, to, wt in edges:
            if wt == -1:
                allowed[fr][to] = True
                allowed[to][fr] = True
            wt = abs(wt)
            graph[fr].update({to: wt})
            graph[to].update({fr: wt})

        dist_less = True
        dest_reachable = False

        while dist_less:
            prevs = list(range(n))
            dists = [inf] * n
            dists[source] = 0
            heap = [(0, source)]

            while heap:
                d, node = heappop(heap)
                if d > target:
                    dist_less = False
                    break
                if node == destination:
                    dest_reachable = True
                    if d == target:
                        dist_less = False
                        break
                    prev = prevs[node]
                    while prev != node and not allowed[prev][node]:
                        node, prev = prev, prevs[prev]
                    if prev == node:
                        return []
                    graph[node][prev] += target - d
                    graph[prev][node] += target - d
                    break
                for neib in graph[node]:
                    nd = d + graph[node][neib]
                    if nd < dists[neib]:
                        dists[neib] = nd
                        prevs[neib] = node
                        heappush(heap, (nd, neib))

        if not dest_reachable:
            return []

        for i in range(len(edges)):
            fr, to, _ = edges[i]
            edges[i][2] = graph[fr][to]

        return edges


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    @staticmethod
    def get_min_distance(n, edges, source, destination):
        graph = defaultdict(list)
        for fr, to, wt in edges:
            graph[fr].append((to, wt))
            graph[to].append((fr, wt))

        # Dijkstra's algorithm
        heap = [(0, source)]
        dists = [inf] * n

        while heap:
            d, node = heappop(heap)
            if node == destination:
                return d
            for neib, nd in graph[node]:
                nd += d
                if nd < dists[neib]:
                    dists[neib] = nd
                    heappush(heap, (nd, neib))
        return 0

    def test_modifiedGraphEdges_1(self):
        print("Test modifiedGraphEdges 1... ", end="")
        n = 5
        edges = [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]]
        source = 0
        destination = 1
        target = 5
        output = [[4, 1, 1], [2, 0, 1], [0, 3, 3], [4, 3, 1]]
        new_edges = self.sol.modifiedGraphEdges(n, edges, source, destination, target)
        min_dist1 = self.get_min_distance(n, new_edges, source, destination)
        if output:
            min_dist_out = self.get_min_distance(n, output, source, destination)
            self.assertEqual(min_dist_out, target)
            self.assertEqual(min_dist1, target)
        else:
            self.assertEqual(new_edges, output)
        print("OK")

    def test_modifiedGraphEdges_2(self):
        print("Test modifiedGraphEdges 2... ", end="")
        n = 3
        edges = [[0, 1, -1], [0, 2, 5]]
        source = 0
        destination = 2
        target = 6
        output = []
        new_edges = self.sol.modifiedGraphEdges(n, edges, source, destination, target)
        min_dist1 = self.get_min_distance(n, new_edges, source, destination)
        if output:
            min_dist_out = self.get_min_distance(n, output, source, destination)
            self.assertEqual(min_dist_out, target)
            self.assertEqual(min_dist1, target)
        else:
            self.assertEqual(new_edges, output)
        print("OK")

    def test_modifiedGraphEdges_3(self):
        print("Test modifiedGraphEdges 3... ", end="")
        n = 4
        edges = [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, -1]]
        source = 0
        destination = 2
        target = 6
        output = [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, 1]]
        new_edges = self.sol.modifiedGraphEdges(n, edges, source, destination, target)
        min_dist1 = self.get_min_distance(n, new_edges, source, destination)
        if output:
            min_dist_out = self.get_min_distance(n, output, source, destination)
            self.assertEqual(min_dist_out, target)
            self.assertEqual(min_dist1, target)
        else:
            self.assertEqual(new_edges, output)
        print("OK")

    def test_modifiedGraphEdges_4(self):
        print("Test modifiedGraphEdges 4... ", end="")
        n = 4
        edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3]]
        source = 0
        destination = 2
        target = 1
        output = []
        new_edges = self.sol.modifiedGraphEdges(n, edges, source, destination, target)
        min_dist1 = self.get_min_distance(n, new_edges, source, destination)
        if output:
            min_dist_out = self.get_min_distance(n, output, source, destination)
            self.assertEqual(min_dist_out, target)
            self.assertEqual(min_dist1, target)
        else:
            self.assertEqual(new_edges, output)
        print("OK")

    def test_modifiedGraphEdges_5(self):
        print("Test modifiedGraphEdges 5... ", end="")
        n = 4
        edges = [[0, 1, -1], [2, 0, 2], [3, 2, 6], [2, 1, 10], [3, 0, -1]]
        source = 1
        destination = 3
        target = 12
        output = [[0, 1, 11], [2, 0, 2], [3, 2, 6], [2, 1, 10], [3, 0, 1]]
        new_edges = self.sol.modifiedGraphEdges(n, edges, source, destination, target)
        min_dist1 = self.get_min_distance(n, new_edges, source, destination)
        if output:
            min_dist_out = self.get_min_distance(n, output, source, destination)
            self.assertEqual(min_dist_out, target)
            self.assertEqual(min_dist1, target)
        else:
            self.assertEqual(new_edges, output)
        print("OK")


if __name__ == "__main__":
    unittest.main()
